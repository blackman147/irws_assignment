# irws_assignment
python -m venv irws_env 
.\env\Scripts\activate -> create and run virtual python environment

pip install -r requirements.txt -> install packages


*****************************************
MILESTONE 1
*****************************************
>o Name of your script/code/program
-- griffith.py


>o List of system requirements:
-- Operating system : mac os monterey v 12.6
-- RAM : 8GB
-- Disk : 250GB


>o Language and version that it is written in:
-- Python 3.6.5
-- scrapy 2.7.1
-- requests 2.18.4

>o List of files in the application or script:
-- scrapping.py
-- output folder


example input -> python scrapping.py documents

example output -> documents/D0,D2,..D20
*****************************************
MILESTONE 2
*****************************************
>o Name of your script/code/program
-- preprocessing.py


>o List of system requirements:
-- Operating system : mac os monterey v 12.6
-- RAM : 8GB
-- Disk : 250GB


>o Language and version that it is written in:
-- Python 3.6.5


>o List of files in the application or script:
-- preprocessing.py
-- stopwords.txt
-- stemmer.py
-- output folder

example input -> python preprocessing.py documents preprocessed stopwords.txt

example output -> preprocessed/D1,D2,..D49
*****************************************
MILESTONE 3
*****************************************
>o Name of your script/code/program
-- inverted_index.py


>o List of system requirements:
-- Operating system : mac os monterey v 12.6
-- RAM : 8GB
-- Disk : 250GB


>o Language and version that it is written in:
-- Python 3.6.5


>o List of files in the application or script:
-- inverted_index.py
-- input folder
-- output file

example input -> python inverted_index.py preprocessed inverted_index.txt

example output -> inverted_index.txt
*****************************************
MILESTONE 4
*****************************************
>o Name of your script/code/program
-- TF_IDF.py

List of system requirements:
-- Operating system : mac os monterey v 12.6
-- RAM : 8GB
-- Disk : 250GB



>o Language and version that it is written in:
-- Python 3.6.5
-- IDE: VS Code

>o List of files in the application or script:
-- TF_IDF.py
-- documents folder
-- output folder

example input -> python TF_IDF.py inverted_index.txt tfidf.txt

example output -> tfidf.txt
*****************************************
MILESTONE 5
*****************************************
>o Name of your script/code/program
-- cosine_similarity.py


>o List of system requirements:
-- Operating system : mac os monterey v 12.6
-- RAM : 8GB
-- Disk : 250GB


>o Language and version that it is written in:
-- Python 3.6.5
-- IDE: pycharm

>o List of files in the application or script:
-- cosine_similarity.py
-- input file

example input -> python cosine_similarity.py tfidf.txt D3 D5

example output -> cosine similarity:  0.777
*****************************************
MILESTONE 6
*****************************************
>o Name of your script/code/program
-- IR.py


>o List of system requirements:
-- Operating system : mac os monterey v 12.6
-- RAM : 8GB
-- Disk : 250GB
> 
> 


>o Language and version that it is written in:
-- Python 3.6.5
-- IDE: pycharm

>o List of files in the application or script:
-- IR.py
-- stemmer.py
-- stopwords.txt
-- input
-- output

example install -> python IR.py "...." stopwords.txt

example output ->
