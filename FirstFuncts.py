## Exercise 28 - Your first Functions

# Create a program that defines functions for the four mathematical basic operations (+, -, * and /)
# Call each of the functions at least three times with different parameters

def sum_up(a,b):
    return a+b

def subtract(a,b):
    return a-b

def multiply(a,b):
    return a*b

def divide(a,b):
    return a/b

print(f"5 + 6 = {sum_up(5,6)}")
print(f"1 + 2 = {sum_up(1,2)}")
print(f"7 + 3 = {sum_up(7,3)}")

print(f"3 - 2 = {subtract(3,2)}")
print(f"10 - 5 = {subtract(10,5)}")
print(f"5 - 1 = {subtract(5,1)}")

print(f"2 * 2 = {multiply(2,2)}")
print(f"3 * 6 = {multiply(3,6)}")
print(f"1 * 10 = {multiply(1,10)}")

print(f"10 / 2 = {divide(10,2)}")
print(f"8 / 4 = {divide(8,4)}")
print(f"7 / 3 = {divide(7,3)}")
