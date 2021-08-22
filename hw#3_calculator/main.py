#Ashat_Polvanov

# Калькулятор для 4ых операций(+,-,*,/), каждая операция - в отдельном модуле,
# основной модуль программы - main.py
# Сделать возможность запускать модули самостоятельно и выполнять приведённый в них функционал, с помощью конструкции: 
# if __name__ == '__main__':
#       pass # ваш код
import addition
import subtraction
import division
import multiplication

def main():
    first_number = float(input('Введите первое число: '))
    second_number = float(input('Введите второе число: '))
    operation = input('Введите операцию "+, -, /, *": ')
    if operation == '+':
        result = addition.operation(first_number, second_number)
    elif operation == '-':
        result = subtraction.operation(first_number, second_number)
    elif operation == '/':
        result = division.operation(first_number, second_number)
    elif operation == '*':
        result = multiplication.operation(first_number, second_number)
    print('Результат: ',result)

if __name__ == '__main__':
    main()