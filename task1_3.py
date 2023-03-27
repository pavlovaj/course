n = int(input("Введите целое число:"))

sum = 0

while n > 0:
    digit = n % 10
    suma = sum + digit
    n = n // 10

print("Сумма:", sum)
