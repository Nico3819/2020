x = input ("which year were you born: " )

def birthday(x):
  age=2020 - x
  return age

current_age = birthday(x)
  
def age_in_twenty (age):
  age_in_20 = age + 20
  print ('age in 20 years = %s'% (age_in_20))

age_in_twenty(current_age)

def age_in_fifty(age):
  age_in_50=age+50
  print ('age in 50 years = %s' % (age_in_50))

age_in_fifty(current_age)
