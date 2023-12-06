# # Calculator
# a = 100  # Number 1
# b = 2  # Number 2

# add = a + b  # Additon
# sub = a - b  # Subtraction
# mult = a * b  # Multiplicaion
# div = a / b  # Division

# # Printing the results
# print("The sum of two numbers", a, "and", b, "is:", add)
# print("The difference of two numbers", a, "and", b, "is:", sub)
# print("The product of two numbers", a, "and", b, "is:", mult)
# print("The quotient by dividing two numbers", a, "and", b, "is:", div)


# Another Calculator using conditional Statement

num1 = int(input("Enter a number: "))
num2 = int(input("Enter another number: "))

print("Press 1 for Addition: ")
print("Press 2 for Subtraction: ")
print("Press 3 for Multiplication: ")
print("Press 4 for Division: ")
print("Press 5 for Modulus: ")
print("Press 6 for Exponential: ")
print("Press 7 for Floor Division: ")

add = num1+num2
sub = num1 - num2
mult = num1 * num2
div = num1 / num2
mod = num1 % num2
exp = num1 ** num2
fd = num1 // num2

choice = int(input("Enter a number for operation: "))

if (choice == 1):
    print("The sum of two numbers", num1, "and", num2, "is:", add)
elif(choice==2):
    print("The difference of two numbers", num1, "and", num2, "is:", sub)
elif(choice==3):
    print("The Multiplication of two numbers", num1, "and", num2, "is:", mult)
elif(choice==4):
    print("The Division of two numbers", num1, "and", num2, "is:", div)
elif(choice==5):
    print("The Modulus of two numbers", num1, "and", num2, "is:", mod)
elif(choice==6):
    print("The Exponential of two numbers", num1, "and", num2, "is:", exp)
elif(choice==7):
    print("The Floor Division of two numbers", num1, "and", num2, "is:", fd)
else:
    exit()


