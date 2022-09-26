## Exercise 29 - Functions with simple loops

# Write a program that contains two different functions
# The first function should take a list as an argument and return the sum of all
# elements in the list, calculated by a loop
# The second function should also take a list and return a list in which the contents
# of the list that was used as parameter are reversed (use a loop as well)

def sum_over(input_list):
    result = 0
    for i in input_list:
        result += i
    return result

def rev_list(input_list):
    return input_list[::-1]

list1 = list(range(2,10,2))

print(f"The sum of all elements in list {list1} is {sum_over(list1)}")
print(f"{list1} reversed is {rev_list(list1)}")

## Exercise 32 - Multiple returns from lists

# Take your functions from exercise 29 and create a new one that returns both results at once
# The function should include only one loop

def sum_rev(input_list):
        result = 0
        for i in input_list:
            result += i
        return result, input_list[::-1]

a,b = sum_rev(list1)
print(f"The sum of all elements in list {list1} is {a}")
print(f"{list1} reversed is {b}")
