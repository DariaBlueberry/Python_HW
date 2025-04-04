#Создать переменную
my_heigh = 170
print(my_heigh)

#Перезаписать переменную
my_name="Daria"
my_name = "Daria Chernikova"
print(my_name)

#Получите пользовательский ввод
pet_name = input("Как зовут вашего питомца?")
print("Ваш любимчик - " + pet_name)

#Создание функции

def print_python():
    print("Учу Python!")


print_python()

#Параметризация функций
def print_letter(let):
    print(let, end="")


print_letter("С")
print_letter("Т")
print_letter("У")
print_letter("Д")
print_letter("Е")
print_letter("Н")
print_letter("Т")
