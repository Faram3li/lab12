import random
import string

def generate_car_number():
    digits = ''.join(random.choices(string.digits, k=4))
    letters = ''.join(random.choices(string.ascii_uppercase, k=3))
    return f"{digits} {letters}"

def generate_multiple_car_numbers(n):
    return [generate_car_number() for _ in range(n)]

n = int(input("Введіть кількість номерів: "))

car_numbers = generate_multiple_car_numbers(n)

print("Згенеровані автомобільні номери:")
for number in car_numbers:
    print(number)
