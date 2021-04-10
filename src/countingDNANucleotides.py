# -*- coding: utf-8 -*-
"""
Created on Sun Nov 15 20:52:24 2020

@author: Jonordona
@ID: DNA
@Title: Counting DNA Nucleotides
"""
def count_dna_nucleotides(text):
    nucleotide_count = {
        'A': 0,
        'C': 0,
        'G': 0,
        'T': 0
    }
    
    for element in text:
        nucleotide_count[element] += 1
    
    return nucleotide_count
        
