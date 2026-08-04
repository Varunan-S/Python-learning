# findidng elements
# Index
cows = ["maadu", "aadu", "paadu"]
print (cows.index("aadu"))

# Count
n = [2,4,5,6,2,3,7,2]
print (n.count(2))

# Sorting
a = [4,2,5,1,3]
a.sort()
print (a)
a.sort(reverse=True)
print (a)

# Sorted
x = [4,1,3]
new = sorted(x)
print (new)
print (x)

# Reverse a program
y = [1,2,3]
y.reverse()
print (y)

# List length
T = [1,2,3]
print (len(T))

# membership
fruits = ["Strawberry", "Lemon"]
print ("Lemon" in fruits)
print ("Mango" in fruits)

#List looping
n = [1,2,3,4,5,6,7,8,9]
for num in n:
    print (n)

# Using Index
for i in range (len(n)):
    print (i,n[i])