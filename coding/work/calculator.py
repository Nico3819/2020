num_one        = input ("enter a number:  ")
math_operation = raw_input ("enter + or - or *:  ")
num_two        = input ("enter a number:  ")

def plus(a,b):
  total=a+b
  return total

if math_operation == '+':
  answer = plus(num_one,num_two)
  print answer

def multcation(a,b):
  total=a*b
  return total

if math_operation == '*':
   answer=multcation(num_one,num_two)
   print answer
def minus(a,b):
  total=a-b
  return total

if math_operation == '-':
  answer=minus(num_one,num_two)
  print answer
else:
  print('invalid')
  #answer=plus(num_one,num_two)
  #print answer
#elif math_operation == '*':
#answer=plus(num_one,num_two) 
#print ("multi")
#else:
  #print ("try again")  

