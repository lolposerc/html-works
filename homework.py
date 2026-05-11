def filter_even(numbers):
    result = []
    for number in numbers:
        if number % 2 == 0:
            result.append(number)
    
    return result

def filter_odd(numbers):
    result = []
    for number in numbers:
        if number % 2 != 0:
            result.append(number)
    
    return result

def filter_prime(numbers):
    result = []
    for number in numbers:
        prime = False
        count = 0
        if number > 0:
            for num in range(1,number+1):
                if number / num == int(number / num):
                    count += 1
                    if count > 2:
                        break
        if count == 2:
            prime = True
        
        if prime == True:
            result.append(num)
    return result

def filter_by_range(numbers, start, end):
    result = []
    for number in numbers:
        if start <= number and end >= number:
            result.append(number)
    return result

def filter_by_condition(numbers, condition_func):
    result = []
    for number in numbers:
        if condition_func(number):
            result.append(number)
    return result

def calculate_statistics(numbers):
    if not numbers:
        return {
            'min': None,
            'max': None,
            'average': None,
            'sum': 0,
            'unique_count': 0
        }

    unique_numbers = set(numbers)
    return {
        'min': min(numbers),
        'max': max(numbers),
        'average': sum(numbers) / len(numbers),
        'sum': sum(numbers),
        'unique_count': len(unique_numbers)
    }

numbers = [12, 7, 23, 4, 19, 8, 11, 15]

print("Четные:", filter_even(numbers))
print("Простые:", filter_prime(numbers))
print("В диапазоне 10-20:", filter_by_range(numbers, 10, 20))
