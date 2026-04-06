import math

def f(x, variant):
    if variant == 'а':
        return x**3 - x - 4.5
    elif variant == 'б':

        return x * math.log10(x + 1) - 1

def dyh(a, b, eps, variant): # Если перемножить плюс на минус, будет минус (меньше 0). Если результат >= 0, значит, знаки одинаковые, и нельзя гарантировать, что внутри есть корень
    if f(a, variant) * f(b, variant) >= 0:
        print("Ошибка: корень на отрезке не гарантирован.")
        return None

    step = 0
    while (b - a) / 2 > eps:
        step += 1
        mid = (a + b) / 2
        if f(mid, variant) == 0:
            return mid
        
        # Выбираем ту половину, где функция меняет знак
        if f(a, variant) * f(mid, variant) < 0:
            b = mid
        else:
            a = mid
            
    return (a + b) / 2

# Решаем вариант 'а' с точностью 0.01
root_a = dyh(1.5, 2.0, 0.01, 'а')
print(f"Вариант а): Корень ≈ {root_a:.3f}")

# Решаем вариант 'в' с точностью 0.01
root_b = dyh(2.0, 3.0, 0.01, 'б')
print(f"Вариант б): Корень ≈ {root_b:.3f}")