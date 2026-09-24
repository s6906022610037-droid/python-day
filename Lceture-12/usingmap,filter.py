from functools import reduce
 
numbers = [1,2,3,4,5]
squared_numbers = map(lambda x: x ** 2  , numbers)

even_squared_numbers = filter(lambda x: x % 2 == 0, squared_numbers )

sum_of_even_squared_number = reduce(lambda x,y : x+y ,even_squared_numbers)
print(sum_of_even_squared_number)