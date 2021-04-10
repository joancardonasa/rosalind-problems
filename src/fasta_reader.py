# -*- coding: utf-8 -*-
"""
Created on Sun Nov 29 15:42:09 2020

@author: Jonordona
@Explanation: Utility to read fasta files and return parsed dictionary

May need tweaking to allow better matching for DNA strand names.
"""
import re

def read_fasta(fasta_file):
    with open(fasta_file, 'r') as f:
        fasta_content = f.read()

    raw_fasta = fasta_content.replace('\n', '')
    
    dna_strands = dict(
        re.findall('>([A-Za-z]+_[\d]+)([ACGT]+)', raw_fasta)
    )

    return dna_strands