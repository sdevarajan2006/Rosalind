'''
Enumerating gene orders
https://rosalind.info/problems/perm/
'''
import math

def permutations_of_three(number_1,number_2,number_3):
    '''
    returns all permutations given 3 numbers 
    '''
    n1 = str(number_1)
    n2 = str(number_2)
    n3 = str(number_3)
    return[(n1 + ' ' + n2 + ' ' + n3),
     (n1 + ' ' + n3 + ' ' + n2), 
     (n2 + ' ' + n1 + ' ' + n3),
    (n2 + ' ' + n3 + ' ' + n1),
    (n3 + ' ' + n2 + ' ' + n1),
    (n3 + ' ' + n1 + ' ' + n2)]

def permutations_of_four(number_1,number_2,number_3,number_4):
    '''
    returns all permutations given 4 numbers 
    '''
    n1 = str(number_1)
    n2 = str(number_2)
    n3 = str(number_3)
    n4 = str(number_4)
    list_of_permutations = []
    for i in permutations_of_three(n2,n3,n4):
        full = n1 + ' ' + i
        list_of_permutations.append(full)
    for i in permutations_of_three(n3,n4,n1):
        full = n2 + ' ' + i
        list_of_permutations.append(full)
    for i in permutations_of_three(n2,n4,n1):
        full = n3 + ' ' + i
        list_of_permutations.append(full)
    for i in permutations_of_three(n2,n3,n1):
        full = n4 + ' ' + i
        list_of_permutations.append(full)
    return(list_of_permutations)

def permutations_of_five(number_1,number_2,number_3,number_4,number_5):
    '''
    returns all permutations given 5 numbers 
    '''
    n1 = str(number_1)
    n2 = str(number_2)
    n3 = str(number_3)
    n4 = str(number_4)
    n5 = str(number_5)
    list_of_permutations = []
    for i in permutations_of_four(n2,n3,n4,n5):
        full = n1 + ' ' + i
        list_of_permutations.append(full)
    for i in permutations_of_four(n3,n4,n5,n1):
        full = n2 + ' ' + i
        list_of_permutations.append(full)
    for i in permutations_of_four(n2,n4,n5,n1):
        full = n3 + ' ' + i
        list_of_permutations.append(full)
    for i in permutations_of_four(n2,n3,n1,n5):
        full = n4 + ' ' + i
        list_of_permutations.append(full)
    for i in permutations_of_four(n2,n3,n1,n4):
        full = n5 + ' ' + i
        list_of_permutations.append(full)
    return(list_of_permutations)

def permutations_of_six(number_1,number_2,number_3,number_4,number_5,number_6):
    '''
    returns all permutations given 6 numbers 
    '''
    n1 = str(number_1)
    n2 = str(number_2)
    n3 = str(number_3)
    n4 = str(number_4)
    n5 = str(number_5)
    n6 = str(number_6)
    list_of_permutations = []
    for i in permutations_of_five(n2,n3,n4,n5,n6):
        full = n1 + ' ' + i
        list_of_permutations.append(full)
    for i in permutations_of_five(n3,n4,n5,n6,n1):
        full = n2 + ' ' + i
        list_of_permutations.append(full)
    for i in permutations_of_five(n4,n5,n6,n1,n2):
        full = n3 + ' ' + i
        list_of_permutations.append(full)
    for i in permutations_of_five(n5,n6,n1,n2,n3):
        full = n4 + ' ' + i
        list_of_permutations.append(full)
    for i in permutations_of_five(n6,n1,n2,n3,n4):
        full = n5 + ' ' + i
        list_of_permutations.append(full)
    for i in permutations_of_five(n1,n2,n3,n4,n5):
        full = n6 + ' ' + i
        list_of_permutations.append(full)
    return(list_of_permutations)

def permutations_of_seven(number_1,number_2,number_3,number_4,number_5,number_6,number_7):
    '''
    returns all permutations given 7 numbers 
    '''
    n1 = str(number_1)
    n2 = str(number_2)
    n3 = str(number_3)
    n4 = str(number_4)
    n5 = str(number_5)
    n6 = str(number_6)
    n7 = str(number_7)
    list_of_permutations = []
    for i in permutations_of_six(n2,n3,n4,n5,n6,n7):
        full = n1 + ' ' + i
        list_of_permutations.append(full)
    for i in permutations_of_six(n3,n4,n5,n6,n7,n1):
        full = n2 + ' ' + i
        list_of_permutations.append(full)
    for i in permutations_of_six(n4,n5,n6,n7,n1,n2):
        full = n3 + i
        list_of_permutations.append(full)
    for i in permutations_of_six(n5,n6,n7,n1,n2,n3):
        full = n4 + ' ' + i
        list_of_permutations.append(full)
    for i in permutations_of_six(n6,n7,n1,n2,n3,n4):
        full = n5 + ' ' + i
        list_of_permutations.append(full)
    for i in permutations_of_six(n7,n1,n2,n3,n4,n5):
        full = n6 + ' ' + i
        list_of_permutations.append(full)
    for i in permutations_of_six(n1,n2,n3,n4,n5,n6):
        full = n7 + ' ' + i
        list_of_permutations.append(full)
    return(list_of_permutations)

def stack(list):
    '''
    Takes a list and turns it into a string separated by new lines
    '''
    ans = ''
    for i in list:
        ans = ans + str(i) + '\n'
    return ans 

def find_permutations(n):
    '''
    Finds the number of permutations and appropriate permutations given a number
    '''
    if n == 3:
        length = len(permutations_of_three(1,2,3))
        stacked = stack(permutations_of_three(1,2,3))
        return(str(length) + '\n' + str(stacked))
    if n == 4:
        length = len(permutations_of_four(1,2,3,4))
        stacked = stack(permutations_of_four(1,2,3,4))
        return(str(length) + '\n' + str(stacked))
    if n == 5:
        length = len(permutations_of_five(1,2,3,4,5))
        stacked = stack(permutations_of_five(1,2,3,4,5))
        return(str(length) + '\n' + str(stacked))
    if n == 6:
        length = len(permutations_of_six(1,2,3,4,5,6))
        stacked = stack(permutations_of_six(1,2,3,4,5,6))
        return(str(length) + '\n' + str(stacked))
    if n == 7:
        length = len(permutations_of_seven(1,2,3,4,5,6,7))
        stacked = stack(permutations_of_seven(1,2,3,4,5,6,7))
        return(str(length) + '\n' + str(stacked))
    else:
        print('number out of range')

if __name__ == '__main__':
    sample = 4
    ans = find_permutations(6)
    print(ans)