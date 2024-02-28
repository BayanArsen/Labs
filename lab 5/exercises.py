import re

with open('row.txt', 'r', encoding='utf-8') as file:
    text = file.read()

task1 = re.findall('ab*', text)
print(task1)

task2 = re.findall('ab{2,3}', text)
print(task2)

task3 = re.findall('[a-z]+_[a-z]+', text)
print(task3)

task4 = re.findall('[A-Z][a-z]+', text)
print(task4)

task5 = re.findall('a.*b$', text)
print(task5)