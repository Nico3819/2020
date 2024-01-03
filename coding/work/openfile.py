f = open("abc.txt", "a")
name = p1
f.write(name + ' ')
#f.write(name)
last_name = "Shetty"
f.write(last_name + ' ')
#f.write(last_name)

name2 = "Leo"
f.write(name2 + ' ')
f.close()

#open and read the file after the appending:
#f = open("demofile2.txt", "r")
#print(f.read())

