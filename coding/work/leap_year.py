while True:
  year = input ("enter a year:  ")
  if year == exit:
    break
  y = year % 4
  if y == 0:
    print 'That is a leap year'
  else:
    print 'That is not a leap year'
  if year > 3020 or year < 1020:
    print 'invalid year'
  else:
    print ''
