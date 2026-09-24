from functools import reduce 

numbers = [1,2,3,4,5]
sun_of_numbers = reduce(lambda x,y : x+y , numbers)
print(sun_of_numbers)