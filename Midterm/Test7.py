def simplePair(*argv):
    ([x,y,z],N) = [*argv]
    if x * y == N:
        return ([x,y])
    elif x * z == N:
        return ([x,z])
    elif y * z == N:
        return ([y,z])
    else:
        return ("null")

print(simplePair([1,2,3],3))
print(simplePair([1,2,3],6))
print(simplePair([1,2,3],9))
print(simplePair([4,3,3],9))
print(simplePair([4,3,3],12))

