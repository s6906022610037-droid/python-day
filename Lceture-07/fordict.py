phonebook = {'Anirach': '777-1111', 'Mickey':'777-2222','Donald':'777-3333'}
phonebook['Bart'] = [1,3,5]

elemants = len(phonebook)
print('There are', elemants, 'elements in the phonebook')

for key in phonebook:
    print(key, ":", phonebook[key])
    
phonebook['Bart'][1] =9
print(phonebook)