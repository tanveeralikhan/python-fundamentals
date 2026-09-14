def greet(name="Tanveer"):
    return f"Hello, {name}!"

print(greet("Alice"))
print(greet())
print(greet(None)) 
print(greet(True))  # This will print "Hello, True!" since True is passed as the name