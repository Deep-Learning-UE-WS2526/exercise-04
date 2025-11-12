import random

l1 = [[int(random.normalvariate(50,20)) for x in range(random.randint(5,20))] for x in range(10)]

i = 0
for outerlist in l1:
  print(i, end=" ")
  for element in outerlist:
    print(element, end=" ")
  print()
  i = i + 1

print()
# Step 4
i = 0
for outerlist in l1:
    print(i, end=" ")

    # Lines 8 and 9
    for n in range(20):
        try:
            print(outerlist[n], end=" ")
        except:
            print(0, end=" ")
    
    print()
    i = i + 1