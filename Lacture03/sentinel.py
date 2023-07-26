keep_going = 'y'

while keep_going == 'y':
    Item = float(input("Enter the item's wholesale cost:"))
    retailprice = Item * 2.5
    print('Retail price $', \
    format(retailprice,',.2f'),'.', sep='')

    keep_going = input('Do you have another item' + \
                       '(Enter y for yes):')
