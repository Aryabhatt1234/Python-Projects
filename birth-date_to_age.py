from datetime import datetime, date

def calculate_age(birth_date):
    today = date.today()
    day, month, year = map(int, birth_date.split('-'))
    birth_date = date(year, month, day)
    age = today.year - birth_date.year

    if today.month < birth_date.month or (today.month == birth_date.month and today.day < birth_date.day):
        age -= 1

    return age

# Example usage
date_input = input("Enter the date of birth (dd-mm-yyyy): ")
age = calculate_age(date_input)
print("Your age is", age, "years")