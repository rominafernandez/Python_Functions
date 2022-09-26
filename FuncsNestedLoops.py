## Exercise 30 - Functions with nested loops

# In Exercise 25 we worked with nested loops to find the maximum of a matrix,
# calculate the sum of all entries of a matrix and create a new matrix that is
# the result of element- wise multiplication of two other matrices
# Write a program that contains three different functions, one for each of the three tasks above

# Coordinates of max value
def max_matrix(input_matrix):
    max = 0
    max_index = [0,0]

    for i in list(range(len(input_matrix))):
        for j in list(range(len(input_matrix[i]))):
            if my_matrix[i][j] > max:
                max = input_matrix[i][j]
                max_index[0] = i
                max_index[1] = j
    return max, max_index

# Sum up matrix
def sum_matrix(input_matrix):
    sum = 0
    for i in input_matrix:
        for j in i:
            sum = sum + j
    return sum

# multiplicate two matrices (with the same dimensions!)
def multiply_matrices(matrix1, matrix2):
    result_matrix = []

    for i in list(range(len(matrix1))):
        tmp = list(range(len(matrix1[i])))
        for j in list(range(len(matrix1[i]))):
            tmp[j] = matrix1[i][j] * matrix2[i][j]
        result_matrix.append(tmp)
    return result_matrix

# use the above Functions
my_list = []
my_matrix = []

for i in range(3):
    my_list.append(i)
for j in range(3):
    my_matrix.append(my_list)

# my_matrix = [[1,3,5],[2,4,6],[7,8,9]]

a,b = max_matrix(my_matrix)
print(f"The max value of the matrix is {a} and first occurs at index {b}")
print(f"The sum of all elements in the matrix is {sum_matrix(my_matrix)}.")
print(f"The first matrix multiplicated by itself results in: {multiply_matrices(my_matrix,my_matrix)}")
