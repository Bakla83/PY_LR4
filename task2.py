import random


def generate_numbers(file_path, N):
    with open(file_path, 'w') as file:
        for _ in range(N):
            file.write(f"{random.randint(1, 100)}\n")


def generate_products(input_file, output_file):
    with open(input_file, 'r') as file:
        numbers = [int(line.strip()) for line in file]

    products = []
    product = 1
    for num in numbers:
        product *= num
        products.append(product)


    with open(output_file, 'w') as file:
        for prod in products:
            file.write(f"{prod}\n")


generate_numbers("numbers.txt", 10)

generate_products("numbers.txt", "products.txt")
