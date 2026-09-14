def greet(name="Tanveer"):
    return f"Hello, {name}!"

print(greet("Alice"))
print(greet())
print(greet(None)) 
print(greet(True))  # This will print "Hello, Bob!" since "Bob" is passed as the name