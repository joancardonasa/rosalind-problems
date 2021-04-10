# -*- coding: utf-8 -*-
"""
Created on Mon Nov 16 19:59:32 2020

@author: Jonordona
@ID: GC
@Title: Computing GC Content
@Explanation: Same species share a vast percentage of their DNA.
The GC-content measures the percentage of the bases in a string of DNA that
are either cytosine or guanine.
The GC-content of most eukaryotic genomes is around 50%, while prokaryotes
have a higher GC-content than 50%.

DNA strings are labeled when consolidated into a db. The FASTA format is used.
>Rosalind_{4-digit code}
"""
import re
def compute_gc_content(fasta_file):
    with open(fasta_file, 'r') as f:
        fasta_content = f.read()

    raw_fasta = fasta_content.replace('\n', '')
    
    dna_strands = {}
    for elements in re.finditer('>([A-Za-z]+_\d{4})([ACGT]+)', raw_fasta):
        fas_id = elements.group(1)
        dna_string = elements.group(2)

        cg_base_amount = len(re.findall('[CG]', dna_string))
        cg_content = 100 * cg_base_amount / len(dna_string)
        
        dna_strands[fas_id] = cg_content
    
    return dna_strands

def get_highest_cg_content(fasta_file):
    all_strands = compute_gc_content(fasta_file)
    
    highest_fas_id = max(all_strands, key = all_strands.get)
    return f'{highest_fas_id}: {all_strands[highest_fas_id]}'
    