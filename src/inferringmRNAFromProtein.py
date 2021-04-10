# -*- coding: utf-8 -*-
"""
Created on Sun Dec 20 20:57:00 2020

@author: Jonordona
@ID: MRNA
@Title: Inferring mRNA From Protein
@Explanation: From a protein string of amino acids, we would like to get the
total number of possibilities of mRNA it could be.

Since each amino acid could correspond to several mRNA codons (3-mers),
we have to cound these and multiply them in order to get the total number of 
possibilities. We also need to take into account the 3 stop codons.

The modulo stuff is just to get the last 6 digits of the very large number that
this multiplication returns.
"""
import pandas as pd

def infer_mrna_from_prot(prot_string=None):
	rna_codon = pd.read_csv('lookup/rna_codon.csv', 
                           index_col='codon', 
                           sep = '|').to_dict()['amino_acid']

	# Build frequency table for each amino acid
	freq_dict = {}
	for k, v in rna_codon.items():
		if v in freq_dict:
			freq_dict[v] += 1
		else:
			freq_dict[v] = 1

	# Get frequency for each amino acid to multiply possibilities
	possib = 1
	for am_acid in prot_string:
		possib *= freq_dict[am_acid]

	# We have to take into account the 3 stop codons
	stop_codons = 3
	possib *= stop_codons
	return possib % 1000000