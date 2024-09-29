from datetime import datetime


def get_days_from_today(date):
    try:
        # Перетворення рядка дати у форматі 'РРРР-ММ-ДД' у об'єкт datetime.
        date = datetime.strptime(date, "%Y-%m-%d").date()

        # Поточна дата, отримана за допомогою datetime.today().
        today = datetime.today().date()

        # Розрахунок різниці між поточною датою та заданою датою.
        diff = today.toordinal() - date.toordinal()
        return diff
    
    except ValueError:
        return "invalid date"
