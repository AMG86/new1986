def my_function ():

    while True:
        stroka1 = input('Введите первую строку: ')
        stroka2 = input('Введите вторую строку: ')

        if type(stroka1) != str or type(stroka2) != str:
            return 0

        elif len(stroka1) == len(stroka2):
            print(1)

        elif len(stroka1) > len(stroka2):
            print(2)

        elif len(stroka1) != len(stroka2) and stroka2 == 'learn':
            print(3)
            
        else:
            break

if __name__ == "__main__":
    my_function()
