# -*- coding: utf-8 -*-
"""
Created on Sun Jan 10 22:32:16 2021

@author: Jonordona
@ID: LEXF
@Title: Enumerating k-mers Lexicographically
@Explanation:
"""
import itertools as it

def enumer_lex(symbols_str, n_bases, format_print = False):
    symbols = symbols_str.split(' ')
    perms = list(it.product(symbols, repeat = n_bases))
    
    perms_form = sorted([''.join(perm) for perm in perms])
    if format_print:
        [print(perm) for perm in perms_form]
    return perms_form