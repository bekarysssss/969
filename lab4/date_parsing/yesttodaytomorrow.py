from datetime import datetime, timedelta

current_date = datetime.now()

new_date = current_date - timedelta(days=1)
new_date_1 = current_date + timedelta(days=1)

print("Yesterday:", new_date.strftime("%Y-%m-%d"))
print("Today:", current_date.strftime("%Y-%m-%d"))
print("Tomorrow:", new_date_1.strftime("%Y-%m-%d"))
