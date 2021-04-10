# -*- coding: utf-8 -*-
"""
Created on Sun Nov 29 12:17:10 2020

@author: Jonordona
@ID: SUBS
@Title: Finding a Motif in DNA
@Explanation: Finding a common interval of DNA in the genomes of two
different organisms suggests that the string has the same function.

Motif is a commonly shared string of DNA. A common task is to search an
organism's genome for a known motif.

Genomes are filled with intervals that occur multiple times. These are called
repeats. Their frequent occurrence makes us suspect that it may not be
happening by random chance, and thus show the actual powert that the DNA
language holds.

In humans the most common repeat is Alu, about 300 bp long and recurs
around a million times in the human genome. It has not been found to serve
a specific goal, and appears to be parasitic.
"""
def finding_motif_in_dna(dna_interval, motif):
    
    locations = []
    
    for position, nucleotide in enumerate(dna_interval):
        
        if motif == dna_interval[position:position + len(motif)]:
            # +1 has to be added since we want 1-based array indexing
            locations.append(position + 1)
            
    return locations
    