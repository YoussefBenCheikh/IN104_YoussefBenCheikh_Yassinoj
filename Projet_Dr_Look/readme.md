# Dr.LOOK

## About this code

This repository contains the code related to the IN104 Project :  Search engine for Covid-19.
It is a search engine for COVID-19, which aims to find the most related articles to what your looking for.


## Data

We used a COVID-19 Open Research Dataset (CORD-19), that was proposed by the White House
and research groups. It consists of 33.31 GB of information that includes target
tablets, ready-to-use embeddings, and json articles.
we used a subset of this dataset that you can download from this link : https://drive.google.com/drive/folders/1zTtY_AQk5Me16OORSnta9IZ7kSuu6uFh

## How to run the search engine :

#### Cleaning docs and getting them ready to index

```bash
python makecleandocs.py /Users/Path_to_json_data_base/ /Users/Path_where_to_save_clean_docs/

```
#### Index if not indexed yet and search

```bash
python indexandsearch.py /Users/Path_to_Clean_Docs/ /Users/Path_where_to_save_index/ "keywords you're looking for"

```

Code files :

1. extract_data.py

    This code has methods that can help you extract data from a json file, such as title, paper_id and content.

    
 2. preprocess_data.py
    
    In this code  you find the methods abling the engine to clean text : lower case the text, delete the special characters, numbers, punctuation and stop words and lemmatize.

    
 3. makecleandocs.py

    Converts the json data base docs to clean txt docs using the methods in preprocess_data.py.
    
 4. indexandsearch.py
 
    This is the code in charge of indexation and the search.
    
 5. utils.py
 
    Some useful functions.


## Remarks
The search engine browses only the articles in english.
The search engine shows the best ten results, to modify the number access to the variable number_docs_result_search in indexandsearch.py.
The search engine indexs 5000 document, to modify the number access to the variable num_docs_index in indexandsearch.py.
If you misspelled a word, Dr.LOOK will suggest three corrections based on the words in the articles.
