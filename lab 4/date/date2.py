from datetime import datetime, timedelta

today = datetime.now().date()

yd = today - timedelta(days=1)
tmr = today + timedelta(days=1)

print("Yesterday:", yd)
print("Today:", today)
print("Tomorrow:", tmr)