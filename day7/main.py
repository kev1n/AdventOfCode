inputs = open('day7.txt')
inputs = inputs.read().splitlines()
from pprint import pprint

dicts = {}
for i in inputs:
  i = i.replace('.', '')
  i = i.split(' contain ')
  values = []
  dicts[i[0].replace(' bags', '')] = i[1:][0].split(', ')


#print(dicts)
def getExchanges(bagName):
  available = []
  for key,value in dicts.items():
    if bagName in key:
      available.append(value)
  return available

def bagchecker(key):
  if key != 'other' and key != 'no other bags':
    available = getExchanges(key)
    for bags in available[0]:
      if 'shiny gold' in bags:
        return True
      else:
        bag = bags.split(' ')[1:-1]
        completebag = ''
        for i in bag:
          completebag += (i + ' ')
        if bagchecker(completebag[:-1]) == True:
          return True

bagamount = 0
def bagCounter(key, numBags):
  global bagamount
  available = getExchanges(key)
  if available != []:
    for bags in available[0]:
      if bags != 'no other bags':
        bag = bags.split(' ')
        bagCount = int(bag[0])
        completebag = ''
        for i in bag[1:-1]:
          completebag += (i + ' ')
        totalbag = bagCount * numBags
        print(f"{numBags} of {key} contains {totalbag} bags of {completebag}")
        bagamount += totalbag
        bagCounter(completebag[:-1], totalbag)

counter = 0
for keys in dicts.keys():
  if bagchecker(keys):
    counter += 1

bagCounter('shiny gold', 1)
print(counter)
print(bagamount)





