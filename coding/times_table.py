x = raw_input ("enter a sentence:  ")
  
q = 0  
flag = 'false'
  
for y in x:
  if y == ' ':
    flag = 'true'

  if ((flag == 'true') and ((y == 'a') or (y == 'e') or (y == 'i') or (y == 'o') or (y == 'u'))):
    print y
    q = q + 1
    flag = 'false'

print q
