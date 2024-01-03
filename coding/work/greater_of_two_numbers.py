x = input ("enter a number")
y = input ("enter a number")

def number(first_num,second_num):
  if first_num > second_num:
    return first_num
  elif first_num < second_num:
    return second_num
  elif first_num == second_num:
    return first_num
  else:
    print ("only numbers work")

answer = number(x,y)
print (answer)

