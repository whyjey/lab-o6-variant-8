import math

# Функція для обчислення f(x)
def f(x):
    return math.log(abs(x + math.exp(x)), 3)

# 1. Обчислення значень функції за допомогою циклу for
def calculate_with_for_loop(a, b, h):
    values = []
    x = a
    while x <= b:
        values.append(f(x))
        x += h
    return values

# 2. Обчислення значень функції за допомогою циклу while
def calculate_with_while_loop(a, b, h):
    values = []
    x = a
    while x <= b:
        values.append(f(x))
        x += h
    return values

# 3. Виведення результатів і обчислення середнього арифметичного
def print_results_and_calculate_average(values):
    for value in values:
        print(value)
    average = sum(values) / len(values)
    print("Середнє арифметичне:", average)

# Основна програма
a = float(input("Введіть a: "))
b = float(input("Введіть b: "))
h = float(input("Введіть h: "))

# Використовуємо обидва методи для обчислень
print("\nОбчислення за допомогою циклу for:")
values_for = calculate_with_for_loop(a, b, h)
print_results_and_calculate_average(values_for)

print("\nОбчислення за допомогою циклу while:")
values_while = calculate_with_while_loop(a, b, h)
print_results_and_calculate_average(values_while)
