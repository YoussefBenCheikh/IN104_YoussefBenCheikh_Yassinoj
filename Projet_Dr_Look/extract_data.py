#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Apr 27 16:55:32 2021

@author: youssefbencheikh
"""

class ExtractData:

    def __init__(self, data):
        self.data = data

    def get_paper_id(self):
        """It returns the id paper
        :return: id_paper
        :rtype id_paper: str"""
        return self.data['paper_id']

    def get_title(self):
        """
        It returns the title of the paper
        :return: title
        :rtype title: str
        """
        return self.data['metadata']['title'].lower()

    def get_text(self):
        """It returns the content of the paper
        :return text or title article in lowercase
        :rtype: str
        """
        L = self.data['body_text']
        text = ""
        for dic in L :
            text += dic['text']

        
        return text