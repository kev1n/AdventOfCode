input = open('day3.txt', 'r')
data = input.read().splitlines()

newdata = []
for z in data:
  newdata.append([z * 10000])

def treemoving(deltaX, deltaY):
  currentX = 0
  currentY = 0
  treehit = 0
  while True:
    try:
      if newdata[currentY][0][currentX] == '#':
        treehit += 1
        currentX += deltaX
        currentY += deltaY
      else:
        currentX += deltaX
        currentY += deltaY
    except:
      break
  return treehit

def probability(args = [(1,1), (3,1), (5, 1), (7, 1), (1,2)]):
  multlist = 1
  for i in args:
    xdelta = i[0]
    ydelta = i[1]
    multlist *= treemoving(xdelta, ydelta)
  return multlist

print(treemoving(3, 1))
print(probability())


    


