import time

x = input ("enter a number:  ")
y = 1 

def function(x,y):
  while y <= x:
    print y
    time.sleep(5)
    y = y + 1

function(x,y)
