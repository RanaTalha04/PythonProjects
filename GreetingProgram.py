import time

timespan = time.strftime('%H:%M:%S')
print(timespan)
name = input("Enter your name: ")

hour = int(time.strftime('%H'))

if (hour > 4 and hour < 12):
    print("Good Morning,", name)
elif (hour > 12 and hour < 15):
    print("Good AfterNoon,", name)
elif (hour > 15 and hour < 18):
    print("Good Evening,", name)
else:
    print("Good Night,", name)
print("-------Welcome to KBC-------")
print("-----Kon Banega CrorePati-----")

question_answers = [['Who was the first prime minister of Pakistan?',
                     ['a) Liaqat Ali Khan', 'b) Muhammad Ali Jinnah',
                         'c) Ayub Khan', 'd) Zulfikar Ali Bhutto'],
                     'a'],
                    ['Who is the last prophet in Islam?',
                     ['a) Hazrat Muhammad (PBUH)', 'b) Hazrat Isa (AS)',
                      'c) Hazrat Musa (AS)', 'd) Hazrat Ibrahim (AS)'],
                     'a'],
                    ['What is the name of the last Holy Book?',
                     ['a) Torah', 'b) Bible', 'c) Quran', 'd) Psalms'],
                     'c'],
                    ['Who reigned over Pakistan from 2018-2022?',
                     ['a) Nawaz Sharif', 'b) Asif Ali Zardari',
                         'c) Imran Khan', 'd) Pervez Musharraf'],
                     'c'],
                    ['What is the national animal of Pakistan?',
                     ['a) Markhor', 'b) Snow Leopard',
                         'c) Himalayan Brown Bear', 'd) Indus Dolphin'],
                     'a']
                    ]

correct_answers = 0

for question_answer in question_answers:
    question = question_answer[0]
    options = question_answer[1]
    answer = question_answer[2]

    print("Question: ", question)

    for option in options:
        print(option)

    user_answer = input("Your Answer: ")

    if user_answer == answer:
        print("Correct!")
        correct_answers += 1
    else:
        print("Incorrect!")
        break

if correct_answers == len(question_answers):
    print("You won 7 crores")
else:
    print('Better luck next time')

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
