# Create a calculator function
# The function should accept three parameters:
# first_number: a numeric value for the math operation
# second_number: a numeric value for the math operation
# operation: the word 'add' or 'subtract'. The default operation is 'add'
# the function should return the result of the two numbers added or subtracted
# based on the value passed in for the operator
#
# Test your function using named notation passing in only the numbers 6 and 4
# Should return 10
#
# Test your function using named notation with the values 6,4, subtract 
# Should return 2
# 
# BONUS: Test your function with the values 6, 4 and divide 
# Have your function return an error message when invalid values are received
def calculation(first_number, second_number, operation):
    if operation.upper() == "ADD":
        answer = (float(first_number) + float(second_number))
        return answer
    elif operation.upper() == 'SUBTRACT':
        answer = (float(first_number) - float(second_number))
        return answer
    else:
        answer = (float(first_number) + float(second_number))
        return answer
    
first_n = input("Please type the first number: ")
second_n = input("Please type the second number: ")
operate = input("Please type the operation (ADD or SUBTRACT): ")
solution = calculation(first_n, second_n, operate)
if operate.upper() == 'ADD':
    print(f"Calculation: {first_n} + {second_n} = {solution}")
elif operate.upper() == 'SUBTRACT':
    print(f"Calculation: {first_n} - {second_n} = {solution}")
else:
    print(f"[INVALID OPERATE, DEFAULT OPERATE ADD] Calculation: {first_n} + {second_n} = {solution}")