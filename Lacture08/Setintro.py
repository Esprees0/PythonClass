setA = {1,2,3,4}
setB = set([8,9,10])

setA.add(5)
setB.update([6,7])
Uset = setA | setB
print(Uset)
print(len(Uset))
print('  ')

setB.update('ABCD')
setA.update([6,7,8])
print(setB)
print('  ')

print(setA.intersection(setB))
print(setA ^ setB)
print('  ')

setB.remove('B')
setB.discard(10)
print(setB)
print(setA.clear())
for val in Uset:
    print(val)