total_balance = 0
pokupka_history = {}

while True:
    print('Меню операций:')
    print('1. Пополнение счета')
    print('2. Покупка')
    print('3. История покупок')
    print('4. Выход')

    choice = input('Выберите пункт меню от 1 до 4: ')

    if choice == '1':
        popolnenie_sum = int(input('Укажите сумму пополнения: '))
        total_balance += popolnenie_sum
        print(f'Ваш баланс пополнен на {popolnenie_sum} руб.')
        print('')

    elif choice == '2':
        print('')
        print(f'Ваш текущий баланс: {total_balance} руб.')
        pokupka_sum = int(input('Укажите сумму покупки: '))

        if pokupka_sum > total_balance:
            print('Недостаточно средств на счете')
            print('')
        else:
            pokupka = input('Что покупаем? ')
            total_balance = total_balance - pokupka_sum
            print(f'Покупка прошла успешно. Ваш текущий баланс: {total_balance} руб.')
            pokupka_history[pokupka] = pokupka_sum
            print('')

    elif choice == '3':
        # print(pokupka_history.items)
        # print(list(pokupka_history.items()))
        # print(pokupka_history)
        print('')
        print('История покупок:')
        for product, price in pokupka_history.items():
            print(f'{product}: {price} руб.')
        print('')

    elif choice == '4':
        print('Вы вышли из программы')
        break

    else:
        print('Неверный пункт меню')
