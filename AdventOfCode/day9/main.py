import numpy as np
import time

inputs = open('day9.txt')
inputs = inputs.read().splitlines()
args = []
for i in inputs:
  args.append(int(i))

def getPossible(listOfNum, possible):
  trueFalse = False
  listOfNum = listOfNum[(len(listOfNum)-25):]
  for i in listOfNum:
    for z in listOfNum:
      if i + z == possible:
        trueFalse = True
  return trueFalse
def getCorrupt():
  index = 25
  while True:
    if getPossible(args[:index], args[index]) == False:
      return args[index], args[:index]
      break
    else:
      index += 1

def getRange(listOfNum, corrupt, toNumber):
  listOfNum = listOfNum[(len(listOfNum)-toNumber):]
  for rangelen in range(2, toNumber):
    freshindex = 0
    while freshindex+rangelen < toNumber:
      summed = np.sum(listOfNum[freshindex: freshindex + rangelen])
      if summed == corrupt:
        return sorted(listOfNum[freshindex: freshindex + rangelen])[0] + sorted(listOfNum[freshindex: freshindex + rangelen])[-1]
      else:
        freshindex += 1


corrupt, corruptlist = getCorrupt()
print(corrupt)
print(getRange(corruptlist, corrupt, len(corruptlist)))

  
  
