phonebook = {'Anirach': '777-111','Mickey':'777-222','Donald':'777-333'}

print(phonebook)

print(phonebook['Mickey'])
print(phonebook.get('Donald'))

key = 'Pluto'
if key in phonebook:
    print(phonebook['Pluto'])
else:
    print(key + ' not in phonebook')

phonebook['Simpson']