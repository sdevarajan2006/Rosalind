'''
Consensus and Profile
https://rosalind.info/problems/cons/'''

import math
def list_to_string(mylist):
  '''
  makes a list of numbers a string
  '''
  list = ''
  for i in mylist:
     list = list + ' ' + str(i)
  return(list)

def profiler(fafsta,letter):
  '''
  given a collection of DNA string and either A,C,T, or G, an apt profile is created
  '''
  l = fafsta.split("\n")[1::2]
  str_length = len(l[1])
  counter = 0
  la = []
  while counter < str_length:
    number = 0
    for i in l:
      if i[counter] == letter:
        number = number + 1
      else:
        number = number
    la.append(number)
    counter = counter + 1
  return la


def finalprofile(fafsta):
  '''
  given a collection of DNA strings, a profile is producted for A, C, T and G
  '''
  return("A:" + list_to_string(profiler(fafsta,'A')) + '\n' + 'C:' + list_to_string(profiler(fafsta,"C")) + '\n' + 'G:'+ list_to_string(profiler(fafsta,'G')) + '\n' + 'T:' + list_to_string(profiler(fafsta,'T')))


def raw(profile):
  '''
  converts the profile into a list of numbers that can be used to make a consensus
  '''
  raw = profile.split('\n')
  index = 0
  for i in raw:
    raw[index] = i[3:]
    index += 1
  return(raw)

def consensus(list):
  '''program that will make a consensus given a list of numbers
  '''
  num = 0
  mystr = ''
  while num < len(list[0]):
    d = {}
    d["A"] = int(list[0][num])
    d["C"] = int(list[1][num])
    d["G"] = int(list[2][num])
    d["T"] = int(list[3][num])
    mystr = mystr + sorted(d.items(), key=lambda x: x[1])[::-1][0][0]
    num = num + 2
  print(mystr)
  return(mystr)

def profile_and_consensus(fafsta):
  '''
  uses all of the helper functions to create a final profile and consensus given a collection of DNA string
   '''
  print (consensus(raw(finalprofile (fafsta))) + '\n' + finalprofile(fafsta))

if __name__ == '__main__':   

  sample = """>Rosalind_1
  ATCCAGCT
  >Rosalind_2
  GGGCAACT
  >Rosalind_3
  ATGGATCT
  >Rosalind_4
  AAGCAACC
  >Rosalind_5
  TTGGAACT
  >Rosalind_6
  ATGCCATT
  >Rosalind_7
  ATGGCACT"""

  profile_and_consensus(sample)