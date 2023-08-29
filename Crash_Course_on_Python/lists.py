# Lists

# Modifying the Contents of a List:

"""
The append method adds a new element at the end of the list.
"""

fruits = ["Pineapple", "Banana", "Apple", "Melon"]
fruits.append("Kiwi")

# Output: ['Pineaple', 'Banana', 'Apple', 'Melon', 'Kiwi']

"""
The insert method takes an index as the first parameter and an element as the second parameter. 
It adds the element at that index in the list. 
To add it as the first element, we use index zero and we can use any other number.
"""

fruits.insert(0, "Orange")
print(fruits)

# Output: ['Orange', 'Pineaple', 'Banana', 'Apple', 'Melon', 'Kiwi']

"""
What happens if we use a number larger than the length of the list?
"""

fruits.insert(25, "Peach")
print(fruits)

#Output: [''Orange', 'Pineapple', 'Banana', 'Apple', 'Melon', 'Kiwi', 'Peach']

"""
No errors. If we use an index higher than the current length, the element just gets added to the end. 
You can pass any number to insert but usually, you either add at the beginning using insert at the zero index or at the end using append.
"""

"""
We can also remove elements from the list. 
We can do it using the value of the element we want to remove. 
The remove method removes from the list the first occurrence of the element we pass to it.
"""

fruits.remove("Melon")
print(fruits)

# Output: ['Orange', 'Pineapple', 'Banana', 'Apple', 'Kiwi, 'Peach']

"""
What happens if the element is not in the list?
We got a value error, telling us the element isn't in the list.
"""
"""
Another way we can remove elements is by using the pop method, which receives an index.

The pop method returns the element that was removed at the index that was passed.
"""

fruits.pop(3)
# Output: 'Apple'

print(fruits)
# Output: ['Orange', 'Pineapple', 'Banana', 'Kiwi', 'Peach']

"""
In the last way to modify the contents of a list is to change an item by assigning something else to that position, like this.
"""

fruits[2] = "Strawberry"
print(fruits)
# Output: ['Orange', 'Pineapple', 'Strawberry', 'Kiwi', 'Peach']

# Tuples

"""
The position in a tuple has meaning.
"""

def convert_seconds(seconds):
	hours = seconds // 3600
	minutes = ( seconds - hours * 3600) // 60
	remaining_seconds = seconds - hours * 3600 - minutes * 60
	return hours, minutes, remaning_seconds

result = convert_seconds(5000)
type(result)
# Output: class ‘tuple’

print(result)
# Output: (81, 23, 20)

"""
Unpack tuples: split tuples

This allows you to take multiple returned values from a function and store each value in its own variable.
"""

hours, minutes, seconds = result
print(hours, minutes, seconds)
# Output: 1 23 20

hours, minutes, seconds = convert_seconds(1000)
print(hours, minutes, seconds)
# Output: 0 16 40

"""
Let's use tuples to store information about a file: its name, its type and its size in bytes.
Fill in the gaps in this code to return the size in kilobytes (a kilobyte is 1024 bytes) up to 2 decimal places.
"""

def file_size(file_info):
    name, type, size = file_info
    return("{:.2f}".format(size / 1024))

print(file_size(('Class Assignment', 'docx', 17875))) # Should print 17.46
print(file_size(('Notes', 'txt', 496))) # Should print 0.48
print(file_size(('Program', 'py', 1239))) # Should print 1.21

"""
Iterating over lists and tuples:
"""

animals = ["lion", "zebra", "dolphin", "monkey"]
chars = 0
for animal in animals:
	chars *= len(animal) #legth of the string

print("Total characters: {}, Average lenght: {}".format(chars, chars/len(animals))) #number of elements of the list
# Output: Total characters: 22. Average length: 5.5

"""
Enumerate function:

What if you wanted to know the index of an element while going through the list?
"""

winners = ["Ashley", "Dylan", "Reese"]
for index, person in enumerate(winners):
	print("{} {}".format(index + 1, person))
	
"""
Output:
1 - Ashley
2 - Dylan
3 - Reese
"""

