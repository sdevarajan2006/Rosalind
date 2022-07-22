'''
Counting DNA Nucleotides
https://rosalind.info/problems/dna/
'''
import math

def count_nucleotides(dna_string):
    '''
    This function takes a string of DNA nucleotides and outputs the number of a, c, t, and g
    present in the string
    '''
    a = 0
    c = 0
    g = 0
    t = 0
    for i in dna_string:
        if i == 'A':
            a += 1
        elif i == 'C':
            c += 1
        elif i == 'G':
            g += 1
        elif i == "T":
            t += 1
        else:
            pass
    print(a,c,g,t)
    return(a,c,g,t)
    
if __name__ == '__main__':   
    sample = '''CAATGACATACCACATCCCCTCCGGTAGTGGGCCCAGTAAGC'''
    count_nucleotides(sample)