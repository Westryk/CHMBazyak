# --- УПРАЖНЕНИЕ 1 ---
# Дано: бета (основание) = 2, t (разряды мантиссы) = 2
# Диапазон порядков: P1 = -1, P2 = 1
beta = 2
t = 2
p_range = range(-1, 2)  # -1, 0, 1

floating_point_numbers = set()

# Формула мантиссы M = d1/beta + d2/beta^2
# d1 не может быть 0 (нормализация), значит d1 = 1
# d2 может быть от 0 до beta-1 (т.е. 0 или 1)
d1 = 1
for d2 in range(beta):
    mantissa = d1/beta + d2/(beta**2)
    for p in p_range:
        num = mantissa * (beta**p)
        floating_point_numbers.add(num)
        floating_point_numbers.add(-num) # Добавляем отрицательные

floating_point_numbers.add(0.0) # Машинный ноль
sorted_numbers = sorted(list(floating_point_numbers))

print(f"Упражнение 1: Количество чисел в системе = {len(sorted_numbers)}")
print(f"Список чисел: {sorted_numbers}")

# --- УПРАЖНЕНИЕ 2 ---
# Машинный ноль для системы: beta=10, t=3, P1=-9, P2=9
# Машинный ноль — это интервал вокруг нуля, числа в котором компьютер считает нулем.
beta2 = 10
p1 = -9
# Минимальное положительное число: мантисса 0.100 * 10^-9
min_positive = 0.1 * (beta2**p1)

print(f"\nУпражнение 2:")
print(f"Границы машинного нуля: (-{min_positive}, {min_positive})")