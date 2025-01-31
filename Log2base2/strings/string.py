# taking input as string and printing normally
str = "Python"
print(str)

# printing string object using for loop
str1 = " is great"
for i in str1:
    print(i)

# checking if char exist in string or not
key = input("Find any char in str: ")
if key in str:
    print(key," found in ",str)
else:
    print(key," not found in ",str)
