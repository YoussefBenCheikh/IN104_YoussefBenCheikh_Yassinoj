#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Apr 10 18:17:47 2021

@author: youssefbencheikh
"""

class logement :
    def __init__(self, adresse, proprietaire, date_construction):
        self.adresse = adresse
        self.proprietaire = proprietaire
        self.date_construction = date_construction
        
    def getAdress(self) :
        return self.adresse
    def getProp(self):
        return self.proprietaire
    def getDateConst(self):
        return self.date_construction
    


class maison (logement) :
    def __init__(self, adresse, proprietaire, date_construction, surface, nb_fenetres):
        super().__init__(adresse, proprietaire, date_construction)
        self.surface = surface
        self.nb_fenetres = nb_fenetres
    
    def getSurface(self):
        return self.surface
    def getFenetres(self):
        return self.nb_fenetres
        
        
class immeuble (logement) :
    def __init__(self, adresse, proprietaire, date_construction, nb_appartement, ascenseur):
        super().__init__(adresse, proprietaire, date_construction)
        self.nb_appartement = nb_appartement
        self.ascenseur = ascenseur
    
    def getNbApp(self):
        return self.nb_appartement
    def getAscn(self):
        return self.ascenseur
    

