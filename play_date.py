from datetime import date, timedelta

today = date.today() # current date of the system
print(today)
print(type(today))

birthday = date(year=1986, month=11, day=25) # month is 1 based
print(birthday)

print(today.year)
print(today.month)
print(today.day)

print(today.weekday())

future_birthday = birthday.replace(year=today.year)
print(future_birthday)

print(future_birthday.strftime('%d-%m-%Y'))
print(future_birthday.strftime('%d %B %Y'))

print(birthday < future_birthday) # use regular relational operators to compare date objects

two_weeks_hence = timedelta(weeks=2)
two_weeks_hence_date = today + two_weeks_hence
print(two_weeks_hence_date)

five_days_past = timedelta(days=-5)
five_days_past_date = today + five_days_past
print(five_days_past_date)