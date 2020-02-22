day_discount = {"завтра": 0.05, "сегодня": 0}
movie_parasite = {12: 250, 16: 350, 20: 450}
movie_1917 = {10: 250, 13: 350, 16: 350}
movie_sonic = {10: 350, 14: 450, 18: 450}
movies = {"Паразиты": movie_parasite, "1917": movie_1917, "Соник в кино": movie_sonic}


def count_discount(date, number):
    discount = day_discount[date]
    if number >= 20:
        discount += 0.2
    return discount


def movie_price(movie, date, number, time):
    try:
        price = str((1 - count_discount(date, number))
                 * movies[movie][time] * number)
        return "Результат: " + price + " руб."
    except:
        return "Ошибка!"


movie = str(input("Введите название фильма:"))
date = str(input("Выбрать день (сегодня, завтра):"))
time = int(input("Выбрать время:"))
number = int(input("Выбрать количество билетов:"))
print("Выбрали фильм:", movie, "День:", date, "Время:", time, "Количество билетов:", number)
print(movie_price(movie, date, number, time))
