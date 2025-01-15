# grade = int(input("Enter your Marks: "))
# if grade >= 90:
#     print("A+")
# elif grade >= 80:
#      print("A")
# elif grade >= 70:
#     print("B")
# elif grade >= 50:
#     print("C")
# elif grade >=40:
#     print("D")
# else:
#     print("F")

print("Tax Calculator")
print("0% tax if sal <2.5lac, 20% tax if sal > 2.5lac")
sal = float(input("Your salary: "))
notax = 250000
tax = sal * (0,0.2) [sal< notax]
print("Taxable ammount is: ",tax-notax)