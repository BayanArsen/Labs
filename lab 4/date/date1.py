from datetime import datetime, timedelta

today = datetime.now()

count = today - timedelta(days=5)

# Print the result
print("-5 day is:", count.strftime("%Y-%m-%d"))