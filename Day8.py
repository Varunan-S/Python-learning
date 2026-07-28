# Working with strings
#n = "Varun"
#name = input ("enter the string")
#print (name)

# Indexing
word = "python"
print (word[4]) 

# Negative Index
print (word[-4])

# Slicing
# (Syntax) = string [start:end]
print (word[0:2])
print (word[:4])
print (word[3:])
print (word[::2])
print (word[::-1]) #reverse
print (word[::-2])
print (word[::1])

# String Length
# keyword = len
print (len(word))

# String Concatenation
Ticket = "Cinemark"
Pet = "Dog"
print (Ticket + " "+ Pet)

# String Repetition 
#print ("Orange " 3*)

# Checking true or false
Food = "Pizza"
print ("P" in Food)
print ("L" in Food)

# Uppercase
Animal = "haWk eYe"
print (Animal.swapcase())