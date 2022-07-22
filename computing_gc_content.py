'''
Computing GC Content
https://rosalind.info/problems/gc/
'''

import math
def cg_count(s):
  cg_counter = 0
  for i in s:
    if i == "C" or i == "G":
      cg_counter = cg_counter + 1
    else:
      pass
  return   (100 * (cg_counter / len(s)))

def find_id(vvalue, dict):
  for i in dict:
    if dict[i] == vvalue:
      print(i)
    else :
      pass 

dicty =  {}
dicty['a'] = 1
dicty['b'] = 2

def cg_content(ss):
  ss = ss.split(">")
  dict = {}
  for i in ss:
    if i == "":
      pass
    else:
      stripped = i.replace("\n","")
      dict[stripped[:13]] = cg_count(stripped[13:])
  print ( (find_id (max(dict.values()), dict)) , (max(dict.values())))
