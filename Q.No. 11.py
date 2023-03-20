# Module 2 Q.No. 11
# To check whether a given number can be expressed as a sum of three squares

m = int(input("Enter the number to check: "))
sq_list = [x**2 for x in range(m)]
count = 0

for i in sq_list:
  for j in sq_list:
    for k in sq_list:
      if i + j + k == m:
        count = count + 1

if count >= 1:
  print("Can be expressed")
else:
  print("Can't be expressed")
