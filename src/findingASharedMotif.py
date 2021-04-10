# -*- coding: utf-8 -*-
"""
Created on Tue Dec  8 11:35:35 2020

@author: Jonordona
@ID: LCSM
@Title: Finding a Shared Motif
@Explanation: The goal is to find the longest common motif
in a collection of DNA strings
"""
from fasta_reader import read_fasta

def find_longest_shared_motif(fasta_file, format_print = False):
    dna_strands = read_fasta(fasta_file)
    
    # Get shortest strand in collection
    # Get all substrings starting from longest to shortest

    # For each one try to find them in other strands
    #   If it is not found in one, stop loop and go to next string

    dna_strings = list(dna_strands.values())
    shortest_string = min(dna_strings, key = len)

    dna_strings.remove(shortest_string)

    # Takes about 3m, could improve by checking each substring wo combs list
    for n_chars in range(len(shortest_string), 1, -1):
        n_char_combs = ordered_combinations(shortest_string, n_chars)

        for substring in n_char_combs:
            pattern_found = check_for_pattern(dna_strings, substring) 
            if pattern_found:
                return substring

    return 'No shared motif found'

def ordered_combinations(s, k):
    '''
    Returns all k-length substrings of s
    '''
    combs = [s[i:j]
        for i in range(0, len(s) + 1) 
        for j in range(0, len(s) + 1) 
        if len(s[i:j]) == k]

    return combs

def check_for_pattern(dna_strands, pattern):
    '''
    Returns True if pattern is found in all strands
    '''
    for strand in dna_strands:
        if pattern not in strand:
            return False

    return True


    