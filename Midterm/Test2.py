# def highestDigit(num):
    
#     # for i in (num):
#     #     print(i)
#     # return 

# print(highestDigit(3790))
# print(highestDigit(2))
# print(highestDigit(377401))

def highest_digit(num):
    max_digit = -1
    print("Maxeie",max_digit)
    while num > 0:
        digit = num % 10
        print("modul",digit)
        max_digit = max(max_digit, digit)
        num //= 10
        print("Max",max_digit)
    return max_digit

# Example usage
# num = 87465
# result = highest_digit(num)
# print(f"The highest digit in {num} is: {result}")

print(highest_digit(3790))
print(highest_digit(2))
print(highest_digit(377401))

