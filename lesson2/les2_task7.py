# 7. Написать программу, доказывающую или проверяющую, что для множества натуральных чисел выполняется равенство:
# 1+2+...+n = n(n+1)/2, где n — любое натуральное число.

n = int(input("введите любое натуральное число: "))
sum = 0
for i in range(1, n + 1):
    sum += i
sum1 = (n * (n + 1)) / 2
print(f"sum = {sum}, sum1 = {sum1}")