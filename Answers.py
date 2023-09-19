# Write the Following Functions 

# 1) Write a Python function called MAX_NUM()to find the maximum of three numbers 

def max_num(num_1,num_2,num_3):
  maximum = max(num_1,num_2,num_3)
  return (maximum)

 # Test 

result = max_num(33,66,99)
print("The maximum of these numbers is:", result)



# 2)Write a Python function called MULT_LIST() to multiply all the numbers in a list.


def mult_list(lst):
  #if empty list, return 0
  if len(lst) == 0:
    return 0
  #product starts with first element of list
  prod = lst[0]

  #go through list elements and multiply them together
  if len(lst) > 1:
    for i in lst[1:]:
      prod = prod * i

  return prod
    
print(mult_list([1,2,3]))
print(mult_list([]))
print(mult_list([15]))




# What I tested it with before I came to this above conclusion:

# def multi_list(numbers, *multiplier):
#     return result_list

#     for num in multi_list:
#         result_list.append(num * multiplier)
        
#         return result_list

# #test

# numbers_list= [10,2,5,2,2]
# multiplier = 10
# multi_list(numbers_list, multiplier)

# print("The multiplication of these numbers is:", multi_list * multiplier)


#3) Write a Python function called REV_STG() to reverse a string. 

original_string = "Hiya"
reversed_string = original_string[1::-1]
print(reversed_string)


# 4) Write a Python function called NUM_WITHIN() to check whether a number falls in a given range. 
# The function accepts the number, beginning of range, and end of range (inclusive) as arguments.
# Examples: num_within(3,2,4) returns True, num_within(3,1,3) returns True, num_within(10,2,5) returns False.

def num_within(number, start_range, end_range):
    if start_range <= number <= end_range:
        return True
    else:
        return False
    
    # Test

number_check = 10
start_range = 2
end_range = 20

if num_within(number_check, start_range, end_range):
    print("True")
else:
    print("False")



# 5) Write a Python function called PASCAL() that prints out the first n rows of Pascal's triangle.
# The function accepts the number n, the number of rows to print
# Note : Pascal's triangle is an arithmetic and geometric figure first imagined by Blaise Pascal. 
# Each number is the two numbers above it added together. 

def pascal(n):
    if n <= 0:
        return
    
    # Initialize the first row with 1
    current_row = [1]
    print(" " * (n - 1) + "1")  # Print the first row centered
    
    for _ in range(n - 1):
        next_row = [1]  # Initialize the next row with the first 1
        
        # Calculate the values for the next row
        for i in range(1, len(current_row)):
            next_value = current_row[i - 1] + current_row[i]
            next_row.append(next_value)
        
        next_row.append(1)  # Add the last 1 to the next row
        
        # Print the next row centered
        print(" " * (n - len(next_row)) + " ".join(map(str, next_row)))
        
        current_row = next_row

# Test the function with a value of n
n = 5
pascal(n)

# pascal(1)
# '''
# output:
# 1
# '''

# pascal(5)
# '''
# output:
# 1
# 1 1
# 1 2 1
# 1 3 3 1
# 1 4 6 4 1
# '''                     







