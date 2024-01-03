while True:
  name = raw_input ("What is your name?  ")
  pos = raw_input ("What is your position?  ")

  if pos == "goalkeeper":
    g = open("goalkeeper.txt","a")
    g.write(name + '\n')

  if pos == "defender":
    d = open("defender.txt","a")
    d.write(name + '\n')

  if pos == "midfielder":
    m = open("midfielder.txt","a")
    m.write(name + '\n')

  if pos == "forward":
    f = open("forward.txt","a")
    f.write(name + '\n')
  
  if name == "exit":
    break
  
