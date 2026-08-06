def calculate_state(nambers):
    total_sum = sum (nambers)
    average = total_sum / len(nambers)
    maximum = max(nambers)
    minimum = min(nambers)
    return total_sum, average, maximum, minimum

numbers = [5, 10, 15, 20, 25]
total, avg, max_value, min_value = calculate_state(numbers)

print(f"Total: {total}")
print(f"Average: {avg}")
print(f"Maximum: {max_value}")
print(f"Minimum: {min_value}")