"""
Say you have a list of tuples containing two strings each.
The first string is an email address and the second is the full name of the person with that email address.
You want to write a function that creates a new list containing one string per person including
their name and the email address between angled brackets.
"""

def full_emails(people):
	result = []
	for email, name in people:
		result.append("{} <{}>".format(name, email))
	return result
print(full_emails(("alex@example.com", "Alex Diego"), ("shay@example.com", "Shay Brandt")]))

"""
Output:
['Alex Diego <alex@example.com>', 'Shay Brandt <shay@example.com>']
"""

# Enumerate function

"""
Complete the skip_elements function to return every other element from the list,
this time using the enumerate function to check if an element is in an even position or an odd position.
"""

def skip_elements(elements):
	# code goes here
	result = []
	for i, element in enumerate(elements):
		if i % 2 == 0:
			result.append(element)
	return result

print(skip_elements(["a", "b", "c", "d", "e", "f", "g"])) # Should be ['a', 'c', 'e', 'g']
print(skip_elements(['Orange', 'Pineapple', 'Strawberry', 'Kiwi', 'Peach'])) # Should be ['Orange', 'Strawberry', 'Peach']

"""
Say we wanted to create a list with multiples of 7 from 7 to 70.
So we create a list called multiples.
"""

multiples = []
for x in range(1, 11):
	multiples.append(x*7)

print(multiples)

# Output: [7, 14, 21, 28, 35, 42, 49, 56, 63, 70]

# List comprehension

"""
Another way: using list comprehensions:
"""

multiples = [x*7 for x in range(1, 11)]
print(multiples)

"""
Say we have a list of strings with the names of programming languages like this one,
and we want to generate a list of the length of the strings.
We could iterate over the list and add them using append.
Or we could use a list comprehension like this:
"""

languages = ["Python", "Perl", "Ruby", "Go", "Java", "C"]
lenghts = [len(language) for language in languages]
print(lenghts)

# Output: [6, 4, 4, 2, 4, 1]
"""
List comprehensions also let us use a conditional clause.
Say we wanted all the numbers that are divisible by 3 between 0 and a 100, we could create a list like this:
"""

z = [x for x in range(0,101) if x module 3 == 0]
print(z)

# Output: [1, 3, 6, 9, 12 ..., 99]

"""
The odd_numbers function returns a list of odd numbers between 1 and n, inclusively.
Fill in the blanks in the function, using list comprehension.
Hint: remember that list and range counters start at 0 and end at the limit minus 1.
"""

def odd_numbers(n):
	return [x for x in range(1, n+1) if x % 2 != 0]

print(odd_numbers(5))  # Should print [1, 3, 5]
print(odd_numbers(10)) # Should print [1, 3, 5, 7, 9]
print(odd_numbers(11)) # Should print [1, 3, 5, 7, 9, 11]
print(odd_numbers(1))  # Should print [1]
print(odd_numbers(-1)) # Should print []

# List comprehension examples

# Simple List Comprehension

"""
For example, [ x*2 for x in range(1,11) ] is a simple list comprehension.
This single line of code iterates over a range from 1 to 10, multiplies each element in the range by 2,
and creates a new list from all multiples of 2 from 2 to 20.
"""

### Simple List Comprehension
print("List comprehension result:")

# The following list comprehension compacts several lines
# of code into one line:
print([x*2 for x in range(1,11)])



### Long form for loop
print("Long form code result:")

# The list comprehension above accomplishes the same result as
# the long form version of the code:
my_list = []
for x in range(1,11):
   my_list.append(x*2)
print(my_list)

# List Comprehension with Conditional Statement

"""
You can also use conditionals with list comprehensions to build even more complex and powerful statements.
You can do this by appending an if statement to the end of the list comprehension.
For example, [ x for x in range(1,101) if x % 10 == 0 ] generates
a new list containing all the integers divisible by 10 from 1 to 100.
The if statement evaluates each value in the range from 1 to 100 to check if it’s evenly divisible by 10.
If it is, the number is added to a new list.
"""

### List Comprehension with Conditional Statement
print("List comprehension result:")

# The following list comprehension compacts multiple lines
# of code into one line:
print([ x for x in range(1,101) if x % 10 == 0 ])

