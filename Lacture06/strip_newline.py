def main():
    infile = open('philosophers.txt','r')
    line1 = infile.readline()
    line2 = infile.readline()
    line3 = infile.readline()
    
    line1 = line1.strip('\n')
    line2 = line2.strip('\n')
    line3 = line3.strip('\n')

    infile.close()

    print('eie'+line1)
    print('oo'+line2)
    print('pp' +line3)

main()