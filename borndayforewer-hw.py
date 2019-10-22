
def check_birthday_year():
    year_of_birth = ''
    while year_of_birth != 1799:
        year_of_birth = int(input('Не соблаговолите ли сказать, когда родился товарищ Пушкин?'))
        # ввел доп. проверку, т.к. почему-то через return year_of_birth не получается -
        # цикл не продолжается, а просто возвращается первый пользовательский ввод, т.е. неверный год рождения
        if year_of_birth == 1799:
            return year_of_birth


def check_birthday_day():
    day_of_birth = ''
    while day_of_birth != '6 июня':
        day_of_birth = input('А дату рождения помните?')
        if day_of_birth == '6 июня':
            print('Верно')

check_birthday_year()
check_birthday_day()


