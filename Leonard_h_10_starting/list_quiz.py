#Andrew Leonard
# list_quiz.py -> h10-3
#

# Give short one-question quiz on HTT10 (Lists) to user
answerOptions  = ['A', 'B', 'C']
print("Which of the following statement about lists is NOT true?")
print('''A. Lists can only contain a single type of data within each list
B. you can check if an item is contained in a list with the in or not in operator 
C. Lists are Mutable
''')
userAnswer = input("Please enter the letter of the statement you think is NOT true: ")

answer = userAnswer.upper()[0]

if answer == 'A':
    print('\n You picked the correct answer! List can contain more than one type of data')
elif answer not in answerOptions:
    print("you did not select a valid answer")
else:
    print('\nSorry, that is incorrect, the correct answer was A.')