# Loops exam

"""
Fill in the blanks to print the numbers 1 through 7.
"""

number = 1 # Initialize the variable
while number < 8: # Complete the while loop condition
    print(number, end=" ")
    number += 1 # Increment the variable

# Should print 1 2 3 4 5 6 7 

"""
Find and correct the error in the for loop below. 
The loop should print every even number from 2 to 12.
"""

for number in range(2, 14, 2):
    print(number)

# Should print:
# 2
# 4
# 6
# 8
# 10
# 12

"""
Fill in the blanks to complete the function "digits (n)" to count how many digits 
the given number has. For example: 25 has 2 digits and 144 has 3 digits.

Tip: you can count the digits of a number by dividing it by 10 once per digit until 
there are no digits left.
"""

def digits(n):
    count = 0
    if n == 0:
      count = 1
    while n > 0: # Complete the while loop condition
        # Complete the body of the while loop. This should include 
        # performing a calculation and incrementing a variable in the
        # appropriate order.  
        n = n//10
        count += 1
    return count
    
print(digits(25))   # Should print 2
print(digits(144))  # Should print 3
print(digits(1000)) # Should print 4
print(digits(0))    # Should print 1

"""
Fill in the blanks to complete the "rows _asterisks" function. This function should 
print rows of asterisks (*), where the number of rows is equal to the "rows" variable. 
The number of asterisks per row should correspond to the row number (row 1 should have
1 asterisk, row 2 should have 2 asterisks, etc.). 
Complete the code so that "row_asterisks(5)" will print:
* 
* * 
* * * 
* * * * 
* * * * * 
"""

def rows_asterisks(rows):
    # Complete the outer loop range to control the number of rows
    for x in range(rows): 
        # Complete the inner loop range to control the number of 
        # asterisks per row
        
        for y in range(x + 1): 
            # Prints one asterisk and one space
            print("*", end=" ")
        # An empty print() function inserts a line break at the 
        # end of the row 
        print()


rows_asterisks(5)
# Should print the asterisk rows shown above

"""
Fill in the blanks to complete the "countdown" function. This function should begin 
at the "start" variable, which is an integer that is passed to the function, and count 
down to 0. Complete the code so that a function call like "countdown (2)" will return 
the numbers "2,1,0".
"""

def countdown(start):
    x = start
    if x > 0:
        return_string = "Counting down to 0: "
        while x >= 0: # Complete the while loop
            return_string += str(x) # Add the numbers to the "return_string"
            if x > 0:
                return_string += ","
            x -= 1 # Decrement the appropriate variable
    else:
        return_string = "Cannot count down to 0"
    return return_string


print(countdown(10)) # Should be "Counting down to 0: 10,9,8,7,6,5,4,3,2,1,0"
print(countdown(2)) # Should be "Counting down to 0: 2,1,0"
print(countdown(0)) # Should be "Cannot count down to 0"

"""
The following code raises an error when executed. What's the reason for the error?

def decade_counter :
    while vear < 50:
        year += 10 
    return year
    
Answer: Failure to initialize the variable
"""

"""
What is the first number that will be printed in the first iteration of this loop? 
Your answer should be only one number.
"""

for count in range(1, 6):
    print(count+1)
    
# Answer: 2

"""
What number is printed at the end of this code?
"""

num1 = 0
num2 = 0

for x in range (5):
    num1 = x
    for y in range (14):
        num2 = y + 3
            
print (num1 + num2)

# Answer: 20

"""
The following code causes an Intinite loop. Can you figure out what Is Incorrect?
"""

def test_code(num):
    x = num
    while x % 2 == 0:
        x = x/2
        
test_code (0)

# Answer: When called with 0, it triggers an infinite loop

# Loops Exam: 

"""
Fill in the blanks to print the even numbers from 2 to 12.
"""

number = 2 # Initialize the variable 
while number < 13 and number % 2 == 0: # Complete the while loop condition
    print(number, end=" ")
    number += 2 # Increment the variable

# Should print 2 4 6 8 10 12 

"""
Find and correct the error in the for loop below. The loop should check each number 
from 1 to 5 and identify if the number is odd or even.
"""

for number in range(1,6):
    if number % 2 == 0:
        print("even")
    else:
        print("odd")


# Should print:
# odd
# even
# odd
# even
# odd

"""
Fill in the blanks to complete the "factorial" function. This function will accept 
an integer variable "n" through the function parameters and produce the factorials 
of this number (by multiplying this value by every number less than the original number
[n* (n-1)], excluding 0). To do this, the function should:

-accept an integer variable "n" through the function parameters;
-initialize a variable "result" to the value of the "n" variable;
-iterate over the values ot "n" using a while loop until "n" is equalto O;
-starting at n-1, multiply the result by the current "n" value;
-decrement "n" bv-1.
For example, factorial 3 would return the value ot 3*2*1, which would be 6.
"""

def factorial(n):
    result = n
    start = n
    n -= 1
    while n > 0: # The while loop should execute as long as n is greater than 0
        result *= n # Multiply the current result by the current value of n
        n -= 1 # Decrement the appropriate variable by -1
    return result


print(factorial(3)) # Should print 6
print(factorial(9)) # Should print 362880
print(factorial(1)) # Should print 1

"""
Fill in the blanks to complete the "sequence" function. This function should print a 
sequence of numbers in descending order, from the given "high" variable to the given 
"low" variable. The range should make the loop run two times. Complete the range 
sequences in the nested loops so that the "sequence (1, 3)" function call prints the 
following:
3, 2, 1
3, 2, 1
"""

def sequence(low, high):
    # Complete the outer loop range to make the loop run twice
    # to create two rows
    for x in range(2): 
        # Complete the inner loop range to print the given variable
        # numbers starting from "high" to "low" 
        # Hint: To decrement a range parameter, use negative numbers
        for y in range(high, low -1, -1): 
            if y == low:
                # Don’t print a comma after the last item
                print(str(y)) 
            else:
                # Print a comma and a space between numbers
                print(str(y), end=", ") 

sequence(1, 3)
# Should print the sequence 3, 2, 1 two times, as shown above.

"""
What happens when the Python interpreter executes a loop where a variable used inside 
the loop is not initialized?

Answer: Will produce a NameError stating the variable is not defined
"""

"""
How many number will this loop print? Your answer should be one number.
"""

for sum in range(5):
    sum += sum
    print(sum)
    
# Answer: 5
    
"""
What number is printed at the end of this code?
"""

num1 = 0
num2 = 0

for x in range(5):
    num1 = x
    for y in range(14):
        num2 = y + 3

print(num1 + num2)

"""
The outer loop iterates over x from 0 to 4, and for each value of x, the inner loop 
iterates over y from 0 to 13. However, both num1 and num2 are overwritten in each 
iteration of the loops. Therefore, when the loops finish, num1 will have the value 4 
(since the last value of x in the loop is 4), and num2 will have the value 16 (since 
the last value of y in the inner loop is 13, and num2 is assigned y + 3).

So, at the end of the code, the sum of num1 and num2 will be 4 + 16 = 20. Therefore, 
the number printed at the end of the code will be 20.
"""

"""
The following code causes an infinite loop. Can you figure out what's incorrect and 
how to fix it?

def count_to_ten():
  # Loop through the numbers from first to last 
  x = 1
  while x <= 10:
    print(x)
    x = 1


count_to_ten()
# Should print:
# 1
# 2
# 3 
# 4
# 5
# 6
# 7
# 8 
# 9
# 10

Answer: Variable "x" is assigned the value 1 in every loop
"""
