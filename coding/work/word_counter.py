x = raw_input ("enter a sentence:  ")

q = 0
flag = 'false'

for y in x:
  #if y == ' ': 
  #  flag = 'true'
    
  if y == ' ':
    flag = 'true'
  if flag == 'true' and y != ' ':
    q = q + 1
    flag = 'false'


if x[0] !=  ' ':
  q = q + 1
  print q
else:
  print q
