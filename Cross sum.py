def legit(n):
  for c in n:
    if c not in digits:
      return False
  return True

def cross_sum(n):
  s = 0
  for i in n:
    s += int(i)
  return s

digits = "0123456789"
number = input("What number do you want to know\nthe cross sums of? ")
while not legit(number):
  number = input("That is not a valid number! ")
print()
current = cross_sum(number)
loop_count = 0
while len(str(current)) > 0 and loop_count != 2:
  print(f"The cross sum of {number} is {current}")
  number = current
  current = cross_sum(str(current))
  if len(str(current)) == 1:
    loop_count += 1
  
