import re

with open('row.txt', 'r', encoding='utf-8') as file:
    text = file.read()

task1 = re.findall('ab*', text)
print('№1: ',task1)

task2 = re.findall('ab{2,3}', text)
print('№2: ',task2)

task3 = re.findall('[a-z]+_[a-z]+', text)
print('№3: ',task3)

task4 = re.findall('[A-Z][a-z]+', text)
print('№4: ',task4)

task5 = re.findall('a.*b$', text)
print('№5: ', task5)