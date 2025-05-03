# Create a Python program that finds the second smallest number in a list of positive integers (including zero). The program should prompt the user to input a list of numbers, then compute and print the second smallest number in that list.

n = list(map(int, input().split()))
n.sort()
print(n[1])


