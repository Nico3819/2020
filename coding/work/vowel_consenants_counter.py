x = raw_input ("enter a word:  ")
q = 0
v = 0
c = 0

for y in x:
  q = q + 1
  if y == 'a' or y == 'e' or y == 'i' or y == 'o' or y == 'u':
    v = v + 1
  else:
    c = c + 1




print ''
print ('the number of letters in this word is %s' % (q))
print ''
print ('the number of vowels in this word is %s' % (v))
print ''
print ('the number of consenants in this word is %s' % (c))
