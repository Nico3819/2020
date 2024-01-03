#y = 0
myplayer = 'messi'
#g = open("goalkeeper.txt","r")
#for x in g:
#if g == myplayer:
 # print 'goalkeeper : yes'
#else:
 # print 'goalkeeper : no'

#print ''
#d = open("defender.txt","r")
#y = 0
#for x in d:
#if g == myplayer:
#  print 'defender : yes'
#else:
 # print 'defender : no'
#print ''
#m = open("midfielder.txt","r")
#y = 0
#for x in m: 
#print ('midfielders : %s' % (y))
#if m == myplayer:
 # print 'midfielder : yes'
#else:
 # print 'midfielder : no'
#print ''
f = open("forward.txt","r")
x = (f.read())
# breakdown the string into a list of words
words = x.split()
for x in words:
  print(x)

#y = 0
#for  in f:
  #x = (f.read())
#  print x
  if x == myplayer:
    print 'forwards : yes'
  else:
    print 'forwards : no'
