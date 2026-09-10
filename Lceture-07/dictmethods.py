phonebook = {'Anirach': '777-1111', 'Mickey':'777-2222',
             'Donald':'777-3333','Pluto':'777-4444'}

heroeesdict = {} 
heroeesdict['Hulk'] = 'Bruce Wayne'
heroeesdict['Iron man'] = 'Clark Kent'
print(heroeesdict.get('Hulk', 'Key not found'))
print(heroeesdict.get('Hulk', 'Key not found'))

for key, value in heroeesdict.items():
    print(key, ":", value) 
    
print(phonebook.keys())
print(phonebook.values())

print(phonebook.pop('Mickey', 'Key not found'))
print(phonebook.pop('Hulk', 'Key not found')) 
print(phonebook)
print(phonebook.popitem())
print(phonebook)
phonebook.clear()
print('After clear:')
print(phonebook) 