def main():
    outfile = open('number.txt','w')
    num1 = int(input('Enther a number: '))
    num2 = int(input('Enther another number: '))
    num3 = int(input('Enther another number: '))

    outfile.write(str(num1) + '\n')
    outfile.write(str(num2) + '\n')
    outfile.write(str(num3) + '\n')
 
    outfile.close()
    print('Data written to numbers.txt')

main()