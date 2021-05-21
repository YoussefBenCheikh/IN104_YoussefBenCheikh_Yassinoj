#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Apr 27 16:59:23 2021

@author: youssefbencheikh
"""

from nltk.corpus import stopwords
from nltk import word_tokenize, sent_tokenize
from nltk.stem import WordNetLemmatizer
import string
from utils import is_number


class PreprocessData:

    def __init__(self, text):
        self.text = text

    stop_words = set(stopwords.words('english'))
    punctuation = string.punctuation
    lemmatizer = WordNetLemmatizer()


    def convert_lowercase(self):
        """
        It converts the text to lower case
        :return: lower case text
        :rtype: str
        """
        return self.text.lower()

    def remove_stop_words(self, text):
        """
        It removes the stopwords
        :param text: it is the text of the article
        :type: str
        :return text: article text without stop words
        :rtype: str
        """
        if isinstance(text, str):
            lst_words = [word for word in word_tokenize(text) if word not in self.stop_words]
        return ' '.join(lst_words)

    def remove_punctuation(self, text):
        """
        It removes the punctuation
        :param text: it is the text of the article
        :type: str
        :return text: article text without punctuation
        :rtype: str
        """
        if isinstance(text, str):
            lst_words = [word for word in word_tokenize(text) if word not in string.punctuation]
        return ' '.join(lst_words)
    
    
    def remove_number(self, text):
        """
        It removes the numbers (int or float)
        :param text: it is the text of the article
        :type: str
        :return text: article text without stop words
        :rtype: str
        """
        if isinstance(text, str):
            lst_words = [word for word in word_tokenize(text) if not is_number(word)]
        return ' '.join(lst_words)



    def remove_special_character(self, text):
        """
        :param text: it is the text of the article
        :type: str
        :return text: article text without special characters
        :rtype: str
        """
        if isinstance(text, str):
            lst_characters = [character for character in text if character.isalnum() or character==" "]
        return ''.join(lst_characters)
        
    def lemmatization_text(self, text):
        """
        :param text: it is the text of the article
        :type: str
        :return text: inflected forms of a word back to 
        original so they can be analysed as a single item
        :rtype: str
        """
        if isinstance(text, str):
            lst_words = [self.lemmatizer.lemmatize(word) for word in word_tokenize(text)]
        return ' '.join(lst_words)