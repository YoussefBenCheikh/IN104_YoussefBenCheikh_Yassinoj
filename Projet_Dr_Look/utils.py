#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Apr 27 17:00:06 2021

@author: youssefbencheikh
"""

import json


def is_number(s):
    """It checks if the entry variable
    is a number (float or int)
    :return: True or False
    :rtype bool """
    try:
        float(s)
        return True
    except ValueError:
        return False


def read_json(path_file):
    """It reads a json document
    :return: json data
    :rtype dic_data: dictionary """
    with open(path_file) as json_file:
        dic_data = json.load(json_file)
        return dic_data


def write_file(path_file, title_or_content):
    """It creates a new document
    :param path_file: it is the path you will save the document
    :param title_or_content: yu will save the text or the title document
    :type path_file: str
    :type title_or_content: str
    """
    file = open(path_file, "w+")
    file.write(title_or_content)
    file.close()