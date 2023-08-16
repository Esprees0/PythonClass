# This program reads and displays the contents
# of the philosophers.txt file.
def main():
    # Opena file named philosophers.txt
    infile = open('philosophers.txt','r')

    # Read the file's contents.
    file_contents = infile.read()

    # Close the file.
    infile.close()

    # Print the data that was read intio
    # memory.
    print(file_contents)   

main() 