import sys
x = input ("enter a number")

y = 0
while y < x:
  e = y % 2
  if e == 0:
    sys.stdout.write("*")
  else:
    sys.stdout.write("#")
  y = y + 1

y = 0
print ''
print ''
while y < x:  
  e = y % 2
  if e == 0:
    print "*"
  else:
    print "#"
  y = y + 1
  
