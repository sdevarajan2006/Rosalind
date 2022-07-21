'''
Transcribing DNA into RNA
https://rosalind.info/problems/rna/
'''
def dna_to_rna(dna_str):
    '''
    Transcribes DNA into RNA
    '''
    rna_str = ''
    for i in dna_str:
        if i == "G" or i == 'A' or i == 'C':
            rna_str = rna_str + i
        else:
            rna_str = rna_str + 'U'
    return(rna_str)
    
if __name__ == '__main__':
    sample = "GATGGAACTTGACTACGTAAATT"
    rna_str = dna_to_rna(sample)
    print(rna_str)