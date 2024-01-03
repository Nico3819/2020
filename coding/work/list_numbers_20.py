
def number_increase():
  x =input ("enter a number")
  print x
  x=x+1
  return x

x=number_increase()
if x >= 20:
  for p in range (1,21):
    print p
else:
  for y in range (1,x):
    print y
