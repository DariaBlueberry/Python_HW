def month_to_season(num):
    if 1 <= num <= 2:
        return ("Зимa")
    if 3 <= num <= 5:
        return ("Весна")
    if 6 <= num <= 8:
        return ("Лето")
    if 9 <= num <= 11:
        return ("Осень")
    if num == 12:
        return ("Зимa")
    else:
        return ("Такого месяца не существует =)")


num_month = int(input("Введите номер месяца:"))
result = month_to_season(num_month)
print(f'{result}')
