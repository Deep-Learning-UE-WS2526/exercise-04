import random

l1 = [[int(random.normalvariate(50,20)) for x in range(random.randint(5,20))] for x in range(10)]

i = 0
for outerlist in l1:
  print(i, end=" ")

  if i == 8 or i == 9:
    for col in range(20):
      try:
        element = outerlist[col]
      except IndexError:
        element = 0
      print(element, end=" ")
  else:
    for element in outerlist:
      print(element, end=" ")

  print()
  i = i + 1
