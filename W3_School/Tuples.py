# Tuple
# Tuples are used to store multiple items in a single variable.

# Tuple is one of 4 built-in data types in Python used to store collections of data, the other 3 are List, Set, and Dictionary, all with different qualities and usage.

# A tuple is a collection which is ordered and unchangeable.

# Tuples are written with round brackets.
# thistuple = ("apple", "banana", "cherry")
# print(thistuple)

# Tuple Items
# Tuple items are ordered, unchangeable, and allow duplicate values.

# Tuple items are indexed, the first item has index [0], the second item has index [1] etc.

# Ordered
# When we say that tuples are ordered, it means that the items have a defined order, and that order will not change.

# Unchangeable
# Tuples are unchangeable, meaning that we cannot change, add or remove items after the tuple has been created.

# Allow Duplicates
# Since tuples are indexed, they can have items with the same value:
# thistuple = ("apple", "banana", "cherry", "apple", "cherry")
# print(thistuple)

# Tuple Length
# To determine how many items a tuple has, use the len() function:
# Example
# Print the number of items in the tuple:
# thistuple = ("apple", "banana", "cherry")
# print(len(thistuple))

# Create Tuple With One Item
# To create a tuple with only one item, you have to add a comma after the item, otherwise Python will not recognize it as a tuple.
# Example
# One item tuple, remember the comma:
# thistuple = ("apple",)
# print(type(thistuple))
# #NOT a tuple
# thistuple = ("apple")
# print(type(thistuple))

# Check if Item Exists
# To determine if a specified item is present in a tuple use the in keyword:
# Example
# Check if "apple" is present in the tuple:
# thistuple = ("apple", "banana", "cherry")
# if "apple" in thistuple:
#   print("Yes, 'apple' is in the fruits tuple")

# Change Tuple Values
# Once a tuple is created, you cannot change its values. Tuples are unchangeable, or immutable as it also is called.
# But there is a workaround. You can convert the tuple into a list, change the list, and convert the list back into a tuple.
# Example:
# Convert the tuple into a list to be able to change it:

# x = ("apple", "banana", "cherry")
# y = list(x)
# y[1] = "kiwi"
# x = tuple(y)
# print(x)

# Add tuple to a tuple.
# You are allowed to add tuples to tuples, so if you want to add one item, (or many), create a new tuple with the item(s), and add it to the existing tuple:
# Example
# Create a new tuple with the value "orange", and add that tuple:
thistuple = ("apple", "banana", "cherry")
y = ("orange",)
thistuple += y

print(thistuple)