# -*- coding: utf-8 -*-
"""
Created on Wed Nov 18 22:49:12 2020

@author: Jonordona
@ID: IPRB
@Title: Mendel's First Law
@Explanation: The first law states that every organism has a pair of alleles
for any given factor.

If the alleles are the same, it is homozygous for that factor.
If they differ, then it is heterozygous.

There are dominant and recessive alleles. If the dominant (A) is present in the
organisms' pair of alleles, then the recessive one will be masked. It has to
be homozygous for the recessive allele (aa) to display the trait.

Genotype marks the precise generic makeup while Phenotype is the physical
manifestation of the underlying traits.
"""
def mendel_inherit_prob(k, m, n):
    total_pop = k + m + n

    # Computed drawing Punnet squares:
        # k is dominant homozygous (AA)
        # m is heterozygous (Aa|aA)
        # n is recessive homozygous (aa)
    dominant_probability_by_pair = {
        'kk': 1,
        'km': 1,
        'kn': 1,
        'mk': 1,
        'mm': 0.75,
        'mn': 0.5,
        'nk': 1,
        'nm': 0.5,
        'nn': 0
    }

    genotypes_amount = {
        'k': k,
        'm': m,
        'n': n
    }

    all_possible_combinations = []
    all_possible_probabilities = []

    for type_1, amount_1 in genotypes_amount.items():
        for type_2, amount_2 in genotypes_amount.items():
            new_combination = type_1 + type_2
            all_possible_combinations.append(new_combination)

            if type_1 == type_2:
                prob_draw = (amount_1 * (amount_1 - 1)) / (total_pop * (total_pop - 1))
            else:
                prob_draw = (amount_1 * amount_2) / (total_pop * (total_pop - 1))

            print(f'Combination {new_combination} has a probability of {prob_draw} of being drawn')
            # This probability is independent from its probability of generating dominant phenotype
            # They can therefore be multiplied

            all_possible_probabilities.append(
                prob_draw * dominant_probability_by_pair[new_combination]
            )

    # All possible probabilities are summed (since it is A OR B OR C...)
    return sum(all_possible_probabilities)