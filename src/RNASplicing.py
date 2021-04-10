# -*- coding: utf-8 -*-
"""
Created on Tue Jan  5 19:17:33 2021

@author: Jonordona
@ID: SPLC
@Title: RNA Splicing
@Explanation: An enzyme called RNA polymerase initiates 
transcription by breaking the bonds joining complementary
bases. After this, it creates a molecule called precursor mRNA
by using one of the single strands of DNA. Moving down on this
template, the RNAP adds a complementary base on each nucleotide,
with the exception of uracil which is added where thymine should go.

After RNAP has created several nucleotides, the first DNA bases 
are bonded again, similrly to a pair of zipper traversing the DNA
helix.

Pre-mRNA is divided into segments called introns and exons.
For protein translation, the introns are not useful, and the
exons are combined to produce the final strand of mRNA.
This cutting and pasting is called splicing, done by a
collection of RNA and proteins called spliceosome.
"""
from transcribingDNAIntoRNA import transcribe_dna_to_rna
from translatingRNAIntoProtein import translate_rna_into_protein
from fasta_reader import read_fasta

def rna_splice(fasta_file):
    dna_strands = iter(read_fasta(fasta_file).values())

    # The first value is DNA, the rest are introns
    dna_strand = next(dna_strands)
    introns = list(dna_strands)

    for intron in introns:
        dna_strand = dna_strand.replace(intron, '')

    rna = transcribe_dna_to_rna(dna_strand)
    prot = translate_rna_into_protein(rna)


    print(prot)
    return prot