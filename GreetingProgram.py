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
