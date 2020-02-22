codes = {343:15, 381:18, 473:13, 485:11}


def count_price(code, minutes):
    return codes[code] * minutes


try:
    kod = int(input("Введите код города:"))
    minutes = int(input("Кол-во минут:"))
    print("Стоимость звонка: ", count_price(kod, minutes))
except:
    print('Ошибка!')

