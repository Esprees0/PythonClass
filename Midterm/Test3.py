# def capToFront(string):
#     checkstring = string.split()
#     for checkstring in len(capToFront(string)):
#         if few == fe:
#             tewf 

# print(capToFront("hApPy"))
# print(capToFront("moveMENT"))
# print(capToFront("shOrtCA"))
# def capToFront(word):
#     return ''.join(sorted(word, key=str.islower))

# # Example usage
# print(capToFront("hApPy"))
# print(capToFront("moveMENT"))
# print(capToFront("shOrtCAKE"))
# new_word = move_capitals_front(word)
# print(f"Original word: {word}")
# print(f"Modified word: {new_word}")

def capToFront(word):
    capital_letters = ""
    non_capital_letters = ""

    for char in word:
        if char.isupper():
            capital_letters += char
        else:
            non_capital_letters += char

    return capital_letters + non_capital_letters

print(capToFront("hApPy"))
print(capToFront("moveMENT"))
print(capToFront("shOrtCAKE"))