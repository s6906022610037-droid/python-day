animals = ["cat", "dog", "rabbit", "hamster", "dog", "parrot"]
# Find the index of the first occurrence of "dog"
first_dog_index = animals.index("dog")
print(f"The first occurrence of 'dog' is at index: {first_dog_index}")
#Output: The first occurrence of 'dog' is at index: 1

#Using index() to find the second occurrence of "dog" by specifying a starting index
second_dog_index = animals.index("dog", first_dog_index + 1)
print(f"The second occurrence of 'dog' is at index: {second_dog_index}")
#Output: The second occurrence of 'dog' is at index: 4