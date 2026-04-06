import math

def F(x):
    """Исходная функция F(x) = 0"""
    return x * math.sin(x) - 1

def simple_iteration():
    print("Метод простой итерации для x*sin(x) - 1 = 0")
    
    # Входные данные
    x = 1.1        # начальное приближение x0
    eps = 1e-5     # точность 10^-5
    q = 0.5        # коэффициент сходимости (max |f'(x)|)
    m = 0.5        # параметр преобразования уравнения
    
    # Вспомогательная величина для условия выхода из цикла
    # a = eps * (1 - q) / q
    limit_val = eps * (1 - q) / q
    
    # Для отслеживания разности между итерациями
    p = 1.0 
    iteration_count = 0

    while abs(p) > limit_val:
        x_old = x
        
        # Итерационная формула: x_next = x - m * F(x)
        x = x_old - m * F(x_old)
        
        # p = x_next - x_prev
        p = x - x_old
        iteration_count += 1
        
        print(f"Итерация {iteration_count}: x = {x:.7f}, |p| = {abs(p):.7f}")

    print("-" * 30)
    print(f"Результат: x = {x:.5f}")
    print(f"Всего итераций: {iteration_count}")

if __name__ == "__main__":
    simple_iteration()