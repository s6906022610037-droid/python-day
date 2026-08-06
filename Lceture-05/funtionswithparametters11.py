conter = 0

def increment():
    global conter
    conter += 11
    print(conter)

increment()
increment()

print(conter)