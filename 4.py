import random

l1 = [[int(random.normalvariate(50,20)) for x in range(random.randint(5,20))] for x in range(10)]

i = 0
for outerlist in l1:
  print(i, end=" ")
  # pad each row up to 20 elements using exceptions when index is out of range
  for j in range(20):
    try:
      print(outerlist[j], end=" ")
    except Exception:
      # if the list is shorter than the index, print a zero
      print(0, end=" ")
  print()
  i = i + 1