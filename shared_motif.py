'''
Finding a Shared Motif
https://rosalind.info/problems/lcsm/
'''
import math

def list_of_nucleotides(sample):
    '''
    This function takes in the sample data in fafsta format and converts it into a list of 
    just the nucleotide sequences
    '''
    split_sample = sample.split('\n')
    new_list = []
    for i in split_sample:
        if i[0] == '>':
            pass
        else:
            new_list.append(i)
    return(new_list)


def substring_in_a_dna_str(substring, dna_str):
    '''
    This function takes in a substring along with a singular DNA string to check whether the 
    substring is present in the DNA sequence 
    '''
    length_of_dna = len(dna_str)
    starting_letter = 0
    ending_letter = 1
    while True:
        if ending_letter > length_of_dna:
            break
        elif dna_str[starting_letter:ending_letter] == substring:
            break
        elif dna_str[starting_letter:ending_letter] == substring[0:ending_letter-starting_letter]:
            ending_letter = ending_letter + 1
        else:
            starting_letter = starting_letter + 1
            ending_letter = starting_letter + 1

    if ending_letter > length_of_dna :
        return(False)
    else:
        return(True)

def substring_in_all_dna_strs(substring,list_of_dna_strings):
    '''
    This function will check whether a substring is present in all of the dna strings in 
    a given list of them
    '''
    length_of_dna_list = len(list_of_dna_strings)
    counter = 0
    while True:
        if length_of_dna_list == counter:
            return(True)
        elif substring_in_a_dna_str(substring,list_of_dna_strings[counter]) == True:
            counter = counter + 1
        else:
            return(False)


def list_of_common_motifs(dna_strings_list):
    '''
    Gives a list of all of the common motifs greater than a length of 1 letter found
    '''
    list_of_motifs = []
    dna_strings = list_of_nucleotides(dna_strings_list)
    starting_substring_letter = 0
    ending_substring_letter = 2
    first_item_in_dna_list = dna_strings[0]
    while True:
        substring = first_item_in_dna_list[starting_substring_letter : ending_substring_letter]
        if ending_substring_letter > len(dna_strings[0]) + 2:
            list_of_motifs.append(substring)
            break
        elif substring_in_all_dna_strs(substring,dna_strings) == True:
            ending_substring_letter = ending_substring_letter + 1
        else:
            list_of_motifs.append(substring[:-1])
            starting_substring_letter = starting_substring_letter + 1
            ending_substring_letter = starting_substring_letter + 2
    return(list_of_motifs)


        
def shared_motif(fafsta_dna_strings):
    '''
    outputs the largest motif out of the given list 
    '''
    longest_motif = max(list_of_common_motifs(fafsta_dna_strings),key=len)
    return(longest_motif)

sample = '''>Rosalind_1
GATTACTGGAC
>Rosalind_2
TAGACCAACTGACA
>Rosalind_3
ATACACTGAAG'''

print(shared_motif(sample))
    




    
        














