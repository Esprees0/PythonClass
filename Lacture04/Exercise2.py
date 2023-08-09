In_str = str(input("Enter a string:"))
print("This is what I found about that string")

if (In_str.isalnum()) == True:
    print("The string is alphanumeric.")   

if (In_str.isalpha()) == True:
    print("The string contains only alphabetic characters")

if (In_str.islower()) == True:
    print("The letters in the string are all lowercase")

if (In_str.isnumeric()) == True:
    print("The string contains only digits.")

if (In_str.isspace()) == True:
    print("The string contains only whitespace")

if (In_str.istitle()) == True:
    print("The string is in title case")
    
if (In_str.isupper()) == True:
    print("The letters in the string are all Uppercase")
