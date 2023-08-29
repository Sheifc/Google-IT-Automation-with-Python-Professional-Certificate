# Exam: Strings, Lists, Dictionaries

"""
Fill in the blanks to complete the "confirm_length" function.
This function should return how many characters a string contains as long as it has one or more characters,
otherwise it will return 0.
Complete the string operations needed in this function so that input like "Monday" will produce the output "6".
"""

def confirm_length(word):
    # Complete the condition statement using a string operation.
    if len(word) > 0:
        # Complete the return statement using a string operation.
        return len(word)
    else:
        return 0

print(confirm_length("a")) # Should print 1
print (confirm_length("This is a long string)) # Should print 21
print (confirm_length ("Monday")) # Should print 6 print
print(confirm_length("")) # Should print 0

"""
Output:
1
21
6
0
"""

"""
Complete the for loop and string method needed in this function so that a function call like
"alpha_length("This has 1 number in it")" will return the output "17". This function should:

1. accept a string through the parameters of the function;
2. iterate over the characters in the string;
3. determine if each character is a letter
(counting only alphabetic characters; numbers, punctuation, and spaces should be ignored);
4. increment the counter;
5. return the count of letters in the string.
"""

def alpha_length(string):
    character = '"
    count_alpha = 0
    # Complete the for loop sequence to iterate over "string".
    for x in string:
        # Complete the if-statement using a string method.
        if x.isalpha():
            count_alpha += 1
    return count_alpha

print(alpha_length("This has 1 number in it")) # Should print 17
print (alpha_length("Thisisallletters")) # Should print 16
print (alpha_length ("This one has punctuation!")) # Should print 21

"""
Output:
17
16
21
"""

"""
Consider the following scenario about using Python lists:
Employees at a company shared the distance they drive to work (in miles) through an online survey.
These distances were automatically added by Python to a list called "distances"
in the order that each employee submitted their distance.
Management wants the list to be sorted in the order of the longest distance to the shortest distance.

Complete the function to sort the "distances" list. This function should:
1. sort the given "distances" list, passed through the function's parameters;;
2. reverse the sort order so that it goes from the longest to the shortest distance;
3. return the modified "distances" list.
"""

def sort_distance (distances):
    distances.sort() # Sort the list
    distances.reverse () # Reverse the order of the list return distances

print(sort_distance([2,4,0,15,8,9]))
# Should print [15, 9, 8, 4, 2, 0]

"""
Output: [15, 9, 8, 4, 2, 0]
"""

"""
Fill in the blank to complete the "squares" function.
This function should use a list comprehension to create a list of squared numbers
(using either the expression n*n or n**2).
The function receives two variables and should return the list of squares that occur
between the "start" and "end" variables inclusively
(meaning the range should include both the "start" and "end" values).
Complete the list comprehension in this function so that input like "squares (2, 3)"
will produce the output "[4, 9]".
"""

def squares (start, end):
    return [n*n for n in range(start, end+1)] # Create the required list comprehension.

print(squares (2, 3)) # Should print [4, 9]
print (squares (1, 5)) # Should print [1, 4, 9, 16, 25]
print(squares (0, 10)) # Should print [0, 1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

"""
Output:
[4, 97
[1, 4, 9, 16, 25]
[0, 1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
"""

"""
Fill in the blanks to complete the "car_listing" function.
This function accepts a "car_prices" dictionary.
It should iterate through the keys (car models) and values (car prices) in that dictionary.
For each item pair, the function should format a string so that a dictionary entry like
"Kia Soul":19000" will print "A Kia Soul costs 19000 dollars".
Each new string should appear on its own line.
"""

def car_listing(car_prices):
    result = ""
    # Complete the for loop to iterate through the key and value items
    # in the dictionary.
    for key, value in car prices.items():
        result += "A {} costs {} dollars\n".format(key. value) # Use a string method to format the required string
return result
print(car_listing({"Kia Soul": 19000, "Lamborghini Diablo":55000, "Ford Fiesta":13000,
                   "Toyota Prius' :24000}))

# Should print:
# a Kia Soul costs 10000 dollars
# A Lamborghini Diablo costs 55000 dollars
# A Ford Fiesta costs 13000 dollars
# A Toyota Prius costs 24000 dollars

"""
Output:
"""

"""
Consider the following scenario about using Python dictionaries:
Tessa and Rick are hosting a party. Together, they sent out invitations,
and collected the responses in a dictionary, with names of their friends
and the number of guests each friend will be bringing.

Complete the function so that the "check_guests" function retrieves the number of guests
(value) the specified friend "guest" (key) is bringing.
This function should:
1. accept a dictionary "guest_list" and a key "guest" variable passed through
the function parameters;
2. print the values associated with the key variable.
"""

def check_guests(guest_list, guest):
    return guest_list [guest] # Return the value for the given key

guest_list = { "Adam":3, "Camila":3, "David":5, "Jamal":3, "Charley":2, "Titus":1,
               "Raj":6, "Noemi": 1, "Sakira":3]

print (check_guests(guest_list, "Adam")) # Should print 3
print (check_guests(guest_list,"Sakira")) # Should print 3
print (check_guests(guest_list, "Charley")) # Should print 2

"""
Output:
3
3
2
"""

"""
Use a dictionary to count the frequency of numbers in the given "text" string.
Only numbers should be counted. Do not count blank spaces, letters, or punctuation.
Complete the function so that input like "1001000111101" will return a dictionary
that holds the count of each number that occurs in the string ('1': 7, '0': 6}.
This function should:
1. accept a string "text" variable through the function's parameters;
2. initialize an new dictionary;
3. iterate over each text character to check if the character is a number'
4. count the frequency of numbers in the input string, ignoring all other characters;
5. populate the new dictionary with the numbers as keys, ensuring each key is unique,
and assign the value for each key with the count of that number;
6. return the new dictionary.
"""

def count numbers(text):
    # Initialize a new dictionary.
    dictionary = {}
    # Complete the for loop to iterate through each "text" character.
    for x in text:
        # Complete the if-statement using a string method to check if the
        # character is a number.
    if x.isnumeric:
        # Complete the if-statement using a logical operator to check if
        # the number is not already in the dictionary.
        if x not in dictionary:
            # use a cictionary operation to a0d the number as a key
            # and set the anacaad count vacue to zero.
            dictionary [x] = 0
        dictionary [x] += 1
        # use a dictionary operation to increment the number count value
        # for the existing key.
        
    return dictionary

print count numbers 1001000111101"))
# Should be {'1': 7, '0': 6}
print(count_numbers ("Math is fun! 2+2=4"))
# Should be {'2': 2, '4': 1}
print (count_numbers ("This is a sentence."))
# Should be st
print (count_numbers ("55 North Center Drive"'))
# Should be {'5': 2}

"""
Output:
{'1': 7, '0': 6}
{'2': 2, '4': 1}
{}
{'5': 2}
"""
                      
"""
What do the following commands return when car_make = "Lamborghini"?
"""
                      
print (car_make [3:-5])
print(car_make [-4:1])
print(car_make [:7])

"""
Output: bor, hini, Lamborg
"""

"""
What does the list "music_genres contain after these commands are executed?
"""
                      
music_genres = ["rock", "pop", "country"]
music_genres. append("blues")

"""
Output: ['rock', 'pop', 'country', 'blues"]
"""

"""
What do the following commands return?
"""
                      
teacher_names = {"Math": "Aniyah Cook", "Science": "Ines Bisset", "Engineering": "Wayne Branon"}
teacher_names.values ()

"""
Output: dict_values([Aniyah Cook', 'Ines Bisset', 'Wayne Branon'])
"""

# Exam: Strings, Lists, Disctionaries

"""
Fill in the blank to complete the "first _character" function.
This function should return the first character of any string passed in.
Complete the string operation needed in this function so that input like "Hello, World"
will produce the output "H".
"""

def first_character(string):
    # Complete the return statement using a string operation.
    return string[0] 


print(first_character("Hello, World")) # Should print H
print(first_character("Python is awesome")) # Should print P
print(first_character("Keep going")) # Should print K

"""
Output:
H
P
K
"""

"""
Fill in the blank to complete the "string_words" function.
This function should split up the words in the given "string" and return the number of wordsin the "string".
Complete the string operation and method needed in this function so that a function call like
"string_ words("Hello, World"" will return the output "2".
"""

def string_words(string):
    # Complete the return statement using both a string operation and 
    # a string method in a single line.
    return len(string.split())


print(string_words("Hello, World")) # Should print 2
print(string_words("Python is awesome")) # Should print 3
print(string_words("Keep going")) # Should print 2
print(string_words("Have a nice day")) # Should print 4

"""
Output:
2
3
2
4
"""

"""
Consider the following scenario about using Python lists:
A professor gave his two assistants, Aniyah and Imani, the task of keeping an attendance list of students
in the order they arrived in the classroom. Aniyah was the first one to note which students arrived,
and then Imani took over. After class, they each entered their lists into the computer and emailed them
to the professor. The professor wants to combine the two lists into one and sort it in alphabetical order.

Complete the code by combining the two lists into one and then sorting the new list.
This function should:
1. accept two lists through the function's parameters;,
2. combine the two lists;
3. sort the combined list in alphabetical order;
4. return the new list.
"""

def alphabetize_lists(list1, list2):

    new_list = [] # Initialize a new list.
    combined_list = list1 + list2 # Combine the lists.
    combined_list.sort() # Sort the combined lists.
    new_list = combined_list # Assign the combined lists to the "new_list".

    return new_list 

Aniyahs_list = ["Jacomo", "Emma", "Uli", "Nia", "Imani"]
Imanis_list = ["Loik", "Gabriel", "Ahmed", "Soraya"]


print(alphabetize_lists(Aniyahs_list, Imanis_list))
# Should print: ['Ahmed', 'Emma', 'Gabriel', 'Imani', 'Jacomo', 'Loik', 'Nia', 'Soraya', 'Uli']

"""
Output:
['Ahmed', 'Emma', 'Gabriel', 'Imani', 'Jacomo', 'Loik', 'Nia', 'Soraya', 'Uli']
"""

"""
Fill in the blank to complete the "increments" function.
This function should use a list comprehension to create a list of numbers incremented by 2 (n+2).
The function receives two variables and should return a list of incremented consecutive numbers
between "start" and "end" inclusively (meaning the range should include both the "start" and "end" values).
Complete the list comprehension in this function so that input like "squares(2, 3)"
will produce the output "[4, 5]".
"""

def increments(start, end):
    return [ n+2 for n in range(start, end+1) ] # Create the required list comprehension.


print(increments(2, 3)) # Should print [4, 5]
print(increments(1, 5)) # Should print [3, 4, 5, 6, 7]
print(increments(0, 10)) # Should print [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]

"""
Output:
[4, 5]
[3, 4, 5, 6, 7]
[2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
"""

"""
Fill in the blanks to complete the "endangered _animals" function.
This function accepts a dictionary containing a list of endangered animals (keys)
and their remaining population (values). For each key in the given "animal_ dict" dictionary,
format a string to print the name of the animal, with one animal name per line.
"""

def endangered_animals(animal_dict):
    result = ""
    # Complete the for loop to iterate through the key and value items 
    # in the dictionary.    
    for key, value in animal_dict.items(): 
        # Use a string method to format the required string.
        result += "{}\n".format(key)
    return result


print(endangered_animals({"Javan Rhinoceros":60, "Vaquita":10, "Mountain Gorilla":200, "Tiger":500}))

# Should print:
# Javan Rhinoceros
# Vaquita
# Mountain Gorilla
# Tiger

"""
Output:
Javan Rhinoceros
Vaquita
Mountain Gorilla
Tiger
"""

"""
Consider the following scenario about using Python dictionaries:
Tessa and Rick are hosting a party. Both sent out invitations to their friends, and each one collected
responses into dictionaries, with names of their friends and how many guests each friend was bringing.
Each dictionary is a partial guest list, but Rick's guest list has more current intormation
about the number of guests.
Complete the function to combine both dictionaries into one, with each friend listed only once,
and the number of guests from Rick's dictionary taking precedence, if a name is included in both dictionaries.
Then print the resulting dictionary. This function should:
1. accept two dictionaries through the function's parameters;
2. combine both dictionaries into one, with each key listed only once;
3. the values from the "guests1" dictionary taking precedence, if a key is included in both dictionaries;
4. then print the new dictionary of combined items.
"""

def combine_guests(guests1, guests2):
    # Use a dictionary method to combine the dictionaries.
    guests2.update(guests1)

    return guests2

Ricks_guests = { "Adam":2, "Camila":3, "David":1, "Jamal":3, "Charley":2, "Titus":1, "Raj":4}
Tessas_guests = { "David":4, "Noemi":1, "Raj":2, "Adam":1, "Sakira":3, "Chidi":5}

print(combine_guests(Ricks_guests, Tessas_guests))
# Should print:
# {'David': 1, 'Noemi': 1, 'Raj': 4, 'Adam': 2, 'Sakira': 3, 'Chidi': 5, 'Camila': 3, 'Jamal': 3, 'Charley': 2, 'Titus': 1}

"""
Output:
{'David': 1, 'Noemi': 1, 'Raj': 4, 'Adam': 2, 'Sakira': 3, 'Chidi': 5, 'Camila': 3, 'Jamal': 3, 'Charley': 2, 'Titus': 1}
"""

"""
Complete the function so that input like "This is a sentence." will return a dictionary that holds
the count of each letter that occurs in the string: ['t': 2, 'h': 1, 'j': 2,
's': 3, 'a': 1, 'e': 3, 'n': 2, 'c': 1}. This function should:
1. accept a string "text" variable through the function's parameters;
2. iterate over each character the input string to count the frequency of each letter found,
(only letters should be counted, do not count blank spaces, numbers, or punctuation;
keep in mind that Python is case sensitive);
3. populate the new dictionary with the letters as keys, ensuring each key is unique,
and assign the value for each key with the count of that letter;
4. return the new dictionary.
"""

def count_letters(text):
    # Initialize a new dictionary.
    dictionary = {} 
    # Complete the for loop to iterate through each "text" character and 
    # use a string method to ensure all letters are lowercase.
    for x in text.lower():
        # Complete the if-statement using a string method to check if the
        # character is a letter.
        if x.isalpha():
            # Complete the if-statement using a logical operator to check if 
            # the letter is not already in the dictionary.
            if x not in dictionary:
                # Use a dictionary operation to add the letter as a key
                # and set the initial count value to zero.
                dictionary[x] = 0
            # Use a dictionary operation to increment the letter count value 
            # for the existing key.
            dictionary[x] += 1 
            # Increment the letter counter. 
    return dictionary

print(count_letters("AaBbCc"))
# Should be {'a': 2, 'b': 2, 'c': 2}

print(count_letters("Math is fun! 2+2=4"))
# Should be {'m': 1, 'a': 1, 't': 1, 'h': 1, 'i': 1, 's': 1, 'f': 1, 'u': 1, 'n': 1}

print(count_letters("This is a sentence."))
# Should be {'t': 2, 'h': 1, 'i': 2, 's': 3, 'a': 1, 'e': 3, 'n': 2, 'c': 1}

"""
Output:
{'a': 2, 'b': 2, 'c': 2}
{'m': 1, 'a': 1, 't': 1, 'h': 1, 'i': 1, 's': 1, 'f': 1, 'u': 1, 'n': 1}
{'t': 2, 'h': 1, 'i': 2, 's': 3, 'a': 1, 'e': 3, 'n': 2, 'c': 1}
"""

"""
What do the following commands return when car_make = "Lamborghini"?
"""
print(car_make[3:-5])
print(car_make[-4:])
print(car_make[:7])

# bor, hini, Lamborg

"""
What does the list "car _makes" contain after these commands are executed?
"""

car_makes = ["Ford", "Volkswagen", "Toyota"]
car_makes.remove("Ford")

# ['Volkswagen', 'Toyota']

"""
What do the following commands return?
"""

speed_limits = {"street": 35, "highway": 65, "school": 15}
speed_limits["highway"]

# 65

# Exam: Strings, Lists, Dictionaries

"""
Fill in the blank to complete the "even _numbers" function.
This function should use a list comprehension to create a list of even numbers using a conditional
if statement with the modulo operator to test for numbers evenly divisible by 2.
The function receives two variables and should return the list of even numbers that occur
between the "first" and "last" variables exclusively (meaning don't modify the default behavior
of the range to exclude the "end" value in the range). For example, even_numbers(2, 7) should return [2, 4, 6].
"""

def even_numbers(first, last):
    return [ n for n in range(first, last) if n % 2 == 0 ]


print(even_numbers(4, 14)) # Should print [4, 6, 8, 10, 12]
print(even_numbers(0, 9))  # Should print [0, 2, 4, 6, 8]
print(even_numbers(2, 7))  # Should print [2, 4, 6]

"""
Output:
[4, 6, 8, 10, 12]
[0, 2, 4, 6, 8]
[2, 4, 6]
"""

"""
What do the following commands return when genre="transcendental"?
"""

print(genre[:-8])
print(genre[-7:9])

# transc, nd

"""
What does the list "colors" contain after these commands are executed?
"""

colors = ["red", "white", "blue"]
colors.insert(2, "yellow")

# ['red', 'white', 'yellow', 'blue']
