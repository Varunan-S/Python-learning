# Exception handling-Handling an error knwoing it will occur prior to it happening, so the program can run smoothly.
# keywords for Exception handling-try, except
try:
    a = 10
    b = 0
    print(a/b)
except:
    print("error expected")
try:
    age = int(input("enter the age"))
    print(age)
except:
    print("Please enter a valid number")