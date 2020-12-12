args = open('day12.txt', 'r')
args = args.read().splitlines()

waypoint = (10, 1)
direction = 90
east = 0
north = 0
for i in args:
  command = i[0]
  amount = int(i[1:])
  eastVal = waypoint[0]
  northVal = waypoint[1]
  if command == 'N':
    waypoint = (eastVal, northVal + amount)
  elif command == 'S':
    waypoint = (eastVal, northVal - amount)
  elif command == 'E':
    waypoint = (eastVal + amount, northVal)
  elif command == 'W':
    waypoint = (eastVal - amount, northVal)
  elif command == 'L':
    if amount == 270:
      waypoint = (northVal, -eastVal)
    if amount == 180:
      waypoint = (-eastVal, -northVal)
    if amount == 90:
      waypoint = (-northVal, eastVal)
  elif command == 'R':
    if amount == 90:
      waypoint = (northVal, -eastVal)
    if amount == 180:
      waypoint = (-eastVal, -northVal)
    if amount == 270:
      waypoint = (-northVal, eastVal)
  elif command == 'F':
    east += (amount * waypoint[0])
    north += (amount * waypoint[1])
  print(waypoint)
print(abs(east) + abs(north))

# eastAmt = 0
# northAmt = 0
# direction = 'east'

# for i in args:
#   command = i[0]
#   amount = float(i[1:])
#   if command == 'E':
#     eastAmt += amount
#   elif command == 'W':
#     eastAmt -= amount
#   elif command == 'N':
#     northAmt += amount
#   elif command == 'S':
#     northAmt -= amount
#   elif command == 'R':
#     if direction == 'east':
#       if amount == 90:
#         direction = 'south'
#       if amount == 180:
#         direction = 'west'
#       if amount == 270:
#         direction = 'north'
#     elif direction == 'west':
#       if amount == 90:
#         direction = 'north'
#       if amount == 180:
#         direction = 'east'
#       if amount == 270:
#         direction = 'south'
#     elif direction == 'south':
#       if amount == 90:
#         direction = 'west'
#       if amount == 180:
#         direction = 'north'
#       if amount == 270:
#         direction = 'east'
#     elif direction == 'north':
#       if amount == 90:
#         direction = 'east'
#       if amount == 180:
#         direction = 'south'
#       if amount == 270:
#         direction = 'west'

#   elif command == 'L':
#     if direction == 'west':
#       if amount == 90:
#         direction = 'south'
#       if amount == 180:
#         direction = 'east'
#       if amount == 270:
#         direction = 'north'

#     elif direction == 'east':
#       if amount == 90:
#         direction = 'north'
#       if amount == 180:
#         direction = 'west'
#       if amount == 270:
#         direction = 'south'

#     elif direction == 'north':
#       if amount == 90:
#         direction = 'west'
#       if amount == 180:
#         direction = 'south'
#       if amount == 270:
#         direction = 'east'
#     elif direction == 'south':
#       if amount == 90:
#         direction = 'east'
#       if amount == 180:
#         direction = 'north'
#       if amount == 270:
#         direction = 'west'

#   elif command == 'F':
#     if direction == 'east':
#       eastAmt += amount
#     elif direction == 'west':
#       eastAmt -= amount
#     elif direction == 'north':
#       northAmt += amount
#     elif direction == 'south':
#       northAmt -= amount

# print(abs(eastAmt) + abs(northAmt))