# Program to sort alphabetically the words form a string provided by the user
x = raw_input ("enter a sentence or words:  ")

f = open ("myfile.txt","a")
f.write(x + '')
f = open ("myfile.txt","r") 
x = (f.read())
f.close()
# breakdown the string into a list of words
words = x.split()

# sort the list
words.sort()

#display the sorted words

print("The sorted words are:")
for word in words:
  print(word)
