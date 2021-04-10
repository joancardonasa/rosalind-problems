# -*- coding: utf-8 -*-
"""
Created on Sun Nov 15 21:15:37 2020

@author: Jonordona
@ID: REVC
@Title: Complementing a Strand of DNA
"""
def reverse_complement(dna):
    complement_map = {
        'A': 'T',
        'C': 'G',
        'G': 'C',
        'T': 'A'
    }
    
    rev_complement = ''
    for element in dna[::-1]:
        rev_complement += complement_map[element]
    
    return rev_complement
        
