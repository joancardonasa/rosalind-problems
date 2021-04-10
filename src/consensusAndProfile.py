# -*- coding: utf-8 -*-
"""
Created on Sun Nov 29 15:25:24 2020

@author: Jonordona
@ID: CONS
@Title: Consensus and Profile
@Explanation: With several homologous strands of DNA (sharing same ancestor),
we can analyze them simultaneously by finding the average case strand to 
represent the most likely common ancestor of the given strands.

The profile matrix of several DNA strings of equal length tells us the
number of times that each base, each in a different row i, appears 
in the j-th position of the matrix.

The result is a 4 x n matrix.

A consensus string is an n-length string formed by selecting the most 
common symbol base at each j-th position. There may be more than one
consensus string per collection of DNA strands.
"""
import numpy as np
from fasta_reader import read_fasta

def consensus_profile(fasta_file, format_print = False):
    dna_dict = read_fasta(fasta_file)

    dna_strands = list(dna_dict.values())

    base_position = {
        0: 'A',
        1: 'C',
        2: 'G',
        3: 'T'
    }

    profile_dict = {
        'A': [0] * len(dna_strands[0]),
        'C': [0] * len(dna_strands[0]),
        'G': [0] * len(dna_strands[0]),
        'T': [0] * len(dna_strands[0])
    }

    for strand in dna_strands:
        for position, nucleotide in enumerate(strand):
            profile_dict[nucleotide][position] += 1

    profile_matrix = np.matrix(list(profile_dict.values()))

    consensus = ''
    for col in profile_matrix.T:
        # Get the position of most frequent symbol for each column (j)
        position = np.argmax(col)
        consensus += base_position[position]

    if format_print:
        print(consensus)
        for idx, elem in enumerate(profile_dict.values()): 
            print(base_position[idx] + 
                  ': ' +
                  ' '.join([str(int) for int in elem]))
        
    
    return profile_dict, consensus
        
        