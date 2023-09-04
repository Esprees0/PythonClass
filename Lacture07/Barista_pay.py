#This program calculates the gross pay for
# each of Megan's baristas.

NUM_EMPLOYEES = 6

def main():
    #Create a list to hold employee hours.
    hours = [0] * NUM_EMPLOYEES

    for index in range(NUM_EMPLOYEES):
        print('Enter the hours worked by employess',\
              index + 1, ': ',sep=' ',end=' ')
        hours[index] = float(input())
    
    pay_rate = float((input('Enter the hourly pay rayte: ')))

    for index in range(NUM_EMPLOYEES):
        gross_pay = hours[index] * pay_rate
        print('Gross pay for employee ', index + 1, ': $', \
              format(gross_pay,',.2f'),sep='')
    
main() 