import random

l1 = [[int(random.normalvariate(50,20)) for x in range(random.randint(5,20))] for x in range(10)]

i = 0
for outerlist in l1:
  print(i, end=" ")
  if(i<8):
    print(i, end=" ")
    for element in outerlist:
      print(element, end=" ")
  else:
    for element in range(20):
      try:
        print(outerlist[element], end=" ")
      except IndexError:
        print("0", end=" ")
  print()
  i = i + 1