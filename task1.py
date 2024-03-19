#задание1

import random


def generate_file(file_path, N):
    with open(file_path, 'w') as file:
        file.write(f"{N} {random.randint(50, 200)}\n")
        for _ in range(N):
            file.write(f"{random.randint(10, 100)}\n")


def count_pairs(ratings, K):
    ratings.sort()
    count = 0
    left = 0
    right = len(ratings) - 1

    while left < right:
        if ratings[left] + ratings[right] >= K:
            count += (right - left)
            right -= 1
        else:
            left += 1

    return count


def process_file(file_path):
    with open(file_path, 'r') as file:
        N, K = map(int, file.readline().split())
        ratings = [int(file.readline()) for _ in range(N)]

    return count_pairs(ratings, K)


generate_file("27-169a.txt", 50)
generate_file("27-169b.txt", 50)

result_A = process_file("27-169a.txt")
result_B = process_file("27-169b.txt")

print(result_A, result_B)
