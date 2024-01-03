
while True:

  x = input ("enter a number: ")
  if x <= 10:
    print ('ones')
  elif x <= 20 and x > 10:
    print ('tens')
  elif x <= 30 and x > 20:
    print ('twenties')
  elif x <= 40 and x > 30:
    print ('thirties')
  elif x <= 50 and x > 40:
    print ('fourties')
  elif x <= 60 and x > 50:
    print ('fifties')
  elif x <= 70 and x > 60:
    print ('sixties')
  elif x <= 80 and x > 70:
    print ('seventies')
  elif x <= 90 and x > 80:
    print ('eighties')
  elif x <= 100 and x > 90:
    print ('nineties')
  else:
    print('the number has to be 0-100')
