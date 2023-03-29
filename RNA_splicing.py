'''
RNA Splicing
https://rosalind.info/problems/splc/
'''
import translating_rna_to_protein
def remove_one_intron(DNA, intron):
    '''
    This function takes in a DNA string and a single intron and removes it from the string
    '''
    starter = 0
    DNA_index = 0
    intron_index = 0
    while (intron_index < len(intron)):
        if (DNA[DNA_index] == intron[intron_index]):
            DNA_index += 1
            intron_index += 1
        else:
            starter += 1
            DNA_index = starter
            intron_index = 0
    return(DNA.replace((DNA[starter:DNA_index]), ''))
 



def RNA_splicing(DNA, introns):
    '''
    This function takes in a string of DNA and multiple introns
    It removes all of the introns, and converts the new string of DNA into a protein string
    '''
    #parsing the DNA and introns
    introns = introns.split('\n')
    for i in introns:
        if (i[0] == '>'):
            introns.remove(i)
    new_dna = DNA.replace('\n','')
    #remove each intron
    for i in introns:
        new_dna = remove_one_intron(new_dna, i)
    #replace the T's with U's to convert the dna string to a protein string
    new_dna = new_dna.replace('T','U')
    return(translating_rna_to_protein.translate_rna_to_protein(new_dna))

if __name__ == '__main__':
    sample_dna = 'ATGGTCTACATAGCTGACAAACAGCACGTAGCAATCGGTCGAATCTCGAGAGGCATATGGTCACATGATCGGTCGAGCGTGTTTCAAAGTTTGCGCCTAG'
    sample_introns = '''>Rosalind_12
ATCGGTCGAA
>Rosalind_15
ATCGGTCGAGCGTGT'''
    ans = RNA_splicing(sample_dna, sample_introns)
    print(ans)


    




