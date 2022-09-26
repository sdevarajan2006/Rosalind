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

sample = "TCAATGCATGCGGGTCTATATGCAT"

def restriction_sites(dna):
    restrictions = []
    n = 0
    counter = 4
    while len(dna) > 3:
        if dna[0:counter] == reverse_complement(dna[0:counter]):
            counter = counter + 1
        else:
            if counter == 4:
                n = n + 1
                dna = dna[1:]
            else:
                restrictions.append((n,counter))
                n = n + 1
                counter = 4
                dna = dna[1:]
            
    print(restrictions)
    
restriction_sites(sample)
