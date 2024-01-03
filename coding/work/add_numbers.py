number_add = input("Enter number : ") 
value_of_number = 1
endpoint = 0

def adding(number_add,value_of_number,endpoint):
  while value_of_number<=number_add:
    endpoint=endpoint+value_of_number
    value_of_number=value_of_number+1
    
  print endpoint

adding(number_add,value_of_number,endpoint)
