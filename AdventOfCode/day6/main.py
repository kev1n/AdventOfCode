# inputs = open('day6.txt')
# inputs = inputs.read().split('\n\n')

# groups = []
# for i in inputs:
#   i = i.replace('\n', ' ')
#   groups.append(i.split(' '))

# yesanswers = 0
# for i in groups:
#   uniqueletters = ''
#   for subgroups in i:
#     for letter in subgroups:
#       if letter not in uniqueletters:
#         uniqueletters += letter
#   yesanswers += len(uniqueletters)

# print(yesanswers)
  
inputs = open('day6.txt')
inputs = inputs.read().split('\n\n')

groups = []
for i in inputs:
  i = i.replace('\n', ' ')
  groups.append(i.split(' '))

realtimes = 0
yesanswers = 0
for i in groups:
  #Part One
  uniqueletters = ''
  for subgroups in i:
    for letter in subgroups:
      if letter not in uniqueletters:
        uniqueletters += letter
  yesanswers += len(uniqueletters)

  #Part Two
  validletters = ''
  for subgroups in i:
    for letter in subgroups:
      containsall = True
      for subgroups2 in i:
        if letter not in subgroups2:
          containsall = False
      if containsall == True:
        if letter not in validletters:
          realtimes += 1
          validletters += letter
          #print(i, letter)

print(yesanswers)
print(realtimes)