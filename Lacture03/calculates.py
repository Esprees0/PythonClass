# This program calculates  sales commissions.
    # Create  a variable to cantrol the loop.
keep_going = 'y'

# Calculate a series of comissions.
while keep_going == 'y':
    # Get a salesperson's sales and commission rate.
    sales = float(input('Enter the amount of sales:'))
    comn_rate = float(input('Enter the amount of sales'))

    # Calculate the comission.
    commission = sales * comn_rate

    # Display the comission.
    print('The commission is $', \
    format(commission, ',.2f'), sep='')

    # See if  the user wants to do another one.
    keep_going = input('Do you want to calculate another' + \
                       'commission (Enter y for yes:)')