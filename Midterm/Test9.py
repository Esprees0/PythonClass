def isValidIP(String):
    splitstr = String.split(".")
    if splitstr.starwith(0):
        splitstr = splitstr -1
    return (len(splitstr)) == 4


print(isValidIP("1.2.3.4"))
print(isValidIP("1.2.3"))
print(isValidIP("1.2.3.4.5"))
print(isValidIP("123.45.78.90"))
print(isValidIP("123.045.067.089"))