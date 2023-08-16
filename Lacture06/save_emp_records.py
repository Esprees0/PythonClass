def main():
    num_enps = int(input('How many employee records ' + \
                         'do you want to create? '))
    
    emp_file = open('employees.txt', 'w')
    for count in range(1,num_enps + 1):
        print('Enter data for employee #',count,sep='')
        name = input('Name: ')
        id_num = input('ID number:')
        dept = input('Departmant:')

        emp_file.write(name + '\n')
        emp_file.write(id_num + '\n')
        emp_file.write(dept + '\n')

        print()

    emp_file.close()
    print('Employee records written to employees.txt')
    
main()