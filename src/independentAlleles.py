# -*- coding: utf-8 -*-
"""
Created on Sun Dec 13 22:26:44 2020

@author: Jonordona
@ID: LIA
@Title: Independent Alleles
@Explanation: Given a parent of genotype AaBb and another parent AaBb, if
each generation creates two members who also pair up with an AaBb:

We want to compute the probability that at least N members of the k iteration 
are also of the type AaBb.

We assume Mendel's second law of Independent Assortment.

Solution: 
Since each member has a parent of type AaBb, they have a 25% chance to also be 
AaBb, and a 75% to not be of this genotype.

The problem can be modeled using a Binomial Distribution, in which we want
to see the probability of N successes in the k-th iteration, where k will have
2^k trials.
"""
from scipy.stats import binom

def independent_alleles(k, n):
    n_trials = 2 ** k

    pmfs = [binom.pmf(i, n_trials, 0.25) for i in range(n, n_trials + 1)]

    return sum(pmfs)