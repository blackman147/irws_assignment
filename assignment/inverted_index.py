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


import re

def clean_text(text):
  # Remove any HTML tags
  text = re.sub(r'<[^>]*>', '', text)

  # Remove any non-alphanumeric characters
  text = re.sub(r'[^\w\s]', '', text)

  # Convert all whitespace to a single space
  text = re.sub(r'\s+', ' ', text)

  # Remove leading and trailing whitespace
  text = text.strip()

  return text

# Example usage
scraped_text = "This is some <b>bold</b> text with special characters like $ and %"
cleaned_text = clean_text(scraped_text)

print(cleaned_text)
# Output: "This is some bold text with special characters like and"
