""" Python Military Check Pass """
import hashlib
import sys

# PUTIN_PREZIDENT_MIRA
# шифр в md5
password = "8c068bdc54d98302087916b9c3f1b840"

def main():
    # Секретная часть требующая подтверждения прав доступа
    print("КОД ЗАПУСКА БАЛИСТИЧЕСКИХ РАКЕТ: NEW_LIFE_0000_|__")
    sys.exit(0)


while True:
    inp = input("Введите пароль: ")
    if hashlib.md5(bytes(inp, 'utf-8')).hexdigest() == password:
        print ("Аутентификация прошла успешно! Вы в системе!")
        main()
    else:
        print ("НЕВЕРНЫЙ ПАРОЛЬ! Вы начали ИГРУ 'рулетка', одна из попыток будет для Вас последней!")