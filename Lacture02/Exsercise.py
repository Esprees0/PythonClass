First_score = int(input('Enter the score for test 1: '))
Second_score = int(input('Enter the score for test 2: '))
Third_score = int(input('Enter the score for test 3: '))

num_sore = [First_score,Second_score,Third_score]
average_sore = sum(num_sore)/len(num_sore)
print('The average score is',format(average_sore,'.2f'))
if average_sore > 95:
        print('Congratulations!')
        print('That is a great average!')
elif average_sore < 50:
        print("It's too less")
    
# Sore_average = ((First_score+Second_score+Third_score)/3)
# print(Sore_average)
# print('The average score is',format(Sore_average,'.2f'))
# if Sore_average > 95:
#         print('Congratulations!')
#         print('That is a great average!')