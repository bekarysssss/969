from datetime import datetime

current_time = datetime.now()

without_microseconds = current_time.replace(microsecond=0)

print("Current time:", current_time)
print("Without microseconds:", without_microseconds)
