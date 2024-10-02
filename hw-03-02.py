import random


def get_numbers_ticket(min, max, quantity):
    
    # Перевіряємо, чи вірні передані значення
    if not (1 <= min < max <= 1000):

        # Повертаємо пустий список чисел, якщо умови не виконуються
        return []
    
    else:

        # Створюємо список чисел від min до max
        numbers = list(range(min, max+1))

        # Генерація унікальних випадкових чисел
        chosen_numbers = random.sample(numbers, quantity)

        # Повертаємо відсортований список чисел
        return sorted(chosen_numbers) 