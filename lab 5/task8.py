import re

with open('row.txt', 'r', encoding='utf-8') as file:
    text = file.read()

task8 = re.split(r'(?=[А-ЯA-Z])', text)
print(task8)