def is_prime(number):
    if number < 2:
        return False
    for i in range(2, number):
        if number % i == 0:
            return False
    return True


def get_prime_numbers(numbers):
    prime_list = []  
    for num in numbers:
        if is_prime(num):  
            prime_list.append(num)
    return prime_list


numbers = [1, 4, 6, 7, 13, 9, 67]
result = get_prime_numbers(numbers)
print(result)  
