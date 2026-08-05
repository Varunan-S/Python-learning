# Nested List
m = [[1,2],[3,4]]
print (m[0][1])

# List comprehension
n = [x for x in range (5)]
print (n)

# Even numbers
even = [x for x in range (2, 21, 2)]
print (even)

# Squares
s = [x*x for x in range (1,6)]
print (s)

# Average
n = [10, 20, 31]
a = sum (n) / len (n)
print (a)

# Remove duplicates
n = [1,2,2,3,4,4]
u = []
for i in n:
    if i not in u:
        u.append(i)
print (u)