import random

# Функция для записи входных данных в файл
def write_input(file_path, n, k, m, plans):
    with open(file_path, 'w') as file:
        file.write(f"{n} {k} {m}\n")  # Записываем параметры n, k и m
        for plan in plans:
            file.write(" ".join(map(str, plan)) + "\n")  # Записываем каждый тарифный план в новой строке

# Функция для чтения входных данных из файла
def read_input(file_path):
    with open(file_path, 'r') as file:
        n, k, m = map(int, file.readline().split())
        plans = [tuple(map(int, file.readline().split())) for _ in range(m)]
    return n, k, m, plans

# Функция для расчета минимальной суммы денег, которую Бубер заплатит
def calculate_minimum_cost(n, k, m, plans):
    total_cost = 0
    for day in range(1, n + 1):
        min_cost = float('inf')  # Инициализируем минимальную стоимость как бесконечность
        for plan in plans:
            l, r, c, p = plan
            if l <= day <= r:  # Если тарифный план доступен в текущий день
                cost = (k + c - 1) // c * p  # Вычисляем стоимость для заданного количества ядер
                min_cost = min(min_cost, cost)  # Обновляем минимальную стоимость
        total_cost += min_cost  # Добавляем минимальную стоимость к общей сумме
    return total_cost

# Функция для записи результата в выходной файл
def write_output(file_path, result):
    with open(file_path, 'w') as file:
        file.write(str(result))

# Функция для генерации случайных тарифных планов
def generate_plans(n, m):
    plans = []
    for _ in range(m):
        l = random.randint(1, n)
        r = random.randint(l, n)
        c = random.randint(1, 10)
        p = random.randint(1, 10)
        plans.append((l, r, c, p))
    return plans

# Генерация случайных входных данных и запись их в файл
n = random.randint(1, 10)
k = random.randint(1, 10)
m = random.randint(1, 5)
plans = generate_plans(n, m)
write_input("task23.in", n, k, m, plans)

# Чтение входных данных
n, k, m, plans = read_input("task23.in")

# Вычисление минимальной суммы денег
minimum_cost = calculate_minimum_cost(n, k, m, plans)

# Запись результата в выходной файл
write_output("task23.out", minimum_cost)
