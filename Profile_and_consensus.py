import math
x = [0,2,4,34,34,53]
def ls(s):
  counter = 0
  for i in s:
    s[counter] = str(i)
    counter = counter + 1
  return s
def lts(s): 
    
    # initialize an empty string
    str1 = " " 
    
    # return string  
    print(str1.join(s))


def list_to_string(l):
  list = ''
  for i in l:
     list = list + ' ' + str(i)
  return(list)

sample=""">Rosalind_1
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


def profiler(f,letter):
  l = f.split("\n")[1::2]
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


def fprofile(f):
  return("A:" + list_to_string(profiler(f,'A')) + '\n' + 'C:' + list_to_string(profiler(f,"C")) + '\n' + 'G:'+ list_to_string(profiler(f,'G')) + '\n' + 'T:' + list_to_string(profiler(f,'T')))

y = fprofile(sample)

# Makes the profile into something usable to make a consensus
def raw(p):
  raw = p.split('\n')
  index = 0
  for i in raw:
    raw[index] = i[3:]
    index += 1
  return(raw)

z = raw(y)
def consensus(l):
  num = 0
  str = ''
  while num < len(l[0]):
    d = {}
    d["A"] = int(l[0][num])
    d["C"] = int(l[1][num])
    d["G"] = int(l[2][num])
    d["T"] = int(l[3][num])
    str = str + sorted(d.items(), key=lambda x: x[1])[::-1][0][0]
    num = num + 2
  return(str)

consensus(z)