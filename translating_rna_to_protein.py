'''
Translating RNA into Protein
https://rosalind.info/problems/prot/
'''

#Codon Table 
cstr = """UUU F      CUU L      AUU I      GUU V
UUC F      CUC L      AUC I      GUC V
UUA L      CUA L      AUA I      GUA V
UUG L      CUG L      AUG M      GUG V
UCU S      CCU P      ACU T      GCU A
UCC S      CCC P      ACC T      GCC A
UCA S      CCA P      ACA T      GCA A
UCG S      CCG P      ACG T      GCG A
UAU Y      CAU H      AAU N      GAU D
UAC Y      CAC H      AAC N      GAC D
UAA Stop   CAA Q      AAA K      GAA E
UAG Stop   CAG Q      AAG K      GAG E
UGU C      CGU R      AGU S      GGU G
UGC C      CGC R      AGC S      GGC G
UGA Stop   CGA R      AGA R      GGA G
UGG W      CGG R      AGG R      GGG G """
clis = cstr.split("\n")
cDict = {}
'Change the codon table from a string to a dictionary'
[cDict.update(dict(list(zip(i.split()[::2], i.split()[1::2])))) for i in clis]




def find_protein(rna_string):
    '''
    This function takes in an rna string of length 3 and finds the matching protein
    '''
    for i in cDict:
        if i == rna_string:
            return(cDict[i])
        else:
            pass

def translate_rna_to_protein(rna_string):
    '''
    This function takes the entire RNA string and converts it into a string of 
    proteins
    '''
    counter = 0
    protein_string = ' '
    while counter < len(rna_string) - 3:
        protein = find_protein(rna_string[counter:counter+3])
        protein_string = protein_string + protein
        counter = counter + 3
    return(protein_string)


if __name__ == '__main__':
    sample = 'AUGGCCAUGGCGCCCAGAACUGAGAUCAAUAGUACCCGUAUUAACGGGUGA'
    ans = translate_rna_to_protein(sample)
    print(ans)



