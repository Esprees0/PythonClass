# This program writes three lines of data
# to a  file.
def main():
    # Open a file named philosophers.txt.
    outfile = open('philosophers.txt','w')

    # Write the names of three philophers
    # to the file.
    outfile.write('John Lock\n')
    outfile.write('David Hume\n')
    outfile.write('Edmund Burke\n')

    # Close the file
    outfile.close()

# Call the main fuction
main()