import re

with open('row.txt', 'r', encoding='utf-8') as file:
    text = file.read()

task9 = re.sub(r'(\w)([A-Z])', r'\1 \2', text)
print(task9)