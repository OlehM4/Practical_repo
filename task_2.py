import random

def get_numbers_ticket(min, max, quantity):
    if min < 1 or max > 1000:
        return []
    try:
        result = random.sample(range(min, max), quantity)
    except ValueError:
        return 'Sample larger than population or is negative'
    result.sort()
    return result

print(get_numbers_ticket(10, 4, 5))