import random

x = random.randint(1,10)
t = 0
  
while t < 3:
  p_choice = input ("choose a number 1-10:  ")
  if (x == p_choice):
    print 'you win' 
    break
  elif (x > p_choice):
    print 'choose a bigger number'
  elif (x < p_choice):
    print 'choose a smaller number'
  else:
    print ''
  t = t + 1
  if t == 3:
    break    
