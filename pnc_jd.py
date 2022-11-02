import numpy as np

# Read question from downloaded dataset
sample_str = ''.join(open("/Users/jagadish/Downloads/rosalind_cons.txt").readlines())

# Parse the dna strings
dna_string_lis = [ "".join(item.strip().split("\n")[1:]).replace( ' ',"") for item in sample_str.strip().split(">") if item.strip()]

# get DNA string length
N = list(map(len, dna_string_lis))[0]

# Get profile matrix
flis = []
for loc in range(N)[:]:
    slis = []
    for dstr in dna_string_lis:
        slis.append(dstr[loc])
    #
    flis.append( [slis.count(aa) for aa in 'ACTG'])

# create a 4 x N matrix 
dM = np.array(flis).T

# get location of maximum value and convert to list
locs = np.argmax(dM, axis=0).tolist()

# convert int location (0,1,2,3) to ACTG char and join the chars
consensus_string = ''.join(['ACTG'[i] for i in locs])

# Convert profile matrix to string
profile_string = ''
for i, ch in enumerate('ACTG'):
    profile_string += f'{ch}: ' + ' '.join(list(map(str, dM[i,:]))) + "\n"

print(consensus_string)
print(profile_string)