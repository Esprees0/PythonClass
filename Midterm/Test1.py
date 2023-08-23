number1 = 4
number2 = 10
number3 = 11
number4 = -9

def numberSplit(num):
    return [num//2,num//2 + num%2]

print(numberSplit(4))
print(numberSplit(10))
print(numberSplit(11))
print(numberSplit(-9))