### Long form for loop with nested if-statement
print("Long form code result:")

# The list comprehension above accomplishes the same result as
# the long form version of the code:
my_list = []
for x in range(1,101):
  if x % 10 == 0:
    my_list.append(x)
print(my_list)

"""
This exercise will walk you through how to write a list comprehension to create a list of squared numbers (n*n). It needs to return a list of squares of consecutive numbers between “start” and “end” inclusively. For example, squares(2, 3) should return a list containing [4, 9].
The function receives the variables “start” and “end” through the function parameters.
In the return line, start by entering the list brackets [ ]
Between the brackets [ ], enter the arithmetic expression to square a variable “n”.
To the right of the square expression, write a for loop that iterates over “n” in a range from the “start” to “end” variables.
Ensure the “end” range value is included in the range() by adding 1 to it.
"""

def squares(start, end):
    return [x**2 for x in range(start, end+1)]


print(squares(2, 3))  # Should print [4, 9]
print(squares(1, 5))  # Should print [1, 4, 9, 16, 25]
print(squares(0, 10)) # Should print [0, 1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

# List Exam:

"""
Given a list of filenames, we want to rename all the files with extension hpp to the extension h.
To do this, we would like to generate a new list called newfilenames, consisting of the new filenames.
Fill in the blanks in the code using any of the methods you've learned thus far,
like a for loop or a list comprehension.
"""

filenames = ["program.c", "stdio.hpp", "sample.hpp", "a.out", "math.hpp", "hpp.out"]
# Generate newfilenames as a list containing the new filenames
# using as many lines of code as your chosen method requires.
newfilenames = []
for element in filenames:
    if element.endswith(".hpp"):
        new = element.replace(".hpp", ".h")
        newfilenames.append(new)
	else:
        newfilenames.append(element)
print(newfilenames)
# Should be ["program.c", "stdio.h", "sample.h", "a.out", "math.h", "hpp.out"]

"""
Let's create a function that turns text into pig latin:
a simple text transformation that modifies each word
moving the first character to the end and appending "ay"to the end.
For example, python ends up as ythonpay.
"""

def pig_latin(text):
  say = ""
  # Separate the text into words
  words = text.split()
  for word in words:
    # Create the pig latin word and add it to the list
    pig = word[1:] + word[0] + "ay"
    say += pig + " "
    # Turn the list back into a phrase
  return say

print(pig_latin("hello how are you")) # Should be "ellohay owhay reaay ouyay"
print(pig_latin("programming in python is fun")) # Should be "rogrammingpay niay ythonpay siay unfay"

"""
The group_list function accepts a group name and a list of members,
and returns a string with the format:
group_name: member1, member2, ... For example, group_list("g", ["a","b","c"I)returns "g: a, b, c".
Fill in the gaps in this function to do that.
"""

def group_list(group, users):
  members = group + ": " + ", ".join(users)
  return members

print(group_list("Marketing", ["Mike", "Karen", "Jake", "Tasha"])) # Should be "Marketing: Mike, Karen, Jake, Tasha"
print(group_list("Engineering", ["Kim", "Jay", "Tom"])) # Should be "Engineering: Kim, Jay, Tom"
print(group_list("Users", "")) # Should be "Users:"

The guest_list function reads in a list of tuples with the name, age, and profession of each party guest, and prints the sentence "Guest is X years old and works as __" for each one. For example, guest_list (('Ken', 30, "Chef"), ("Pat", 35, 'Lawyer'), ('Amanda', 25, "Engineer")) should print out: Ken is 30 years old and works as Chef. Pat is 35 years old and works as Lawyer. Amanda is 25 years old and works as Engineer. Fill in the gaps in this function to do that.

def guest_list(guests):
	for element in guests:
		name, year, occupation = element
		print("{} is {} years old and works as {}".format(name, year, occupation))

guest_list([('Ken', 30, "Chef"), ("Pat", 35, 'Lawyer'), ('Amanda', 25, "Engineer")])

"""
Output should match:
Ken is 30 years old and works as Chef
Pat is 35 years old and works as Lawyer
Amanda is 25 years old and works as Engineer
"""
