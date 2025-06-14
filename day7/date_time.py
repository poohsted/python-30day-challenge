# Day 7

# Using datetime to get current time and date

from datetime import datetime

now = datetime.now()
print("Current date and time:", now)
print("Just the date:", now.date())
print("Formatted:", now.strftime("%Y-%m-%d %H:%M:%S"))

# Formatting dates and times

from datetime import date

birthday = date(2004, 4, 13)
print("Your birthday:", birthday)

from datetime import datetime

start = datetime(2025, 6, 13, 14, 0, 0)
end = datetime(2025, 6, 13, 16, 30, 0)

duration = end - start
print("Duration:", duration)
print("Total minutes:", duration.total_seconds() / 60)

# Creating countdown timers

import time

seconds = 5
for i in range(seconds, 0, -1):
    print(f"Countdown: {i} seconds remaining")
    time.sleep(1)

print("Time's up!")

# Measuring execution time 

import time

def slow_task():
    time.sleep(2)
    print("Done sleeping")

start = time.time()
slow_task()
end = time.time()

print("Execution time:", end - start, "seconds")




