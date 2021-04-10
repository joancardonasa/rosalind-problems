# -*- coding: utf-8 -*-
"""
Created on Wed Dec  2 22:47:22 2020

@author: Jonordona
@ID: GRPH
@Title: Overlap Graphs
@Explanation: In biology it is common to observe graph systems.

How to computationally model a network without needing to render a picture?

We can use an adjancency list, where each row of the list contains the two
node labels corresponding to a unique edge.
"""
from fasta_reader import read_fasta

def overlap_graphs(fasta_file, k, format_print = False):
    dna_strands = read_fasta(fasta_file)
    
    adj_list = []
    for k_s, s in dna_strands.items():
        other_strands = dict(dna_strands)
        other_strands.pop(k_s)
        
        for k_t, t in other_strands.items():
            if (s[-k:] == t[:k]):
                if format_print:
                    print(k_s + ' ' + k_t)
                
                adj_list.append((k_s, k_t))
            
    return adj_list
    