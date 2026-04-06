def calculate_errors(x_approx, lower_bound=None, upper_bound=None, delta_x=None):
    """
    x_approx: наилучшее приближение (x)
    delta_x: предельная абсолютная погрешность (Δx)
    """
    if lower_bound is not None and upper_bound is not None:
        delta_x = (upper_bound - lower_bound) / 2
    
    # Относительная погрешность (δx)
    delta_otnos = delta_x / abs(x_approx)
    
    return {
        "x": x_approx,
        "delta_absolute": delta_x,
        "delta_otnos_percent": delta_otnos * 100
    }

# --- УПРАЖНЕНИЕ 1 ---

ex1 = calculate_errors(x_approx=99.5, lower_bound=99.0, upper_bound=100.0)

# --- УПРАЖНЕНИЕ 2 ---

measurements = [4.8, 5.0, 4.9, 4.8, 5.0]
x_mean = sum(measurements) / len(measurements) # Поиск среднего арифметического (сумма всех секунд делить на количество попыток)


# Δx для многократных измерений (как в примере на стр. 15): (max - min) / 2
delta_x_2 = (max(measurements) - min(measurements)) / 2  # Разница между самым долгим и самым быстрым замером. Делим на 2, чтобы найти погрешность Δx
ex2 = calculate_errors(x_approx=x_mean, delta_x=delta_x_2)

# Вывод результатов
print("Упражнение 1 (Стол):")
print(f"Предельная абсолютная погрешность (Δx): {ex1['delta_absolute']} см")
print(f"Относительная погрешность (δx): {ex1['delta_otnos_percent']:.2f}%")

print("\nУпражнение 2 (Маятник):")
print(f"Наилучшее приближение (среднее x): {ex2['x']:.2f} с")
print(f"Предельная абсолютная погрешность (Δx): {ex2['delta_absolute']:.2f} с")
print(f"Относительная погрешность (δx): {ex2['delta_otnos_percent']:.2f}%")