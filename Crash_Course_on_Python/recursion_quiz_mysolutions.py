# Recursion Quiz

"""
What is recursion used for?

• Recursion is used to call a function from inside the same function.

You nailed it! By reducing the problem to a smaller one each time 
a recursive function is called, we can tackle complex problems in simple steps.
"""

"""
Which of these activities are good use cases for recursive programs? 
Check all that apply.

• Going through a file system collecting information related to directories and files.

Right on! Because directories can contain subdirectories that can contain 
more subdirectories, going through these contents is a good use case for a 
recursive program.

• Managing permissions assigned to groups inside a company, when each group 
can contain both subgroups and users.

Correct. As the groups can contain both groups and users, 
this is the kind of problem that is a great use case for a recursive solution.
"""

"""
Fill in the blanks to make the is_power_of function return whether the number 
is a power of the given base. 
Note: base is assumed to be a positive number. 
Tip: for tunctions that return a boolean value. 
You can return the result ot a comparison.
"""

def is_power_of(number, base):
    # Base case: when number is smaller than base.
    if number < base:
        # If number is equal to 1, it's a power (base**0).
        return number == 1

    # Recursive case: keep dividing number by base.
    return is_power_of(number // base, base)

print(is_power_of(8,2)) # Should be True
print(is_power_of(64,4)) # Should be True
print(is_power_of(70,10)) # Should be False

"""
Output:
True
True
False
"""

"""
Implement the sum_positive_numbers function, as a recursive function 
that returns the sum of all positive numbers between the number n received and 1. 
For example, when n is 3 it should return 1+2+3=6, and when n is 5 
it should return 1+2+3+4+5=15.
"""

def sum_positive_numbers(n):
  if n == 1:
    return 1
  else: 
    return n + sum_positive_numbers(n-1)

print(sum_positive_numbers(3)) # Should be 6
print(sum_positive_numbers(5)) # Should be 15

"""
Output:
6
15
"""