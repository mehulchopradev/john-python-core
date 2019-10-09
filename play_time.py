from datetime import time, datetime

specific = time(hour=13, minute=30)
print(specific)

dt = datetime.now() # current date and time
print(dt)

print(dt.time())
print(dt.date())