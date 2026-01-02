import random

def get_numbers_ticket(min, max, quantity):
    if min < 1 or max > 1000:
        return []
    
    result = random.sample(range(min, max), quantity)
    result.sort()
    return result

print(get_numbers_ticket(1, 49, 6))