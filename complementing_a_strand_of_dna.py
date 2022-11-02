'''
Complementing a strand of DNA
https://rosalind.info/problems/revc/
'''

def reverse_complement(dna_strand):
    '''
    This function reverses a strand of DNA and finds the appropriate DNA to complement it
    '''
    dna_str = dna_strand[::-1]
    complement = ''
    for i in dna_str:
        if i == 'A':
            complement = complement + 'T'
        elif i == 'T':
            complement = complement + 'A'
        elif i == 'G':
            complement = complement + 'C'
        elif i == 'C':
            complement = complement + 'G'
        else:
            pass
    return(complement)

if __name__ == '__main__':
    sample = '''
    GAGTACTG
    '''
    ans = reverse_complement(sample)
    print(ans)

