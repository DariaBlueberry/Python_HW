#Использование if

#Пример 1

age = 18

if (age < 18):
    print("ok")
else:
    print("Не берем в лагерь")
print("final")

#Пример 2

password = "test123"

if (password == "test123"):
    print("passed")
else:
    print("Неверный логин или пароль")

#Intaractive - Создаем программу по обратной связи:

# Как-то получить от пользователя оценку
rate_is_str = input('Оцените работу оператора от 1 до 5:') #str
rate = int(rate_is_str) #int

#Проверить, что оценка от 1 до 5
if (rate < 1):
    rate = 1
if (rate > 5):
    rate = 5

print(rate)

#В зависимости от оценки предложить дать обратную связь

feedback = ''

if rate == 1:
    feedback = input('расскажите, что нам улучшить?')
elif rate == 2:
        feedback = input('что вас смутило?')
elif rate == 3:
    feedback = input('что мы могли бы улучшить?')
elif rate == 4:
    feedback = input('расскажите, почему не 5?')
else:
    feedback = input('расскажите, как похвалить оператора?')

print(feedback)

#Работа с циклами
for x in range(1,10):
    print(x)

#Таблица квадратов
for x in range(1,21):

    print('x=', x, 'x2=', x*x)

#Вывести список студентов, если список будет изменяться:
students = ['Александр', 'Михаил', 'Мария', 'Ольга', 'Кирилл', 'Олеся', 'Виктор']

for i in range(0, len(students)):
    print(students[i])

#Что еще умеют циклы?
word = 'Test'

for x in range(0, len(students)):
    print(students[x])

for s in word:
    print(s)

for student in students:
    print(student)

#Что еще умеют циклы? Напечатать только нечетные цифры(фильтрация):
nums = [1,2,3,4,5,6,7,8,9,10]

for n in nums:
    if (n % 2 == 1):
        print(n)

#Логическое and
user_login = 'adam'
user_pass = 'Qwerty123456'

login = input("Login: ")
password = input("Password: ")

if (login == user_login) and (password == user_pass):
    print("Secret is open")
else:
    print('Locked')

#Логическое or
crit1 = 'red'
crit2 = 'lock'

color = input("Color: ")
feature = input("Feature: ")

if (color == crit1) or (feature == crit2):
    print('Buy it!')
else:
    print("Don't buy")
