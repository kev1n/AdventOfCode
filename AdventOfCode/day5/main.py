import math

args = open('day5.txt', 'r')
inputs = args.read().splitlines()

highestId = 0
allId = []
for part in inputs:
  row = 0
  column = 0
  rowrange = (0, 127)
  columnrange = (0, 7)
  for character in part:
    rowmidpoint = (rowrange[0] + rowrange[1]) / 2
    if character == 'B':
      rowmidpoint = math.ceil(rowmidpoint)
      rowrange = (rowmidpoint, rowrange[1])

    elif character == 'F':
      rowmidpoint = math.floor(rowmidpoint)
      rowrange = (rowrange[0], rowmidpoint)
  
  if part[6] == 'B':
    row = rowrange[1]
  else:
    row = rowrange[0]

  for character in part[7:]:
    columnmid = (columnrange[0] + columnrange[1]) / 2
    if character == 'R':
      columnmid = math.ceil(columnmid)
      columnrange = (columnmid, columnrange[1])
    elif character == 'L':
      rowmidpoint = math.floor(rowmidpoint)
      columnrange = (columnrange[0], columnmid)
  
  if part[-1] == 'R':
    column = columnrange[1]
  else:
    column = columnrange[0]
  
  ID = (row * 8) + column
  if ID > highestId:
    highestId = ID
  allId.append(ID)


allId = sorted(allId)
#print(highestId)
index1 = 0
index2 = 1
while index2 < len(allId):
    if allId[index1] + 2 == allId[index2]:
        print(allId[index1],allId[index2])
    index1 +=1
    index2 +=1

