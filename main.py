import calculator
print(calculator.add(2, 5))
print(calculator.sub(2, 5))

# specific func in mod
from calculator import add
print(add(7, 5))

# Alias in mod
import calculator as cal
print(cal.sub(2, 2))
