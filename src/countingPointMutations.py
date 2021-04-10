# -*- coding: utf-8 -*-
"""
Created on Wed Nov 18 22:36:46 2020

@author: Jonordona
@ID: HAMM
@Title: Counting point mutations
@Explanation: A point mutation replaces one base with another
at a single nucleotide. This also modifies the complementary base.

Two DNA strands from different same-species genomes are homologous
if they share a recent ancestor.

Counting the number of bases at which they differ gives us the number
of minimum point mutations that have occurred between two strands.

The Hamming distance between two strings outputs the number of symbols that
differ between them.
"""
def count_point_mutations(s, t):
    # s and t must be same lengths
    h_dist = 0
    for idx, base in enumerate(s):
        h_dist += base != t[idx]

    return h_dist