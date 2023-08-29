
"""
Python Collections (Arrays):
----------------------------
There are four collection data types in the Python programming language:

-List is a collection which is ordered and changeable. Allows duplicate members.
-Tuple is a collection which is ordered and unchangeable. Allows duplicate members.
-Set is a collection which is unordered, unchangeable*, and unindexed. No duplicate members.
-Dictionary is a collection which is ordered** and changeable. No duplicate members.

*Set items are unchangeable, but you can remove and/or add items whenever you like.

Set:
----
A set is used when you want to store a bunch of elements and be certain that there are only present once.

Dictionaries:
-------------
Tha data inside take the form of pairs of keys and values.
They are used to organize elements into collections.
Can include one or more keys, with one or more values associated with each key.

Ordered or Unordered?
---------------------
From Python version 3.7, dictionaries are ordered. In Python 3.6 and earlier, dictionaries are unordered.
When we say that dictionaries are ordered, it means that the items have a defined order, and that order will not change.
Unordered means that the items does not have a defined order, you cannot refer to an item by using an index.

Operations:
-----------
len(dictionary) - Returns the number of items in a dictionary.

for key, in dictionary - Iterates over each key in a dictionary.

for key, value in dictionary.items() - Iterates over each key,value pair in a dictionary.

if key in dictionary - Checks whether a key is in a dictionary.

dictionary[key] - Accesses a value using the associated key from a dictionary.

dictionary[key] = value - Sets a value associated with a key.

del dictionary[key] - Removes a value using the associated key from a dictionary.


Methods:
--------
dictionary.get(key, default) - Returns the value corresponding to a key, or the default value if the specified key is not present.

dictionary.keys() - Returns a sequence containing the keys in a dictionary.

dictionary.values() - Returns a sequence containing the values in a dictionary.

dictionary[key].append(value) - Appends a new value for an existing key.

dictionary.update(other_dictionary) - Updates a dictionary with the items from another dictionary. Existing entries are updated; new entries are added.

dictionary.clear() - Deletes all items from a dictionary.

dictionary.copy() - Makes a copy of a dictionary.

Examples:
"""

file_counts = {"jpeg":10, "txt":14, "csv":2, "py":23}
print(file_counts)

# Output: {"jpeg":10, "txt":14, "csv":2, "py":23}

"""
Say you want to find out how many text files there are in the dictionary.
"""

File_counts ["txt"]
# Output: 14

"""
You can also use the in keyword to check if a key is contained in a dictionary.
"""

"jpg" in file_counts
# Output: True

"html" in file_counts
# Output: False

pet_dictionary = {"dogs": ["Yorkie", "Collie", "Bulldog"], "cats": ["Persian", "Scottish Fold", "Siberian"], "rabbits": ["Angora", "Holland Lop", "Harlequin"]}

print(pet_dictionary.get("dogs", 0))
# Should print ['Yorkie', 'Collie', 'Bulldog']

"""
Dictionaries are mutable. It means we can add remove and replace entries.
"""

file_counts ["cfg"] = 8
print(file_counts)
# Output: {"jpeg":10, "txt":14, "csv":2, "py":23, "cfg":8}

file_counts["csv"] = 17
print(file_counts)
# Output: {"jpeg":10, "txt":14, "csv":17, "py":23, "cfg": 8}

del file_counts["cfg"]
print(file_counts)
# Output: {"jpeg":10, "txt":14, "csv":2, "py":23}

"""
Like with strings lists and tuples,you can use for loops to iterate through the contents of a dictionary.
If you use a dictionary in a for loop, the iteration variable will go through the keys in the dictionary.
"""

file_counts = {"jpg":10, "txt":14, "csv":2, "py":23}
for extension in file_counts:
	print extension
"""
# Output:
jpg
txt
csv
py
"""

"""
It's easier and faster to search for an element in a dictionary than a list.

If you want to access the associated values, you can either use the keys as indexes of the dictionary
or you can use the items method which returns a tuple for each element in the dictionary.

The tuple's first element is the key. Its second element is the value.

Example:
"""

for ext, amount in file_counts.items():
	print("there are and then {} files with the .{} extension".format(amount, ext))
"""
# Output:
There are 10 files with the .jpg extension
There are 14 files with the .txt extension
There are 2 files with the .csv extension
There are 23 files with the .py extension
"""

"""
Sometimes you might just be interested in the keys of a dictionary.
Other times you might just want the values.
You can access both with their corresponding dictionary methods like this.
"""

file_counts.keys()
# Output: dict_keys(['jpg', 'txt', 'csv', 'py'])

file_counts.values()
# Output: dict_values([10, 14, 2, 23])

"""
You just need to iterate them as you would with any sequence.
"""

for value in file_counts.values():
	print value
"""
# Output:
10
14
2
23
"""

"""
Therefore, we can use items to get key value pairs, keys to get the keys, and values to get just the values.

Example:

Complete the code to iterate through the keys and values of the cool_beasts dictionary.
Remember that the items method returns a tuple of key, value for each element in the dictionary.
"""

cool_beasts = {"octopuses":"tentacles", "dolphins":"fins", "rhinos":"horns"}
for key, value in cool_beasts.items():
    print("{} have {}".format(key, value))
"""
# Output:
octopuses have tentacles
dolphins have fins
rhinos have horns
"""

"""
We know that each key can be present only once, so dictionaries are a great tool for counting elements and analyzing frequency.

Example: check out a simple example of counting how many times each letter appears in a piece of text.

In this code, we're first initializing an empty dictionary, then going through each letter in the given string.
For each letter, we check if it's not already in the dictionary.
And in that case, we initialize an entry in the dictionary with a value of zero.
Finally, we increment the count for that letter in the dictionary.
To sum up, we've created a dictionary where the keys are
each of the letters present in the string and the values are how many times each letter is present.
"""

