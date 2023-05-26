a = input("Ввод:")
def duplicates(a):
    if len(set(a)) == len(a):
        return("Дубликатов нет.")
    else:
        return("Есть дубликаты.")
print(duplicates(a))
