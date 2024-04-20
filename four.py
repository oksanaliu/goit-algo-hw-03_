from datetime import datetime, timedelta

def get_upcoming_birthdays(users):
    today = datetime.today().date()
    upcoming_birthdays = []

    for user in users:
        birthday = datetime.strptime(user["birthday"], "%Y.%m.%d").date()

        next_birthday = datetime(today.year, birthday.month, birthday.day).date()
        if next_birthday < today:
            next_birthday = datetime(today.year + 1, birthday.month, birthday.day).date()

        days_until_birthday = (next_birthday - today).days

        if 0 <= days_until_birthday <= 7:
            if next_birthday.weekday() >= 5:
                days_until_birthday += (7 - next_birthday.weekday())
                next_birthday += timedelta(days=(7 - next_birthday.weekday()))


            congratulation_date = next_birthday.strftime("%Y.%m.%d")

            upcoming_birthdays.append({"name": user["name"], "congratulation_date": congratulation_date})

    return upcoming_birthdays

users = [
    {"name": "Oksana Liuklian", "birthday": "2001.04.27"},
    {"name": "JMariia Bilusiak", "birthday": "2001.07.23"}
]

upcoming_birthdays = get_upcoming_birthdays(users)
print("Список привітань на цьому тижні:", upcoming_birthdays)

