p1 = raw_input ("what is your favourite goalkeeper:  ")
p2 = raw_input ("what is your favourite defender:  ")
p3 = raw_input ("what is your favourite defender:  ")
p4 = raw_input ("what is your favourite defender:  ")
p5 = raw_input ("what is your favourite defender:  ")
p6 = raw_input ("what is your favourite midfielder:  ")
p7 = raw_input ("what is your favourite midfielder:  ")
p8 = raw_input ("what is your favourite midfielder:  ")
p9 = raw_input ("what is your favourite forward:  ")
p10 = raw_input ("what is your favourite forward:  ")
p11 = raw_input ("what is your favourite forward:  ")
f = open("goaleeper.txt", "a")
name = p1
f.write(name + '\n')
f.close()

d = open("defender.txt","a")
name2 = p2
d.write(name2 + '\n')
name3 = p3
d.write(name3 + '\n')
name4 = p4
d.write(name4 + '\n')
name5 = p5
d.write(name5 + '\n')
d.close()

m = open("midfielder.txt","a")
name6 = p6
m.write(name6 + '\n')
name7 = p7
m.write(name7 + '\n')
name8 = p8
m.write(name8 + '\n')
m.close()

f = open("forward.txt","a")
name9 = p9
f.write(name9 + '\n')
name10 = p10
f.write(name10 + '\n')
name11 = p11
f.write(name11 + '\n')
f.close()
