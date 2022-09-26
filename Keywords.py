## Exercise 64 - Keywords in Python_Functions

# Create a list with at least 15 random entries
# Iterate over it with a for loop and add up the elements
# Create one if statement in your loop that can’t be true and add a pass
# Include a second if statement in your loop that breaks the loop if your sum gets bigger than a threshold (you chose)
# Include a third if statement in your loop that uses continue if the current entry
# of your list is in a specific range, eg. 50 to 60, and prints out something in all other cases (use else)
# Print out the sum and the number of iterations

list1 = list(range(2,50,2))
sum = 0
tmp = 0

for i in list1:
    sum += i
    tmp += 1
    if i > len(list1):
        pass
    if sum > 30:
        break
    if i > 5 and i < 10:
        continue
    print(f"+ {i} is {sum} and it's iteration nr. {tmp}")
