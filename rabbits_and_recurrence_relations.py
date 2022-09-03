'''
Rabbits and Recurrence Relations
https://rosalind.info/problems/fib/
'''

import math


def number_of_offspring(n,k):
    '''
    This function takes in n months with k offspring per month, and produces the total number of rabbits
    that will be present per month
    This module was difficult for me to understand, but once I found the pattern the code was much easier to figure out
    '''
    number_of_months = n
    list_of_monthly_offspring = []
    while number_of_months > 0:
        if number_of_months == n or number_of_months == n - 1:
            list_of_monthly_offspring.append(1)
            number_of_months = number_of_months - 1
        else: 
            new_offspring = (list_of_monthly_offspring[(len(list_of_monthly_offspring) - 2)] * k) + (list_of_monthly_offspring[(len(list_of_monthly_offspring) - 1)])
            list_of_monthly_offspring.append(new_offspring)
            number_of_months = number_of_months - 1
    print(list_of_monthly_offspring[-1])

number_of_offspring(35,5)