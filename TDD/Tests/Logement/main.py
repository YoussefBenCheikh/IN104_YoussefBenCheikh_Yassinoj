#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Apr 10 19:42:24 2021

@author: youssefbencheikh
"""
import Logement




#maison 1
adresse = 'Somewhere in Earth'
proprietaire = 'Someone'
date_construction = '01/01/1999'
surface = 120
nb_fenetres = 20

maison1 = Logement.maison(adresse, proprietaire, date_construction, surface, nb_fenetres)

#immeuble 1
adresse = 'Somewhere else in Earth'
proprietaire = 'Someone else'
date_construction = '01/01/1999'
nb_appartement = 60
ascenseur = True

immeuble1 = Logement.immeuble(adresse, proprietaire, date_construction, nb_appartement, ascenseur)

print("maison 1 est à : {}, elle est propriétée de : {}, construite le {}.".format(maison1.getAdress(),maison1.getProp(),maison1.getDateConst()))
print("immeuble 1 est à : {}, il est propriété de : {}, construit le {}.".format(immeuble1.getAdress(),immeuble1.getProp(),immeuble1.getDateConst()))