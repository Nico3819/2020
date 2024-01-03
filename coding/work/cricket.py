import random
import time

print "--------------------------------------------------------------------------"
print " "
print "@                               _                                  ,,"
print " \\   _   @'                    ( )_                       .      _  \\"
print "  \\_( )_//                    / Y |                   .      /--( )_//"
print "    | Y/--                    /\   /               .        //  \~ \ "
print "    |_/       _ / o          ( _\ /            .                   - \ "
print "  _ //\      | | |    .       \_\\\        .                     //  \\--,"
print " /_// /      | | |      .    / \ \\\ .                           \\"
print "/ // /_______|_|_|__________/_/_\ \_______________________________\\______"
print "-------------------------------------------- Play Cricket ----------------"
print " "

print 'Team Nico batting'
runs = 0
ball = 1
x = random.randint(0,6)

while True:
  out = ('BOWLED!!!','LBW!!!','Run out!!!','Caught Behind!!!','Hit Wicket!!!','Caught and bowled!!!','Obstructing the field!!!','Stumped!!!')
  hit0 = ('well fielded','straight to the fielder','beaten','slight hesitatiion no run','well left')
  hit1 = ('he played it safely there','quick single')
  hit2 = ('fielder preventing it from being a 4','playing safe on that one','easy shot right there')
  hit3 = ('great shot to get the 3','oh nearly a 4 but the fielder blocking the ball','great placement of the ball','just short of 4 runs')
  hit4 = ('great placement of the ball','great shot','nearly a six','brilliant cover drive','great pull shot','through the gaps')
  hit6 = ('great shot in the stands','over all the players heads','the ball goes high in the stands','ball goes high in the air and outside the stadium')
  #if x == 5:
   # time.sleep(1)
   # print random.choice(out)
   # break

  time.sleep(3.5)
  print ''
  print ('* %s balls: ' % (ball))
  ball = ball + 1
  x = random.randint(0,6)
  if x == 5:
    time.sleep(1)
    print random.choice(out)
    break
  print ''
  print ('%s runs' % (x))
  if x == 0:
    print random.choice(hit0)
  elif x == 1:
    print random.choice(hit1)
  elif x == 2:
    print random.choice(hit2)
  elif x == 3:
    print random.choice(hit3)
  elif x == 4:
    print random.choice(hit4)
  elif x == 6:
    print random.choice(hit6)
  runs = runs + x
  print ''
  print ('score = %s' % (runs))

print ('Team Nico total = %s' % (runs))

print "----------------------"
print 'Team Leo batting'
runs1 = 0
ball1 = 1
x = random.randint(0,6)

while True:
  out = ('BOWLED!!!','LBW!!!','Run out!!!','Caught Behind!!!','Hit Wicket!!!','Caught and bowled!!!','Obstructing the field!!!','Stumped!!!')
  #if x == 5:
   # time.sleep(1)
   # print random.choice(out)
   # break

  time.sleep(3.5)
  print ''
  print ('* %s balls: ' % (ball1))
  ball1 = ball1 + 1
  x = random.randint(0,6)
  if x == 5:
    time.sleep(1)
    print random.choice(out)
    break

  print ''
  print ('%s runs' % (x))
  if x == 0:
    print random.choice(hit0)
  elif x == 1:
    time.sleep(1)
    print random.choice(hit1)
  elif x == 2:
    time.sleep(1)
    print random.choice(hit2)
  elif x == 3:
    time.sleep(1)
    print random.choice(hit3)
  elif x == 4:
    time.sleep(1)
    print random.choice(hit4) 
  elif x == 6:
    time.sleep(1)
    print random.choice(hit6) 
  runs1 = runs1 + x
  if x == 5:
    time.sleep(1)
    print random.choice(out)
    break

  print ''
  print ('score = %s' % (runs1))
print ('Team Leo total = %s' % (runs1))  



if runs1 == runs:
  print "  ________________   "
  print " /_  __/  _/ ____/ "
  print "  / /  / // __/   "
  print " / / _/ // /___   "
  print "/_/ /___/_____/   "
                  


elif runs1 > runs:
  print "  ______                        __                  _       ___           "
  print "/_  __/__  ____ _____ ___      / /   ___  ____     | |     / (_)___  _____"
  print "  / / / _ \/ __ `/ __ `__ \   / /   / _ \/ __ \    | | /| / / / __ \/ ___/ "
  print " / / /  __/ /_/ / / / / / /  / /___/  __/ /_/ /    | |/ |/ / / / / (__  ) "
  print "/_/  \___/\__,_/_/ /_/ /_/  /_____/\___/\____/     |__/|__/_/_/ /_/____/  "


elif runs1 < runs:
  print "  ______                        _   ___               _       ___           "
  print " /_  __/__  ____ _____ ___     / | / (_)________     | |     / (_)___  _____"
  print "  / / / _ \/ __ `/ __ `__ \   /  |/ / / ___/ __ \    | | /| / / / __ \/ ___/ "
  print " / / /  __/ /_/ / / / / / /  / /|  / / /__/ /_/ /    | |/ |/ / / / / (__  )  "
  print "/_/  \___/\__,_/_/ /_/ /_/  /_/ |_/_/\___/\____/     |__/|__/_/_/ /_/____/  "

