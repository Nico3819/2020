x = raw_input ("enter a word:  ")
q = 0
myrev = ''

for w in x:
   myrev = w + myrev

print myrev

if myrev == x:
  print 'this word is a palindrome'
else:
  print 'this word is not a palindrome'
