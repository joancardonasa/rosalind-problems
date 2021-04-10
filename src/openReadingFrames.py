# -*- coding: utf-8 -*-
"""
Created on Tue Dec 29 22:47:50 2020

@author: Jonordona
@ID: ORF
@Title: Open Reading Frames
@Explanation: Each strand of DNA can serve as coding strand for RNA transcription.

Thus, every DNA string implies six reading frames, or six ways the string can be
translated into amino acids. Three are for the strand, and three for the reverse
complement.

An open reading frame however, starts from the start codon (ATG, Methionine),
and stops at any of the three possible stop codons. The elements in between
have to be triplets in order for the frame to form a valid chain of amino acids.
"""
import regex as re
import pandas as pd

from fasta_reader import read_fasta
from complementingADNAString import reverse_complement

dna_codon = pd.read_csv('lookup/dna_codon.csv', 
                       index_col='codon', 
                       sep = '|').to_dict()['amino_acid']

def open_read_frames(fasta_file, format_print = False):
    dna_strands = read_fasta(fasta_file)
    dna_strand = next(iter(dna_strands.values()))
    
    # Take into account the reverse complement
    dna_strand_rev = reverse_complement(dna_strand)
    
    stop_codons = [k for k,v in dna_codon.items() if v == 'Stop']
    # (M)ethionine is considered to be the start codon
    start_codon = [k for k,v in dna_codon.items() if v == 'M'][0]

    # Elements between Methionine and stop codons can only be triplets
    pattern = f'(({start_codon})(...)*?)({"|".join(stop_codons)})'
    
    all_cand_prot = []
    for strand in [dna_strand, dna_strand_rev]:
        candidate_dna = [g[0] for g in re.findall(pattern, strand, overlapped = True)]
        if format_print:
            print(candidate_dna)
        candidate_prot = [translate_dna_to_prot(cand) for cand in candidate_dna]
        all_cand_prot = list(set(all_cand_prot + candidate_prot))

    if format_print:
        print('\n'.join(all_cand_prot))
        [print(len(cand)) for cand in all_cand_prot]

    return all_cand_prot

def translate_dna_to_prot(dna):
    triplets = re.findall('...', dna)
    protein_string = ''.join([dna_codon[triplet] for triplet in triplets])

    return protein_string


open_read_frames('data/orf_globin.fas', format_print = True)