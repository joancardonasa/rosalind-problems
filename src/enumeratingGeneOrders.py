# -*- coding: utf-8 -*-
"""
Created on Fri Jan  1 17:36:45 2021

@author: Jonordona
@ID: PERM
@Title: Enumerating Gene Orders
@Explanation: There is a difference between point mutations and 
genome rearrangements. The former lack the power to create and differentiate 
entire species, while the latter are larger mutations that move around
large blocks of DNA.

These are usually fatal and thus can very rarely influence the genome of an 
entire species.

Two closely related species will have very similar genomes. To simplify the
comparison between them, we must identify similar intervals called synteny
blocks. Rearrangements have moved these blocks around the genome of the similar
species.

Synteny blocks are not strictly identical, but we may consider them equivalent.
We can label these blocks using integers, in order to compare them among species.

We'll just use itertools since there is really no point in reinventing the wheel.
Anything I might come up with will surely be slower and less efficient.

The main takeaway is that we can use integers to identify synteny blocks and
compare their location amongst different genomes by using permutations.
"""
import itertools
import os
def all_permutations(n, format_print = False):
    elements = list(range(1, n + 1))
    
    perms = list(itertools.permutations(elements))
    if format_print:
        out_file = 'output/perm_out.txt'
        if os.path.exists(out_file): os.remove(out_file)
        f = open(out_file, 'a')
        
        f.write(str(len(perms)) + '\n')
        [f.write(' '.join(map(str, perm)) + '\n') for perm in perms]

        f.close()
    return True
    
