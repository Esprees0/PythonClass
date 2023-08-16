# def main():
#     emp_file = open('employees.txt','r')
#     for txt in emp_file:
#         line1 = emp_file.readline()
#         line2 = emp_file.readline()
#         line3 = emp_file.readline()
#         line1 = line1.strip('\n')
#         line2 = line2.strip('\n')
#         line3 = line3.strip('\n')   
#         print('Name: '+ line1)
#         print('ID: ' + line2)
#         print('Dept: ' + line3)
#     emp_file.close()
# main()

def main():
    emp_file = open('employees.txt','r')
    Bat = emp_file.readline()
    while Bat != '':
        print('Name: ' )
        name = emp_file.readline()
        ID = emp_file.readline()
        dept = emp_file.readline()

        print('Name' + name)
        print('ID_card'+ ID)
        print('Dept' + dept)
        Bat = emp_file.readline()
    emp_file.close()
main()