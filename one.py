from datetime import datetime

def days_from_today(date):
    try:

        input_date = datetime.strptime(date, '%Y-%m-%d')
        today_date = datetime.today()
        delta = (today_date - input_date).days
    
        return delta
    except ValueError:
        return "Дата введена неправильно. Введіть дату у форматі 'РРРР-ММ-ДД'."
    
some_date = input("Введіть дату у форматі 'РРРР-ММ-ДД': ")

print(days_from_today(some_date))