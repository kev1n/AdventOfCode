#Data cleaning
inputs = open('day3.txt', 'r')
inputs = inputs.read().split('\n\n')

cleaned = []
for i in inputs:
  i = i.replace("\n", ' ')
  cleaned.append(i.split(' '))

#Part One
validpassports = []
valid = 0
for i in cleaned:
  if len(i) == 8:
    valid += 1
    validpassports.append(i)
  elif len(i) == 7:
    cidcounted = False
    for z in i:
      if z[:3] == 'cid':
        cidcounted = True
    if cidcounted == False:
      valid += 1
      validpassports.append(i)
        
#print(valid)
#Part two
valid = 0
counter = 0
for i in validpassports:
  validation = True
  for z in i:
    key = z[:3]
    value = z[4:]
    if key == 'byr':
      if not (int(value) >= 1920 and int(value) <= 2002):
        validation = False
    elif key == 'iyr':
      if not (int(value) >= 2010 and int(value) <= 2020):
        validation = False
    elif key == 'eyr':
      if not (int(value) >= 2020 and int(value) <= 2030):
        validation = False
    elif key == 'hgt':
      if value[-2:] == 'cm':
        if not (int(value[:-2]) >= 150 and int(value[:-2]) <= 193):
          validation = False
      elif value[-2:] == 'in':
        if not (int(value[:-2]) >= 59 and int(value[:-2]) <= 76):
          validation = False
      else:
        validation = False
    elif key == 'hcl':
      if value[0] != '#':
        validation = False
      if len(value[1:]) != 6:
        validation = False
      for characters in value [1:]:
        if characters not in 'abcdef0123456789':
          validation = False
    elif key == 'ecl':
      if value not in ['amb','blu','brn','gry','grn','hzl','oth']:
        validation = False
    elif key == 'pid':
      if len(value) != 9:
        validation = False
    if validation == True:
      print(i)
  if validation == True:
    valid += 1

print(valid)
