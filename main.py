from datetime import datetime, timedelta
from collections import defaultdict

def get_birthdays_per_week(users):
    today = datetime.today().date()

    birthdays = defaultdict(list)

    for user in users:
        name = user["name"]
        birthday = user["birthday"].date()
        # print('name: ', name)
        # print('birthday: ', birthday)
        
        birthday_this_year = birthday.replace(year=today.year)
        # print('birthday_this_year: ', birthday_this_year)
        if birthday_this_year < today:
            birthday_this_year = birthday.replace(year=today.year + 1)
        delta_days = (birthday_this_year - today).days
        # print('delta_days: ', delta_days)
        if delta_days < 7:
            day_of_week = (today + timedelta(days=delta_days)).strftime('%A')
            # print('day_of_week: ', day_of_week)
            if day_of_week == "Saturday" or day_of_week == "Sunday":
                day_of_week = "Monday"
            birthdays[day_of_week].append(name)
    for day, names in birthdays.items():
        print(f"{day}: {', '.join(names)}")
    # print("birthdays: ", birthdays)





users = [
    {"name": "Bill Gates", "birthday": datetime(1955, 10, 14)},
    {"name": "Jill Valentine", "birthday": datetime(1990, 10, 15)},
    {"name": "Kim Kardashian", "birthday": datetime(1980, 10, 21)},
    {"name": "Jan Koum", "birthday": datetime(1976, 10, 19)}
]

get_birthdays_per_week(users)
# print('get_birthdays_per_week(users): ', get_birthdays_per_week(users))