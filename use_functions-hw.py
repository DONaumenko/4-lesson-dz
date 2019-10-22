"""
1. пополнение счета
при выборе этого пункта пользователю предлагается ввести сумму на сколько пополнить счет
после того как пользователь вводит сумму она добавляется к счету
снова попадаем в основное меню
"""
# Начальное значение счета
total_balance = 0

def menu_output():
    print('Меню операций:')
    print('1. пополнение счета')
    print('2. покупка')
    print('3. история покупок')
    print('4. выход')
    choice = int(input('Напишите цифру от 1 до 4:'))
    return choice


def popolnenie_scheta():
    popolnenie = int(input('Сколько рублей вы хотите положить на счёт?'))
    total_balance += popolnenie
    print(f'Ваш баланс пополнен на {popolnenie} руб. Общий баланс: {total_balance} руб.')
    menu_output()


def pokupka():
    pass


def pokupka_history():
    pass

choice = menu_output()
if choice == 1:
    popolnenie_scheta()
elif choice == 2:
    pokupka()
elif choice == 3:
    pokupka_history()
elif choice == 4:
    exit()
else:
    print('Нет такой буквы в этом слове:) Try again')








