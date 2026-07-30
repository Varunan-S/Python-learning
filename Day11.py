# Reverse String
word = "Varun"
print (word[::-1])

# Reverse without bulit in function
num = input ("enter the string: ")
reverse = ""
for i in num:
    reverse = i + reverse
print ("reversed string is", reverse)