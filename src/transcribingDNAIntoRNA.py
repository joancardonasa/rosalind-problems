# -*- coding: utf-8 -*-
"""
Created on Sun Nov 15 21:08:34 2020

@author: Jonordona
@ID: RNA
@Title: Transcribing DNA into RNA
"""
def transcribe_dna_to_rna(dna):
    transcription = {
        'A': 'A',
        'C': 'C',
        'G': 'G',
        'T': 'U'
    }
    
    rna = ''
    for element in dna:
        rna += transcription[element]
        
    return rna
