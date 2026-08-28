stud = {
    "Alex": 85,
    "John": 72,
    "Sarah": 91,
    "Mike": 68,
    "Emma": 80
}

total = 0

for name in stud:
    total = total + stud[name]

highest = 0
lowest = 100

for name in stud:
    if stud[name] > highest:
        highest = stud[name]

    if stud[name] < lowest:
        lowest = stud[name]

for name in stud:
    if stud[name] >= 80:
        print(name, "Good")
    else:
        print(name, "Average")

print("Total:", total)
print("Highest:", highest)
print("Lowest:", lowest)



sentence = input("Enter a sentence: ")

words = 1
letters = 0
vowels = 0

for char in sentence:
    if char == " ":
        words = words + 1
    else:
        letters = letters + 1

    if char == "a" or char == "e" or char == "i" or char == "o" or char == "u":
        vowels = vowels + 1

print("Words:", words)
print("Letters:", letters)
print("Vowels:", vowels)