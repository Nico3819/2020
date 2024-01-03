y=0
while True:
  x=0  
  california = raw_input ("What is the capital of California:  ") 
  if california == ('sacramento'):
    x=x+1  
    print ('correct')
  else:
    print ('incorrect')
    y=y+1
  nevada = raw_input ("What is the capital of Nevada:  ")
  if nevada == ('carson city'):
    x=x+1
    print ('correct')
  else:
    y=y+1
    print ('incorrect')
  oregon = raw_input ("What is the capital of Oregon:  ")
  if oregon == ('salem'):
    x=x+1
    print ('correct')
    print x
  else:
    y=y+1
    print ('incorrect')
    print x
  if x == 3:
    break
  elif y == 12:
    break
  print ('try = %s' % (y))
