import re

with open('row.txt', 'r', encoding='utf-8') as file:
    text = file.read()

task6 = re.sub(r'[ ,.]', ':', text)
print(task6)
