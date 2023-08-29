# List Quiz:

"""
Given a list of filenames, we want to rename all the files 
with extension hpp to the extension h.
To do this, we would like to generate a new list called newfilenames, 
consisting of the new filenames.
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

# Should be "ellohay owhay reaay ouyay"
print(pig_latin("hello how are you")) 
# Should be "rogrammingpay niay ythonpay siay unfay"
print(pig_latin("programming in python is fun")) 

"""
Which list method can be used to add a new element to a list at a 
specified index position?

list.insert(index, x)
"""

"""
Tuples and lists are very similar types of sequences. 
What is the main thing that makes a tuple different from a list?

A tuple is immutable
"""

"""
The group_list function accepts a group name and a list of members,
and returns a string with the format:
group_name: member1, member2, ... For example, 
group_list("g", ["a","b","c"I)returns "g: a, b, c".
Fill in the gaps in this function to do that.
"""

def group_list(group, users):
    members = group + ": " + ", ".join(users)
    return members

# Should be "Marketing: Mike, Karen, Jake, Tasha"
print(group_list("Marketing", ["Mike", "Karen", "Jake", "Tasha"])) 
# Should be "Engineering: Kim, Jay, Tom"
print(group_list("Engineering", ["Kim", "Jay", "Tom"])) 
print(group_list("Users", "")) # Should be "Users:"

"""
Output:
Marketing: Mike, Karen, Jake, Tasha
Engineering: Kim, Jay, Tom
Users:
"""

"""
The guest_list function reads in a list of tuples with the name, age, and profession of each party guest, and prints the sentence "Guest is X years old and works as __" for each one. For example, guest_list (('Ken', 30, "Chef"), ("Pat", 35, 'Lawyer'), ('Amanda', 25, "Engineer")) should print out: Ken is 30 years old and works as Chef. Pat is 35 years old and works as Lawyer. Amanda is 25 years old and works as Engineer. Fill in the gaps in this function to do that.
"""
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
