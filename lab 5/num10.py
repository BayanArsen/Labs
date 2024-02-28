import re

with open('row.txt', 'r', encoding='utf-8') as file:
    text = file.read()

task10 = re.sub(r'(?<!^)(?=[A-Z])', '_', text).lower()
print(task10)