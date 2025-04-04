# Високостный год
def is_year_leap(year):
    if year % 4 == 0:
        return True
    else:
        False


year_num = int(input('Введите год'))
result = is_year_leap(year_num)
print(f'год {year_num}:{result}')
