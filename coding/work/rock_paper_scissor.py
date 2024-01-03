import time
import random
x = raw_input ("Choose rock, paper or scissor:  ")

cpu_choice = ('rock','scissor','paper')

cpu = random.choice(cpu_choice)
print 'rock'
time.sleep(1)
print 'paper'
time.sleep(1)
print 'scissor'
time.sleep(1)
print 'shoot'
print ''
print ''
print cpu

if x == 'rock' and cpu == 'scissor':
  print 'you win'
elif x == 'rock' and cpu == 'rock':
  print 'it is a tie'
elif x == 'rock' and cpu == 'paper':
  print 'you lose'

if x == 'paper' and cpu == 'rock':
  print 'you win'
elif x == 'paper' and cpu == 'paper':
  print 'it is a tie'
elif x == 'paper' and cpu == 'scissor':
  print 'you lose'

if x == 'scissor' and cpu == 'paper':
  print 'you win'
elif x == 'scissor' and cpu == 'scissor':
  print 'it is a tie'
elif x == 'scissor' and cpu == 'rock':
  print 'you lose'

