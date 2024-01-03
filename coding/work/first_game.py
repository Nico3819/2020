#x = input('type a number:  ')

def first_game():
  while True:
    x = input ("enter a number")
    if x < 10:
      print ("you win")
      break
    elif x > 10:
      print ("try again")    

first_game()

