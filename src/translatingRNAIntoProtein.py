# -*- coding: utf-8 -*-
"""
Created on Sun Nov 29 11:33:20 2020

@author: Jonordona
@ID: PROT
@Title: Translating RNA into protein
@Explanation: While nucleic acids such as DNA and RNA are polymers of nucleotides,
proteins are chains of smaller molecules named amini acids.

The Central Dogma of molecular biology tells us that DNA is transcribed into 
RNA (specifically mRNA), and mature mRNA gets translated in a ribosome into
proteins. 4 RNA bases are translated into a language of 20 amino acids.

There are 20 common amino acids that appear in every species.
"""
import requests
import re
from lxml import html

# First we have to import the RNA codon table and parse it:
rna_codon_html = requests.get('http://rosalind.info/glossary/rna-codon-table/')
tree = html.fromstring(rna_codon_html.content)
raw_table = (tree.xpath('//div[@class="glossary-term"]/pre/text()')[0]).replace('\n', '')

matches = re.findall('([UCAG]{3})\s+(Stop|[A-Z])', raw_table)
rna_codon_table = dict(matches)

def translate_rna_into_protein(mrna_string):
    triplets = re.findall('...', mrna_string)
    
    protein_string = ''.join([rna_codon_table[triplet] for triplet in triplets])
    
    return protein_string.split('Stop')[0]