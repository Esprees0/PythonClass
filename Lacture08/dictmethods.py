phonebook = {'Anirach': ' 777-111', 'Mickey': '777-222',
             'Donald': '777-333','Pluto': '777-444'}

herosdict = {}
herosdict['Hulk'] = '888-111'
herosdict['Iron Man'] = '888-222'
print(herosdict.get('Halk', 'Key not found'))
print(herosdict.get('Hulk', 'Key not found'))

for key, value in phonebook.items():
     print(key,value)

print(phonebook.keys())
print(phonebook.values())

print(phonebook.pop('Mick', 'Element not foud'))
print(phonebook.pop('Mickey', 'Element not found'))
print(phonebook)
print(phonebook.popitem())
print(phonebook)
phonebook.clear()
print('After clear')
print(phonebook)