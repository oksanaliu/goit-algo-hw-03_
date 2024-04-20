import random

def get_numbers_ticket(min_num, max_num, quantity):
    
    if not (1 <= min_num <= max_num <= 50) or not (1 <= quantity <= max_num - min_num + 1):
        return []

    numbers = set()
    while len(numbers) < quantity:
        numbers.add(random.randint(min_num, max_num))

    return sorted(numbers)

min_num = 1
max_num = 49
quantity = 6
print(get_numbers_ticket(min_num, max_num, quantity))