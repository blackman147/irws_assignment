import sys
from math import log

# input file is the 1st argument, output file is the 2nd argument
if len(sys.argv) > 1:
    input_file = sys.argv[1]
else:
    input_file = "inverted_index.txt"

if len(sys.argv) > 2:
    output_file = sys.argv[2]
else:
    output_file = "tfidf_weights.txt"

# use a dictionary to store the number of occurrences of each term in each document

term_dict = {}

with open(input_file, 'r') as f:
    for line in f:

        line = line.split("\t")

        term = line[0]

        files = line[1:]
        files2 = []

        for file in files:
            try:
                if file[0] == "D":
                    files2.append(file)
            except:
                pass
        files = files2

        for file in files:

            file = file.split("[")

            file_name = file[0]

            cnt = int(file[1].split("]")[0])

            if term not in term_dict:
                term_dict[term] = {}

            if file_name not in term_dict[term]:

                term_dict[term][file_name] = cnt

            else:

                term_dict[term][file_name] += cnt

# create the TF-IDF weights matrix
# format : <term><TAB><file_name>[<number_of_occurrences>]<TAB><file_name>[<number_of_occurrences>]...
with open(output_file, 'w') as f:
    f.write("D1\tD2\tD3\tD4\tD5\tD6\tD7\tD8\tD9\tD10\tD11\tD12\tD13\tD14\tD15\tD16\tD17\tD18\tD19\tD20")

    for term in term_dict:
        # get the number of documents that contain the term and number of occurrences of the term in each document
        # and replace any nonexistent file with 0
        num_docs = len(term_dict[term])

        docs_with_term = term_dict[term]

        for j in range(1, 51):
            if "D" + str(j) not in docs_with_term:
                docs_with_term["D" + str(j)] = 0.001

        op_string = term + "\t"
        # for each file that contains the term, getting the number of occurrences of the term in the file
        # and calculating the TF-IDF weight, restricting to 3 decimal places
        for file in docs_with_term:

            cnt = docs_with_term[file]

            tfidf = cnt / num_docs * log(num_docs / cnt)

            tfidf = round(tfidf, 3)
            # if the TF-IDF weight is 0.001, replace it with 0 because it cannot have a negative TF-IDF weight.
            if tfidf == 0.001:
                tfidf = 0

            if tfidf < 0:
                tfidf = 0
            # adding the TF-IDF weight to the output string, removing the last TAB
            op_string += str(tfidf) + "\t"

        op_string = op_string[:-1]

        f.write(op_string + "\n")
