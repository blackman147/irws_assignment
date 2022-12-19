import os
import sys
import re

from nltk.stem import PorterStemmer

if len(sys.argv) > 1:
    input_folder = sys.argv[1]
else:
    input_folder = "documents"

if len(sys.argv) > 2:
    output_folder = sys.argv[2]
else:
    output_folder = "output"

if len(sys.argv) > 3:
    stopwords_filename = sys.argv[3]
else:
    stopwords_filename = "stopwords.txt"


if not os.path.exists(output_folder):
    os.makedirs(output_folder)


stopwords = []
with open(stopwords_filename, 'r') as f:
    for line in f:
        stopwords.append(line.strip())

files = os.listdir(input_folder)

for file in files:
    with open(input_folder + "/" + file, 'r') as f:
        text = f.read()

        text = re.sub(r'[^\w\s]', '', text)

        tokens = text.split()

        tokens = [token.strip() for token in tokens]

        tokens = [token for token in tokens if token not in stopwords]

        stemmer = PorterStemmer()

        tokens = [stemmer.stem(token, i=0, j=len(token) - 1) for token in tokens]

        tokens = [token.lower() for token in tokens]

        tokens = [token for token in tokens if not token.isdigit()]

        tokens = [token for token in tokens if token != '']

        with open(output_folder + "/" + file, 'w') as f:
            f.write(' '.join(tokens))
