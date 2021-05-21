#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Apr 27 16:58:31 2021

@author: youssefbencheikh
"""

import json
import glob
import sys
from langdetect import detect

from extract_data import ExtractData
from preprocess_data import PreprocessData
from utils import read_json  
from utils import write_file
if __name__ == '__main__':
    path_documents = sys.argv[1]
    list_documents = glob.glob(path_documents + '*.json')
    print("nombre de documents traitées :",len(list_documents))
    # Path of each document
    for path_doc in list_documents:
        # Load json
        data = read_json(path_doc)
        # object
        obj_data = ExtractData(data)
        # call get_text method
        text = obj_data.get_text()

        # make sure the article is in english
        if detect(text)=='en':
          
          
          # call get_paper_id method
          paper_id = obj_data.get_paper_id()
          
          # call get_title method
          title = obj_data.get_title()
       
          # Object to pre-process the text
          obj_preprocess = PreprocessData(text)
          # Convert the text to lower case
          obj_preprocess.text = obj_preprocess.convert_lowercase()
        
          # Remove punctuation
          obj_preprocess.text = obj_preprocess.remove_punctuation(obj_preprocess.text)
        
          # Remove numbers
          obj_preprocess.text = obj_preprocess.remove_number(obj_preprocess.text)
        
          # Remove stop words
          obj_preprocess.text = obj_preprocess.remove_stop_words(obj_preprocess.text)
        
          # Remove the special characters
          obj_preprocess.text = obj_preprocess.remove_special_character(obj_preprocess.text)
        
          # Lemmatization
          obj_preprocess.text = obj_preprocess.lemmatization_text(obj_preprocess.text)
        
          # Write the documents
          path_file = sys.argv[2]+paper_id+".txt"
          write_file(path_file, title+obj_preprocess.text)
        
        
        
        
        
        
        