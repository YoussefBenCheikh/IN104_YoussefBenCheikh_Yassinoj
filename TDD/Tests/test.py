#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Apr 18 02:15:11 2021

@author: youssefbencheikh
"""


import unittest
import Logement 




#maison 1
adresse = 'Somewhere in Earth'
proprietaire = 'Someone'
date_construction = '01/01/1999'
surface = 120
nb_fenetres = 20

maison1 = Logement.maison(adresse, proprietaire, date_construction, surface, nb_fenetres)



class Test(unittest.TestCase):

    def test_getAdress(self):
        self.assertEqual(maison1.getAdress(), 'Somewhere in Earth', "Should be Somewhere in Earth")

    def test_getProp(self):
        self.assertEqual(maison1.getProp(), 'Someone', 'Should be Someone')

    def test_Surface(self):
        self.assertEqual(maison1.getSurface(), 120, 'Should be 120')
    def test_get_fenetres(self):
        self.assertEqual(maison1.getFenetres(), 20, 'Should be 20')

if __name__ == '__main__':
    unittest.main()