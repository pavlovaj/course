import time

n = input("Введите дату рождения в формате дд.мм.гггг:")
print(round((time.time() - time.mktime(time.strptime(n, '%d.%m.%Y'))) / 86400))
