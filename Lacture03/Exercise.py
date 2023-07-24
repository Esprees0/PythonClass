print('KPH \t MPH')
print("=============")
for kph in range(60,140,10):
    mph = float(kph*(0.6214))
    print(kph, '\t' ,format(mph,'.1f'))

print('______________')