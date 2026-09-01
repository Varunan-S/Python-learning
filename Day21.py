# Func with conditions
def house(n):
    if n > 0:
        return "positive"
    elif n < 0:
        return "negative"
    else:
        return "zero"

print(house(2))
print(house(-4))
print(house(0))

