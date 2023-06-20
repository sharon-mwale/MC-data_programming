def average(numbers):
    if len(numbers) == 0:
        return 0  # Avoid division by zero error for an empty list
    total = sum(numbers)
    count = len(numbers)
    average_value = total / count
    return average_value


numbers = [5, 10, 15, 20]
result = average(numbers)
print(result)  

