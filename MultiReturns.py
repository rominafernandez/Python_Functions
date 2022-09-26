## Exercise 31 - Multiple Returns

# In exercise 28 you created four different functions, now combine them into a new
# function that returns all four results at once
# Call this function at least three times with different parameters and print out the results

def math_ops(a,b):
    add_result = a+b
    subtract_result = a-b
    multiply_result = a*b
    division_result = a/b
    return add_result, subtract_result, multiply_result, division_result

a,b,c,d = math_ops(5,9)
print(f"5 + 9 = {a}; 5 - 9 = {b}; 5 * 9 = {c}, 5 / 9 = {d}")

a,b,c,d = math_ops(7,12)
print(f"7 + 12 = {a}; 7 - 12 = {b}; 7 * 12 = {c}, 7 / 12 = {d}")

a,b,c,d = math_ops(15,4)
print(f"15 + 4 = {a}; 15 - 4 = {b}; 15 * 4 = {c}, 15 / 4 = {d}")
