text = """A   71.03711
C   103.00919
D   115.02694
E   129.04259
F   147.06841
G   57.02146
H   137.05891
I   113.08406
K   128.09496
L   113.08406
M   131.04049
N   114.04293
P   97.05276
Q   128.05858
R   156.10111
S   87.03203
T   101.04768
V   99.06841
W   186.07931
Y   163.06333"""
d = {}
#This code reads each line of the string, splits it into letter and number using the split() method, 
# and adds it to the dictionary using the letter as the key and the number as the value.
for line in text.split('\n'):
    letter, number = line.split()
    d[letter] = float(number)

def calculating_protein_mass(protein_string):
    '''
    Given a protein string, this function uses the dictionary to find the total mass
    of the protein
    '''
    mass_sum = 0.0
    for i in protein_string:
        mass_sum += (d[i])
    return(round(mass_sum, 3))

if __name__ == '__main__':
    sample = 'SKADYEK'
    print(calculating_protein_mass(sample))

n = 10E4