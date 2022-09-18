import math

def probability_of_dominant_allele(organism_1, organism_2):
  '''Given 2 organisms, calculates the chance of a dominant trait being present
  '''
  if (organism_1 == 'Bb' and organism_2 == 'bb') or organism_1 == 'bb' and organism_2 == 'Bb':
    return 0.5
  elif (organism_1 == 'BB' and organism_2 == 'bb') or (organism_1 == 'bb' and organism_2 == 'BB'):
    return 1
  elif (organism_1 == 'BB' and organism_2 == 'Bb') or (organism_1 == 'Bb' and organism_2 == 'BB'):
    return 1
  elif (organism_1 == 'bb' and organism_2 == 'bb'):
    return 0
  elif (organism_1 == 'BB' and organism_2 == 'BB'):
    return 1
  else:
    return 0.75

def fn(ks,ms,ns):
  '''
  This function finds all of the probabilities of each possible combination of picking 2 
  organisms
  '''
  k = ['BB'] * ks
  m = ['Bb'] * ms
  n = ['bb'] * ns
  list_of_organsims = k + m + n
  head = list_of_organsims[0]
  list_of_organsims = list_of_organsims[1:]
  probabilities = []
  while len(list_of_organsims) >= 1:
    for i in list_of_organsims:
      probabilities.append(probability_of_dominant_allele (head, i))
    head = list_of_organsims[0]
    list_of_organsims = list_of_organsims[1:]
  summ = sum(probabilities)
  length = len(probabilities)
  return(summ/length)


