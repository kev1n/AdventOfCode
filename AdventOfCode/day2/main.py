inputs = open('day2.txt', 'r')
args = inputs.read().splitlines()
valid = 0
for i in args:
  everything = i.split(' ')
  ranges = everything[0]
  ranges = ranges.split('-')

  letter = everything[1][0]
  string = everything[2]
  
  occurances = string.count(letter)
  if int(ranges[0]) <= occurances <= int(ranges[1]):
    valid += 1

print(valid)

valid2 = 0
for i in args:
  everything = i.split(' ')
  ranges = everything[0]
  ranges = ranges.split('-')

  letter = everything[1][0]
  string = everything[2]

  if (string[int(ranges[0])-1] == letter and string[int(ranges[1])-1] != letter) or (string[int(ranges[0])-1] != letter and string[int(ranges[1])-1] == letter):
    valid2 += 1

print(valid2)