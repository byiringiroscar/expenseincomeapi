import datetime


todays_date = datetime.date.today()
ayear_ago = todays_date-datetime.timedelta(days=30*12)
print("ayear_ago", ayear_ago)