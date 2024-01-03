import random
import time

print 'Q:  How do you think your team played?'
time.sleep(3)
answers = ('I think that they played well','It is always hard on the road','They did not play so great today','The boys gave everything, but its hard place to come', 'We are happy with a point on the road', 'This is not the way to play football, they just parked the bus', 'Some player have to sacked, if not i will get sacked')
print ''
print (random.choice(answers))
time.sleep(3)
print ''
print 'Q:  Do you think that last goal was a goal?'
time.sleep(3)
print ''
answer1 = ('I did not see it yet','No I saw that he was offside','Yes it was a goal', 'VAR is a waste of time', 'You tell me if it was a goal!', 'I dont want to talk about it')
print (random.choice(answer1))
time.sleep(3)
print ''
print 'Q:  What did you tell the players at halftime?'
time.sleep(3)
print ''
answer2 = ('Do what they were doing in the first half','I told them they needed to be more quick','I told them to wake up', 'To not concede a goal early in the second half', 'To get the first goal early in the second half','They should use the wings more often','They should park the bus','Play long balls to the strikers', 'To play more physical')
print (random.choice(answer2))
time.sleep(3)
print ''

