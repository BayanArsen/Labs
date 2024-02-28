import re

with open('row.txt', 'r', encoding='utf-8') as file:
    text = file.read()
    
task7 = ''.join(word.capitalize() for word in text.split('_'))
print(task7)