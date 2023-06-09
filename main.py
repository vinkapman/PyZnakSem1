"""Задача 2: Найдите сумму цифр трехзначного числа.
123 -> 6 (1 + 2 + 3)
100 -> 1 (1 + 0 + 0)

Решение:

num = int(input("Введите трехзначное число: "))
sum = num//100 + ((num - num//100*100))//10 + ((num - num//100*100))%10

print("Сумма цифра введенного чила равна:", sum)

Задача 4: Петя, Катя и Сережа делают из бумаги журавликов. Вместе
они сделали S журавликов. Сколько журавликов сделал каждый
ребенок, если известно, что Петя и Сережа сделали одинаковое
количество журавликов, а Катя сделала в два раза больше журавликов,
чем Петя и Сережа вместе?
6 -> 1 4 1
24 -> 4 16 4
60 -> 10 40 10

Решение:

sum = int(input("Сколько журавликов сделали дети: "))

petr = int(sum / 6)
serg = petr
kate = petr * 4

print("Петр сделал", petr, "журавлика(ов), Сергей сделал", serg, "журавлика(ов), Катя", kate, "журавлика(ов).")


Задача 6: Вы пользуетесь общественным транспортом? Вероятно, вы
расплачивались за проезд и получали билет с номером. Счастливым
билетом называют такой билет с шестизначным номером, где сумма
первых трех цифр равна сумме последних трех. Т.е. билет с номером
385916 – счастливый, т.к. 3+8+5=9+1+6. Вам требуется написать
программу, которая проверяет счастливость билета.
385916 -> yes
123456 -> no

Решение:

num = int(input("введите номер билета: "))

cifOne = num//100000
cifTwo = (num - cifOne * 100000)//10000
cifThree = (num - cifOne * 100000 - cifTwo * 10000)//1000
cifFour = (num - cifOne * 100000 - cifTwo * 10000 - cifThree * 1000)//100
cifFive = (num - cifOne * 100000 - cifTwo * 10000 - cifThree * 1000 - cifFour * 100)//10
cifSix = (num - cifOne * 100000 - cifTwo * 10000 - cifThree * 1000 - cifFour * 100 - cifFive * 10) % 10

if (cifOne + cifTwo + cifThree == cifFour + cifFive + cifSix):
    print("Билет с №", num, "является счастливым!")
else:
    print("Билет с №", num, "не является счастливым. Удачи в будущем!")

Задача 8: Требуется определить, можно ли от шоколадки размером n × m долек 
отломить k долек, если разрешается сделать один разлом по
прямой между дольками (то есть разломить шоколадку на два
прямоугольника).
3 2 4 -> yes
3 2 1 -> no

Решение:

m = int(input("Введите первую сторону: "))
n = int(input("Введите вторую сторону: "))
k = int(input("Введите количество долек, которое хотите отломить: "))

if (k%m == 0 or k%n == 0) and k<m*n:
    print("Yes")
else:
    print("No")

"""