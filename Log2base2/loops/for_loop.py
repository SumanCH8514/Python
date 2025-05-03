# Write a program to get a string S from the user and count the number of vowels present in the string. Finally, display the vowel count.

vowels = {'a', 'e', 'i', 'o', 'u'}
s = input("Enter a string: ")
# count = 0
# for char in s:
#     if char in vowels:
#         count += 1

# print(f"The number of vowels in the string is: {count}")

# -------------------OR----------------------

print("The number of vowels in the string is: ",sum(1 for char in s if char in vowels))
