# -*- coding: utf-8 -*-
"""
Created on Wed Dec  2 23:15:11 2020

@author: Jonordona
@ID: IEV
@Title: Calculating Expected Offspring
@Explanation: The expected value of a random variable X taking values k
between 1 and n is:

    sum([Pr(X == k) * k for k in range(1,n)])

e.g. for a fair die:
    
    sum([(1/6) * k for k in range(1,7)]) = 3.5
    
If all outcomes are equally spaced in the distribution, it is a uniform
random variable.

Given six integers < 20k are the number of couples in a population possessing
each genotype pairing for a given factor:
    
    1. AA-AA
    2. AA-Aa
    3. AA-aa
    4. Aa-Aa
    5. Aa-aa
    6. aa-aa

We want to know the expected number of offspring displaying the dominant 
phenotype in the next generation, knowing that each couple has two offspring.
"""
def expected_offspring(n_couples_in_gentype, n_offspring):
    
    # Calculated with Punnet Square
    dom_prob_by_pair = {
        1: 1,
        2: 1,
        3: 1,
        4: 0.75,
        5: 0.5,
        6: 0
    }

    total = 0
    for idx, n_couples in enumerate(n_couples_in_gentype):
        total += n_couples * n_offspring * dom_prob_by_pair[idx + 1]
    
    return total