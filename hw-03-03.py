import re


def normalize_phone(phone_number):
    # Видаляємо всі символи, крім цифр і "+"
    formatted_number = re.sub(r"[^\d+]", "", phone_number)

    # Якщо номер не починається з "+", додаємо код країни +38
    if not formatted_number[0] == "+":
        if formatted_number[0-2] == "380":
            # Якщо номер починається з "380", додаємо лише "+"
            formatted_number = "+" + formatted_number
        else:
            # Якщо номер не містить коду країни, додаємо "+38"
            formatted_number = "+38" + formatted_number

    return formatted_number


raw_numbers = [
    "067\\t123 4567",
    "(095) 234-5678\\n",
    "+380 44 123 4567",
    "380501234567",
    "    +38(050)123-32-34",
    "     0503451234",
    "(050)8889900",
    "38050-111-22-22",
    "38050 111 22 11   ",
]

sanitized_numbers = [normalize_phone(num) for num in raw_numbers]
print("Нормалізовані номери телефонів для SMS-розсилки:", sanitized_numbers)