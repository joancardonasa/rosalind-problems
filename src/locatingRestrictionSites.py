# -*- coding: utf-8 -*-
"""
Created on Sun Jan 03 09:16:39 2021

@author: Jonordona
@ID: REVP
@Title: Locating Restriction Sites
@Explanation: Bacteriophages are viruses that require a bacterial host to
propagate. They acheive this by understanding the genetic framework the bacteria
uses. Its goal is to insert DNA that will replicate inside the bacteria
and lead to reproduction of the parasitic virus.

The bacteria can hide its cellular functions or use restriction enzymes, which
cut through viral DNA. This restriction enzyme is a homodimer, composed of two
identical substructures.

Each of these structures are separated so it can bind and cut a strand of the
DNA molecule of the phage. Both substructures are pre-prgrammed with the same
target string of between 4 and 12 nucleotides to search for in the phage DNA.

The chance that both strands will be cut is larger if the target is located on
both strands, as closely as possible. Thus, the best the enzyme can do is when
two target copies appear directly across from each other along the phage DNA. 
Most enzyme targets have this form.
"""
from complementingADNAString import reverse_complement
from fasta_reader import read_fasta

def locate_restriction_sites(fasta_file, format_print = False):
    dna_strands = read_fasta(fasta_file)
    dna_strand = next(iter(dna_strands.values()))
    rev_comp = reverse_complement(dna_strand)

    locations = []
    for idx, elem in enumerate(dna_strand):
        # The reverse palindromes can be between 4 and 12 chars
        for n in range(12, 4-1, -1):
            forw = dna_strand[idx:idx+n]
            reve = rev_comp[-(idx+1):-(idx+n+1):-1][::-1]

            if len(forw) == n and forw == reve:
                hit = f'{idx+1} {n}'
                locations.append(hit)
                if format_print: print(hit)
                break

    return locations