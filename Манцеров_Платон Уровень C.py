#1
import random
lst = [random.randint(-100,100) for i in range(random.randint(10, 1000))]
print(lst)
sum = 0
for i in range(len(lst)):
    if lst[i] > 0:
        sum=sum+lst[i]
print(sum)


#2
try:
    a = float(input("Введите a: "))
    b = float(input("Введите b: "))
    X = float(input("Введите X: "))
    if a <= X <= b:
        print(f"Число {X} принадлежит промежутку [{a}, {b}]")
    else:
        print(f"Число {X} не принадлежит промежутку [{a}, {b}]")
except(ValueError):
    print("Введите число")


#3
numbers = int(input("Введите количество чисел"))
lst_2 = [random.randint(0,123456)for i in range(numbers)]
print(lst_2)
minimum = 0
maximum = 123457
for elem in lst_2:
    if elem < maximum:
        maximum = elem
    if elem > minimum:
        minimum = elem
print(f"Минимум {maximum}")
print(f"Максимум {minimum}")