def count_letter(text):
	result = {}
	for letter in text:
		if letter not in result:
			result[letter] = 0
		result[letter] += 1
	return result

count_letters("aaaaa")
# Output: {'a': 5}

count_letters("tenant")
# Output:
{'t': 2, 'e': 1, 'n': 2, 'a': 1}

count_letters("a long string with a lot of letters")
# Output:
{'a': 2, ' ': 7, 'l': 3, 'o': 3, 'n': 2, 'g': 2, 's': 2, 't': 5, 'r': 2, 'i': 2, 'w': 1, 'h': 1, 'f': 1, 'e': 2}

"""
Iterate over the key and value pairs of a dictionary using a for loop with the dictionary.items() method
to calculate the sum of the values in a dictionary.

# This function returns the total time, with minutes represented as
# decimals (example: 1 hour 30 minutes = 1.5), for all end user time
# spent accessing a server in a given day.
"""

def sum_server_use_time(Server):

    # Initialize the variable as a float data type, which will be used
    # to hold the sum of the total hours and minutes of server usage by
    # end users in a day.
    total_use_time = 0.0

    # Iterate through the "Server" dictionary’s key and value items
    # using a for loop.
    for key,value in Server.items():

        # For each end user key, add the associated time value to the
        # total sum of all end user use time.
        total_use_time += Server[key]

    # Round the return value and limit to 2 decimal places.
    return round(total_use_time, 2)

FileServer = {"EndUser1": 2.25, "EndUser2": 4.5, "EndUser3": 1, "EndUser4": 3.75, "EndUser5": 0.6, "EndUser6": 8}

print(sum_server_use_time(FileServer)) # Should print 20.1

"""
Concatenate a value, a string, and the key for each item in the dictionary and append to the end of a new list[ ] using the list.append(x) method.

Iterate over keys with multiple values from a dictionary using nested for loops with the dictionary.items() method.

# This function receives a dictionary, which contains common employee
# last names as keys, and a list of employee first names as values.
# The function generates a new list that contains each employees’ full
# name (First_name Last_Name). For example, the key "Garcia" with the
# values ["Maria", "Hugo", "Lucia"] should be converted to a list
# that contains ["Maria Garcia", "Hugo Garcia", "Lucia Garcia"].
"""

def list_full_names(employee_dictionary):
    # Initialize the "full_names" variable as a list data type using
    # empty [] square brackets.
    full_names = []

    # The outer for loop iterates through each "last_name" key and
    # associated "first_name" values, in the "employee_dictionary" items.
    for last_name, first_names in employee_dictionary.items():

        # The inner for loop iterates over each "first_name" value in
        # the list of "first_names" for one "last_name" key at a time.
        for first_name in first_names:

            # Append the new "full_names" list with the "first_name" value
            # concatenated with a space " ", and the key "last_name".
            full_names.append(first_name+" "+last_name)

    # Return the new "full_names" list once the outer for loop has
    # completed all iterations.
    return(full_names)


print(list_full_names({"Ali": ["Muhammad", "Amir", "Malik"], "Devi": ["Ram", "Amaira"], "Chen": ["Feng", "Li"]}))
# Should print ['Muhammad Ali', 'Amir Ali', 'Malik Ali', 'Ram Devi', 'Amaira Devi', 'Feng Chen', 'Li Chen']

"""
Use the dictionary[key] = value operation to associate a value with a key in a dictionary.

Iterate over keys with multiple values from a dictionary, using nested for loops and an if-statement, and the dictionary.items() method.

Use the dictionary[key].append(value) method to add the key, a string, and the key for each item in the dictionary.

# This function receives a dictionary, which contains resource
# categories (keys) with a list of available resources (values) for a
# company’s IT Department. The resources belong to multiple categories.
# The function should reverse the keys and values to show which
# categories (values) each resource (key) belongs to.
"""

def invert_resource_dict(resource_dictionary):
  # Initialize a "new_dictionary" variable as a dict data type using
  # empty {} curly brackets.
    new_dictionary = {}
    # The outer for loop iterates through each "resource_group" and
    # associated "resources" in the "resource_dictionary" items.
    for resource_group, resources in resource_dictionary.items():
        # The inner for loop iterates over each "resource" value in
        # the list of "resources" for one "resource_group" key at a time.
        for resource in resources:
            # The if-statement checks if the current "resource" value has
            # been appended as a key to the "new_dictionary" yet.
            if resource in new_dictionary:
                # If True, then append the "resource_group" as a value to the
                # "resource", which is now the key.
                new_dictionary[resource].append(resource_group)
            # If False (else), then add the "resource" as a new key with the
            # "resource_group" as a value for that key.
            else:
                new_dictionary[resource] = [resource_group]
    # Return the new dictionary once the outer for loop has completed
    # all iterations.
    return(new_dictionary)


print(invert_resource_dict({"Hard Drives": ["IDE HDDs", "SCSI HDDs"],
        "PC Parts":  ["IDE HDDs", "SCSI HDDs", "High-end video cards", "Basic video cards"], "Video Cards": ["High-end video cards", "Basic video cards"]}))
# Should print {'IDE HDDs': ['Hard Drives', 'PC Parts'], 'SCSI HDDs': ['Hard Drives', 'PC Parts'], 'High-end video cards': ['PC Parts', 'Video Cards'], 'Basic video cards': ['PC Parts', 'Video Cards']}
