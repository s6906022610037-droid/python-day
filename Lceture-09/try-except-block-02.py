filename = input('Enter the filename: ')
try: 
    infile = open(filename, 'r')
    contents = infile.read() 
    print(contents)
    infile.close()
except IOError as e:
    print('An Error occurred trying to read')
    print('the file', filename)
          
print("End program")
    