args = open("input.txt", 'r')
inputs = args.read()
inputs = inputs.split('\n')

saved = []
for i in inputs:
  for z in inputs:
    if int(i) + int(z) == 2020:
      saved.append((int(i), int(z)))

for i in saved:
  print(i[0] * i[1])

print('-------------------')

saved2 = []
for i in inputs:
  for z in inputs:
    for m in inputs:
      if int(i) + int(z) + int(m) == 2020:
        saved2.append((int(i), int(z), int(m)))

for i in saved2:
  print(i[0] * i[1] * i[2])
