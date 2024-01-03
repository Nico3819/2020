x = input ("enter a number:  ")

w = x / 2
y = x - 1 

while x > y:
  x = x * y
  q = x * y
  y = y - 1 
  if y == 1:
   q = q / w
   print q
   break
