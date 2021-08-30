#Ashat_Polvanov

# Дан файл с данными:

# name,age,salary
# Tom,28,500
# Alice,23,1200
# Bob,34,2400
# Mark,23,700
# Frank,20,900
# Fill,23,1200
# Jonh,44,2330
# Greg,53,1500
# Peter,18,100
# 1. Посчитать среднюю зп.
# 2. Посчитать средний возраст

import csv
import os
import sys



names = ['Tom', 'Alice','Bob', 'Mark', 'Frank', 'Fill', 'Jonh', 'Greg', 'Peter']
ages = [28, 23, 34, 23, 20, 23, 44, 53, 18]
salarys = [500, 1200, 2400, 700, 900, 1200, 2330, 1500, 100]
my_database = []
index = 0
while index != 9:
    my_database.append({'name' : names[index], 'age' : ages[index], 'salary' : salarys[index]})
    index += 1
FILE_NAME = os.path.join(sys.path[0], 'employee_data.txt')
with open(FILE_NAME, 'w') as file:
    writer = csv.DictWriter(file, my_database[0].keys())
    writer.writeheader()
    writer.writerows(my_database)

def average_calculation(salarys):
    sum_of_numbers = 0
    for i in salarys:
        sum_of_numbers += i
    average_number = sum_of_numbers / len(salarys)
    return average_number
    
average_salary = average_calculation(salarys)
average_age = average_calculation(ages)
def main():
    average_calculation(salarys)
    average_calculation(ages)
    return average_salary, average_age
main()
with open(FILE_NAME) as file:
    file.read()

with open(FILE_NAME, 'w') as file:
    file.write('Average_salary =' + '%s' % average_salary + '\n')

with open(FILE_NAME) as file:
    file.read()

with open(FILE_NAME, 'w') as file:
    file.write('Average_age =' + '%s' % average_age )