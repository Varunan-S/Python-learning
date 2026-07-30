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
w = "lk"
if w == w[::-1]:
    print ("String is a palindrome")

else:
    print ("string is false")

# count vowels
text = input ("enter the string: ")
count = 0
for i in text:
    if i in "aeiouAEIOU":
        count += 1
print (count)
