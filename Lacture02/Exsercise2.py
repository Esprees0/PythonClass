Hours_worked = int(input('Enter the number of hours worked:'))
Pay_rate = float(input('Enter the hourly pay rate :'))

if Hours_worked > 40:
    grosspay =  (40*20)+(((Hours_worked-40)*20)*1.5)
    # Gross = 40*Pay_rate
    # Overtime =  ((Hours_worked-40)*20)*1.5
    # GrossOT = Gross + Overtime   
    print('The gross pay is $',format(grosspay,'2f'))
else :
    Grosspay = Hours_worked*Pay_rate
    print('The gross pay is $',format(Grosspay,'.2f'))
 