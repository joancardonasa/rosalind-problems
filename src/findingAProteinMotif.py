# -*- coding: utf-8 -*-
"""
Created on Tue Dec 15 22:06:07 2020

@author: Jonordona
@ID: MPRT
@Title: Finding a Protein Motif
@Explanation: Proteins perform all practical aspects of the cell.

A protein domain is an interval of aminoacids that can evolve
and function independently. Each domain usually performs a single
function of the protein.

In a domain, an essential component for its function is called
a motif. Protein motifs are generally constant among species.

To find protein motifs, we can use UniProt, a protein repo.

Motifs can be identified in a regex-like fashion:

[XY]: X or Y
{X}: Any aminoacid except X

In this case, we want to find the N-glycosylation motif: N{P}[ST]{P} 
"""
import regex as re
import requests

def find_protein_motif(protein_list_file, format_print = False):
    with open(protein_list_file, 'r') as f:
        protein_list = f.read().splitlines()

    # Protein mapping with its aminoacid sequence
    proteins = {}
    for protein in protein_list:
        ftext = requests.get(f'''
            https://www.uniprot.org/uniprot/{protein}.fasta''').text
        ftitle = re.search('>.*', ftext).group()
        proteins[protein] = ftext.replace(ftitle, '').replace('\n', '')

    n_gly_motif = re.compile('N[^P][ST][^P]')
    n_gly_locations = {}
    for protein, am_ac_seq in proteins.items():
        # +1 to make it 1-based index
        motif_locs = [idx.start() + 1 for idx 
                      in n_gly_motif.finditer(am_ac_seq, overlapped = True)]

        n_gly_locations[protein] = motif_locs
        if format_print and len(motif_locs) > 0:
            print(protein)
            print(' '.join(map(str, motif_locs)))

    return n_gly_locations
