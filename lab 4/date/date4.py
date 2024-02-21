from datetime import datetime

date1 = datetime.strptime(input("Enter 1: "), "%Y-%m-%d %H:%M:%S")
date2 = datetime.strptime(input("Enter 2: "), "%Y-%m-%d %H:%M:%S")

print("The difference: ", abs((date2 - date1).total_seconds()))