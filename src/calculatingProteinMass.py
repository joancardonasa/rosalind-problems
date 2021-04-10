# -*- coding: utf-8 -*-
"""
Created on Sat Dec 12 22:40:09 2020

@author: Jonordona
@ID: PRTM
@Title: Calculating Protein Mass
@Explanation: Each of the 20-symbol amino acids has a weight.

Given a protein, a weighted string of amino acids, 
we wish to compute the weight of such string in atomic mass units (Dalton).
"""
import pandas as pd

def calculate_protein_mass(w_string):
    mass = pd.read_csv('lookup/monoisotopic_mass.csv', 
                           index_col='aminoacid_res', 
                           sep = '|').to_dict()['mass']
    
    weights = [mass[am] for am in w_string]
    return sum(weights)
