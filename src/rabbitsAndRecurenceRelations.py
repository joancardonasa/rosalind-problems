# -*- coding: utf-8 -*-
"""
Created on Sun Nov 15 21:21:48 2020

@author: Jonordona
@ID: FIB
@Title: Rabbits and Recurrence Relations
"""
def rabbit_branching(n, k):
    # G_i = G_(i-1) + k * G_(i-2)
    pairs_in_generation = [0, 1]
    
    total_pairs = 0
    while len(pairs_in_generation) < n + 1:
        # Reason for n + 1:
        # We have to take into account G_0, in which 0 pairs are present
        new_amount = pairs_in_generation[-1] + k * pairs_in_generation[-2]
        pairs_in_generation.append(new_amount)

    total_pairs = pairs_in_generation[-1]
    return total_pairs
