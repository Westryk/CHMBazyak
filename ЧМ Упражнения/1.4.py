def get_delta_strict(val):
    """Считает абсолютную погрешность для числа, верного в строгом смысле"""
    s = f"{val:g}" # Число в строку без лишних нулей
    if '.' in s:
        decimals = len(s.split('.')[1]) # Знаки после запятой
    else:
        decimals = 0
    return 0.5 * (10**-decimals) # Формула верной в строгом смысле цифры

def calc_op(x, y, op):
    dx, dy = get_delta_strict(x), get_delta_strict(y) # Получаем ошибки для обоих чисел
    
    if op == '+': # Δ(x ± y) = Δx + Δy
        res = x + y
        d_res = dx + dy

    elif op == '-':
        res = x - y
        d_res = dx + dy # При вычитании ошибки всё равно складываются

    elif op == '*':
        res = x * y
        # Формула: Δ(xy) = x*Δy + y*Δx
        d_res = abs(x)*dy + abs(y)*dx

    elif op == '/':
        res = x / y
        # Формула: Δ(x/y) = (x*Δy + y*Δx) / y^2
        d_res = (abs(x)*dy + abs(y)*dx) / (y**2)
    
    delta_otnos = (d_res / abs(res)) * 100
    return res, d_res, delta_otnos

# Примеры из упражнения:
# Добавляем букву варианта четвертым элементом в кортеж
tasks = [
    (24.37, 9.18, '-', 'а'),
    (18.437, 24.9, '+', 'б'),
    (24.1, 0.037, '-', 'в'),
    (1.504, 1.502, '-', 'г'),
    (234.5, 194.3, '-', 'д'),
    (0.65, 1984, '*', 'е'),
    (12.6, 40.3, '*', 'ж'),
    (72.3, 0.34, '/', 'з'),
    (8124.6, 2.9, '/', 'и')
]

print(f"{'Вар':<4} | {'Операция':<15} | {'Результат':<10} | {'Δ (Абс)':<10} | {'δ (Относ, %)'}")
print("-" * 70)

for x, y, op, label in tasks:
    res, d_abs, d_otnos = calc_op(x, y, op)
    
    print(f"{label + ')':<4} | {x} {op} {y:<7} | {res:<10.4f} | {d_abs:<10.5f} | {d_otnos:.4f}%")