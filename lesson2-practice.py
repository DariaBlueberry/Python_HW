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