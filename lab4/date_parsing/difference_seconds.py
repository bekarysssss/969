from datetime import datetime

def date_difference_seconds(date1, date2):
    date1 = datetime.strptime(date1, '%Y-%m-%d %H:%M:%S')
    date2 = datetime.strptime(date2, '%Y-%m-%d %H:%M:%S')

    difference = date2 - date1
    return difference.total_seconds()

date1 = '2024-02-18 00:38:00'
date2 = '2024-02-19 11:00:00'
print("Difference", date_difference_seconds(date1, date2))
