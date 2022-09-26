# Exercise 70 - Functions with defaults

# Create a python program that uses default arguments in its functions

def value_root(value, root=2):
    return value**(1/root)

print(f"The square root of 16 is {value_root(16)}")
print(f"The third root of 16 is {value_root(16,3)}")


## Exercise 71 - Keyword arguments

# Try to call back your generated functions with the help of keyword arguments
# Change the order of the handed over arguments while doing so

print(f"The square root of 25 is {value_root(value = 25)}")
print(f"The third root of 25 is {value_root(root = 3, value = 25)}")
