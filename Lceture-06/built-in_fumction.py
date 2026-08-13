number = [4,2,9,1,5,6]

length = len(number)
print(f"Length of the list: {length}")

total_sum= sum(number)
print(f"Sum of all elements: {total_sum}")

max_value = max(number)
print(f"Maximum value in the list: {max_value}")

min_value = min(number)
print(f"Minimum value in the list: {min_value}")

sorted_numbers = sorted(number)
print(f"Sorted list: {sorted_numbers}")

# 6. any(): Check if any element in the list is True
bool_list = [False, True, False]
any_true = any(bool_list)
print(f"Is any element True? {any_true}") # Output: Is any
# element True? True

# 7. all(): Check if all elements in the list are True
all_true = all(bool_list)
print(f"Are all elements True? {all_true}") # Output: Are all
# elements True? False

# 8. list(): Convert an iterable to a list (if not already a list)
string = "hello"
char_list = list(string)
print(f"List of characters: {char_list}") # Output: List of
# characters: ['h', 'e', 'l', 'l', 'o']

# 9. reversed(): Return a reverse iterator of the list
reversed_numbers = list(reversed(number))
print(f"Reversed list: {reversed_numbers}") # Output: Reversed
# list: [6, 5, 1, 9, 2, 4]

# 10. enumerate(): Return an iterator of tuples containing index
# and value
enumerated_numbers = list(enumerate(number))
print(f"Enumerated list: {enumerated_numbers}")
# Output: Enumerated list: [(0, 4), (1, 2), (2, 9), (3, 1), (4,
# 5), (5, 6)]