First_name = str(input('Enter your first name:'))
Last_name = str(input('Enter your last name:'))
ID_num = str(input('Enter your student ID number:'))
print('Your system login name is \n',(((First_name)[:3]+(Last_name)[:3]+(ID_num)[-3:])))