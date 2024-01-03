x = float(raw_input ("how many dollars do you have?:  "))
y = raw_input ("which country would you like to go to?:  ")
y = y.lower()

def money(x,y):
  if y == 'europe':
    e = x * 0.89
    print ('euros = %s' % (e))
  elif y == 'mexico':
    p = x * 22.46
    print ('pesos = %s' % (p))
  elif y == 'india':
    r = x * 76.34
    print ('rupees = %s' % (r))
money(x,y)
