from datetime import datetime ,timedelta
current_time = datetime.now()
new_time = current_time.replace(microsecond=0)
print("Original Datetime:", current_time)
print("Datetime without microseconds:", new_time)