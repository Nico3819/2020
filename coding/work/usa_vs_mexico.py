import random
import time
print 'Usa vs Mexico'
x = raw_input("Who is going to win?  ")
usa_score = random.randint(1,6)
mexico_score = random.randint(1,6)
time.sleep(3)
print ('Usa %s vs %s Mexico' % (usa_score,mexico_score))


if x == 'mexico' and (usa_score < mexico_score):
  print 'you were right mexico won'
elif x == 'mexico' and (usa_score > mexico_score):
  print 'you were wrong usa won'
elif 'mexico' and (usa_score == mexico_score):
  print 'you were wrong it is a tie'



if x == 'tie' and (usa_score == mexico_score):
  print 'you were right it was a tie'
elif x == 'tie' and (usa_score > mexico_score):
  print 'you were wrong usa won'
elif x == 'tie' and (usa_score < mexico_score):
  print 'you were wrong mexico won'

if x == 'usa' and (usa_score > mexico_score):
  print 'Usa won you were right'
elif x == 'usa' and (usa_score < mexico_score):
  print 'you were wrong mexico won'
elif x == 'usa' and (usa_score == mexico_score):
  print 'you were wrong it is a tie'
