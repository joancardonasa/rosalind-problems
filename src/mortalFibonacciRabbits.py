# -*- coding: utf-8 -*-
"""
Created on Tue Dec  1 21:25:11 2020

@author: Jonordona
@ID: FIBD
@Title: Mortal Fibonacci Rabbits
@Explanation: If every adult pair of rabbits generates a pair of baby rabbits
on the next month, and all rabbits live for m months, how many rabbit pairs 
will there be after n months?

Solution: Until month m, will be standard Fibonacci. 
    F_n = F_n-1 + F_n-2

From that moment on,
    F_n = F_n-2 + F_n-3 + ... + F_n-m

"""
def mortal_rabbits(n, m):
    generations = [0, 1]
    
    while len(generations) <= n:
        next_gen = 0
        if len(generations) > m:
            for ix in range(-m, -1):    
                next_gen += generations[ix]
        else:
            next_gen = generations[-1] + generations[-2]
        
        generations.append(next_gen)
    
    return generations[-1]
    