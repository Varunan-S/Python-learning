# Reverse String
word = "Varun"
print (word[::-1])

# Reverse without bulit in function
num = "food"
reverse = ""
for i in num:
    reverse = i + reverse
print ("reversed string is", reverse)

# Palindrome check
w = input ("enter the string: ")
if w == w[::-1]:
    print ("String is a palindrome")

else:
    print ("string is false")