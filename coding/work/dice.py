import random
import time

def rolling():
  print 'rolling the dice...'
  time.sleep(1)
  print '.'
  time.sleep(1)
  print '.'
  time.sleep(1)
  print '.'
  print(random.randint(1,6))

rolling()
