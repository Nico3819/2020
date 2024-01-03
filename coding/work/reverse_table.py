x1 = 'liverpool'
x2 = 'man city'
x3 = 'leiceter'
x4 = 'chelsea'
x5 = 'man united'

table = x1,x2,x3,x4,x5

x = 0
for y in table:
  print y
  x = x + 1
  

print x

print table[x-1]
print table[x-2]
print table[x-3]
print table[x-4]
print table[x-5]
print ' '

for myvar in range(5,0,-1) :
  print table[myvar-1]

