def add(a,b):
    return a + b
print(add(5, 3))  # Output: 8

def add(*numbers):
    return sum(numbers)
print(add(1, 2, 3, 4))  # Output: 10