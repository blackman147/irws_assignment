import os
import sys
import re

if len(sys.argv) > 1:
    input_folder = sys.argv[1]
else:
    input_folder = "output"

if len(sys.argv) > 2:
    output_file = sys.argv[2]
else:
    output_file = "inverted_index.txt"

# reading all files in input folder, getting all tokens from all files and making the tokens unique
files = os.listdir(input_folder)

tokens = []
for file in files:
    with open(input_folder + "/" + file, 'r') as f:
        text = f.read()
        text = re.sub(r'[^\w\s]', '', text)
        tokens += text.split()

tokens = list(set(tokens))

# for all tokens print the file name and the number of occurrences
# getting all files that contains the token, counting the number of occurrences of the token in the file and
# printing the token and the files that contains it to the output file.
for token in tokens:

    files_with_token = []
    files_with_token_str = ""
    for file in files:
        with open(input_folder + "/" + file, 'r') as f:
            text = f.read()
            if token in text:
                files_with_token.append(file)

                cnt = text.count(token)
                files_with_token_str += file.split(".")[0] + "[" + str(cnt) + "]" + "\t"

    with open(output_file, 'a') as f:
        f.write(token + "\t" + files_with_token_str + "\n")

