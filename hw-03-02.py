import random


def get_numbers_ticket(min, max, quantity):

    # Перевірка на відповідність умовам
    if min >= 1 and max <= 1000:

        # Створюємо список чисел від min до max
        numbers = list(range(min, max+1))

        # Генерація унікальних випадкових чисел
        chosen_numbers = random.sample(numbers, quantity)

        # Повертаємо відсортований список чисел
        return sorted(chosen_numbers)
    else:

        # Повертаємо пустий список чисел, якщо умови не виконуються
        return []
    

lottery_numbers = get_numbers_ticket(1, 49, 6)
print("Ваші лотерейні числа:", lottery_numbers)