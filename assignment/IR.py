import os
import sys
from math import log
from nltk.stem import PorterStemmer

# the first argument is the input folder, the second argument is the query while stopwords file is the third argument
# query will be converted to lower case
if len(sys.argv) > 1:
    folder = sys.argv[1]
else:
    folder = "documents"

if len(sys.argv) > 2:
    query = sys.argv[2]
else:
    query = "document sample"

query = query.lower()

if len(sys.argv) > 3:
    stopwords_file = sys.argv[3]
else:
    stopwords_file = "stopwords.txt"

stopwords = []
with open(stopwords_file, 'r') as f:
    for line in f:
        stopwords.append(line.strip())

files = os.listdir(folder)

query_tokens = query.split()

query_tokens = [PorterStemmer().stem(token, i=0, j=len(token) - 1) for token in query_tokens]

# retrieve the  score for every token in every file and  store it in a dictionary
score_dict = {}

num_docs = len(files)


def get_score(file):
    with open("./" + file, 'r') as f:
        text = f.read()

    tokens = text.split()

    tokens = [PorterStemmer().stem(token, i=0, j=len(token) - 1) for token in tokens]

    tokens = [token.lower() for token in tokens]

    tokens = [token for token in tokens if token not in stopwords]

    # getting the cosine similarity between the query and the file
    # getting the number of tokens and unique tokens in the file and the query,

    number_docs = len(files)

    number_tokens = len(set(tokens))

    number_query_tokens = len(set(query_tokens))

    number_file_tokens = len(tokens)

    # retrieve the tf-idf for every token in the file and query
    # store the tf-idf in a dictionary

    tfidf_dict = {}
    for token in tokens:
        # to get the tf-idf for the token in the file and the query
        tfidf_dict[token] = log(1 + number_file_tokens / number_tokens) * log(number_docs / (1 + tokens.count(token)))
    for token in query_tokens:
        tfidf_dict[token] = log(1 + number_query_tokens / number_query_tokens) * log(
            number_docs / (1 + tokens.count(token)))

    # get the cosine similarity between the query and the file and get the sum of the squares of the query,
    # dot product of the query and the file and to get the cosine similarity and the score
    sum_query_squares = sum([tfidf_dict[token] ** 2 for token in query_tokens])

    sum_file_squares = sum([tfidf_dict[token] ** 2 for token in tokens])

    dot_product = sum([tfidf_dict[token] * tfidf_dict[token] for token in query_tokens])

    cosine_similarity = dot_product / (sum_query_squares ** 0.5 * sum_file_squares ** 0.5)

    score = cosine_similarity
    return score


for file in files:
    file_name = file.split(".")[0]

    file_path = os.path.join(folder, file)

    score = get_score(file_path)

    score_dict[file_name] = score

print("\n")

sorted_score_dict = sorted(score_dict.items(), key=lambda kv: kv[1], reverse=True)

for key, value in sorted_score_dict:
    print(key, value)
