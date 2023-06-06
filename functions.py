# Напишите функцию с именем find_all(target, symbol), которая принимает два аргумента: строку target и символ symbol и возвращает список, содержащий все местоположения этого символа в строке.
# Примечание 1. Если указанный символ не встречается в строке, то следует вернуть пустой список.

# объявление функции
def find_all(target, symbol):
    z = []
    n = -1
    for i in target:
        n += 1
        if i == symbol:
            z.append(n)
    return z
# считываем данные
target = input()
symbol = input()
# вызываем функцию
print(find_all(target, symbol))
# ------------------------------------------------------------------

# Напишите функцию merge(list1, list2), которая принимает в качестве аргументов два отсортированных по возрастанию списка, состоящих из целых чисел, и объединяет их в один отсортированный список.
# Примечание 1. Списки list1 и list2 могут иметь разную длину.

# объявление функции
def merge(list1, list2):
    g = list1 + list2
    g.sort()
    return g
# считываем данные
numbers1 = [int(c) for c in input().split()]
numbers2 = [int(c) for c in input().split()]
# вызываем функцию
print(merge(numbers1, numbers2))
# ------------------------------------------------------------------

# Напишите функцию print_fio(name, surname, patronymic), которая принимает три параметра:
# name – имя человека;
# surname – фамилия человека;
# patronymic – отчество человека;
# а затем выводит на печать ФИО человека.
# Примечание. Предусмотрите тот факт, что все три буквы в ФИО должны иметь верхний регистр.

# объявление функции
def print_fio(name, surname, patronymic):
    z = surname[:1] + name[:1] + patronymic[:1]
    print(z.upper())
# считываем данные
name, surname, patronymic = input(), input(), input()
# вызываем функцию
print_fio(name, surname, patronymic)
# ------------------------------------------------------------------

# Напишите функцию print_digit_sum(), которая принимает одно целое число num и выводит на печать сумму его цифр.

# объявление функции
def print_digit_sum(n):
    num = []
    n = str(n)
    for i in range(len(n)):
        num.append(int(n[i]))
    print(sum(num))
# считываем данные
n = int(input())
# вызываем функцию
print_digit_sum(n)
# ------------------------------------------------------------------

