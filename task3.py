import random


def write_input(file_path, n, k, m, plans):
    with open(file_path, 'w') as file:
        file.write(f"{n} {k} {m}\n")
        for plan in plans:
            file.write(" ".join(map(str, plan)) + "\n")


def read_input(file_path):
    with open(file_path, 'r') as file:
        n, k, m = map(int, file.readline().split())
        plans = [tuple(map(int, file.readline().split())) for _ in range(m)]
    return n, k, m, plans


def calculate_minimum_cost(n, k, m, plans):
    total_cost = 0
    for day in range(1, n + 1):
        min_cost = float('inf')
        for plan in plans:
            l, r, c, p = plan
            if l <= day <= r:
                cost = (k + c - 1) // c * p
                min_cost = min(min_cost, cost)
        total_cost += min_cost
    return total_cost


def write_output(file_path, result):
    with open(file_path, 'w') as file:
        file.write(str(result))


def generate_plans(n, m):
    plans = []
    for _ in range(m):
        l = random.randint(1, n)
        r = random.randint(l, n)
        c = random.randint(1, 10)
        p = random.randint(1, 10)
        plans.append((l, r, c, p))
    return plans


n = random.randint(1, 10)
k = random.randint(1, 10)
m = random.randint(1, 5)
plans = generate_plans(n, m)
write_input("task23.in", n, k, m, plans)

n, k, m, plans = read_input("task23.in")

minimum_cost = calculate_minimum_cost(n, k, m, plans)

write_output("task23.out", minimum_cost)
