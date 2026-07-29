# End keyword
D = "Doggy"
print (D.endswith("gy"))

# isdigit
print ("2478".isdigit())
print ("1237ab".isdigit())

# isalpha
print ("adfg".isalpha())
print ("6fgd".isalpha())

# isalmun
print ("hag43".isalnum())
print ("sg 47".isalnum())

# islower
print ("x".islower())

# isupper
print ("Z".isupper())

# isspace
print ("  ".isspace())

# escapecharacters
print ("i\n am\n Varunan")

# string formatting
name = "Varun"
print ("Hi" + name)

# Format
name = "Varun"
age = 15
print ("my name is {} and my age is {}".format(name, age))

# f string
name = "kaleb"
age = 18
print (f"my name is {name} and I am {age} yeards old")

# building functioms
text = "Python" 
print (len (text))
print (max (text))
print (min (text))
print (sorted (text))