def main():
    emp_file = open('employees.txt','r')
    for line in emp_file:
        amount = float(line)
        
    
    emp_file.close()
main()