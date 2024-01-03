# import only system from os 
from os import system, name 

# import sleep to show output for some time period 
from time import sleep 

# define our clear function 
def clear(): 

	# for windows 
	if name == 'nt': 
		_ = system('cls') 

	# for mac and linux(here, os.name is 'posix') 
	else: 
		_ = system('clear') 

#
# nico's code
#
import random
x = 0
while True:
  print "  o  "
  print " /|\ "
  print " / \ "
  sleep(0.5)
  clear()
  print " \ o / "
  print "   |   "
  print "  / \  "
  sleep(0.5)
  clear()
  print "      _ o  "
  print "       /\  "
  print "      | \  "
  sleep(0.5)
  clear()
  print "            ___\o "
  print "           /)  |  "
  sleep(0.5)
  clear()
  print "                 __|   " 
  print "                   \o  " 
  print "                   ( \ " 
  sleep(0.5)
  clear()
  print "                       \ /  "
  print "                        |   " 
  print "                       /o\  "
  sleep(0.5)
  clear()
  print "                            |__  "
  print "                          o/     "
  print "                         / )     "
  sleep(0.5)
  clear()
  print "                                 o/__ "  
  print "                                 |  (\ " 
  sleep(0.5)
  clear()
  print "                                        o _ " 
  print "                                        /\  "  
  print "                                        / | " 
  sleep(0.5)
  clear()
  print "                                           \ o / "
  print "                                             |   "
  print "                                            / \  "
  sleep(0.5)
  clear()
  print "                                               o  "
  print "                                              /|\ "
  print "                                              / \ "
  sleep(0.5)
  clear()
  x = x + 1
  if x == 3:
    break
