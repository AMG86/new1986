def age_grade():
    while True:
        age = input ('Введите Ваш возраст: ')
        try:
            s = float(age)
            if s <= 0:
                print('Ошибка')
            elif s > 0 and s <= 2:
                print('Вы младенец')
                break
            elif s > 2 and s <= 4:
                print('Вы ходите в ясли')
                break
            elif s > 4 and s <= 6:
                print('Вы ходите в детский сад')
                break
            elif s > 6 and s <= 17:
                print('Вы учитесь в школе')
                break
            elif s > 17 and s <= 22:
                print('Вы учитесь в ВУЗе')
                break
            elif s > 22 and s <= 65:
                print('Вы работаете')
                break
            elif s > 65:
                print('Вы на пенсии')
                break
        except:
            if age.isalpha():
                print('Ошибка')

if __name__ == "__main__":
    age_grade()
