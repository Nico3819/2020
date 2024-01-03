g = open("goalkeeper.txt","r")
y = 0
for x in g:
  y = y + 1
print ('goalkeepers = %s' % (y))

print ''
d = open("defender.txt","r")
y = 0
for x in d:
  y = y + 1  
print ('defenders = %s' % (y))
print ''
m = open("midfielder.txt","r")
y = 0
for x in m:
  y = y + 1
  
print ('midfielders = %s' % (y))

print ''
f = open("forward.txt","r")
y = 0
for x in f:
  print x
  y = y + 1  
print ('forwards = %s' % (y))

