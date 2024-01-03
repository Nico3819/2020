#/usr/bin/pyth

print ('===================================================')
print ('I                                                 I')
print ('I  O POWER                                        I')
print ('I                                                 I')
print ('I                                                 I')
print ('I                      Mute                       I')
print ('I                                                 I')
print ('I                        ^                        I')
print ('I     exit                              guide     I')
print ('I                                                 I')
print ('I               <                 >               I')
print ('I       +                                 ^       I')
print ('I                                                 I')
print ('I    volume                            channel    I')
print ('I                        V                        I')
print ('I       -                                 v       I')
print ('I                                                 I')
print ('I          <<           >ll           >>          I')
print ('I                                                 I')
print ('I                                                 I')
print ('I                                                 I')
print ('I                                                 I')
print ('I                                                 I')
print ('I   1                    2                     3  I')
print ('I                                                 I')
print ('I                                                 I')
print ('I   4                    5                     6  I')
print ('I                                                 I')
print ('I                                                 I')
print ('I   7                    8                     9  I')
print ('I                                                 I')
print ('I                                                 I')
print ('I                        0                        I')
print ('I                                                 I')
print ('I                                                 I')
print ('I                                                 I')
print ('I                                                 I')
print ('I                                                 I')
print ('I                                                 I')
print ('==================================================I')
print ('                                                   ')
x = raw_input('enter your choice:  ')
print x

if x == "volume +":
  print ("volume +1")
elif x == "volume -":
  print ("volume -1")
elif x == ">>":
  print ("fast forward")
elif x == "<<":
  print ("go back")
elif x == "1":
  print ("enter channel number")
elif x == ">ll":
  print ("pause/resume")
elif x == "^":
  print ("up")
elif x == ">":
  print ("right")
elif x == "<":
  print ("left")
elif x == "V":
  print ("down")
elif x == "mute":
  print ("volume 0")
elif x == "exit":
  print ("exit")
else:
  print ("invalid button try again")

