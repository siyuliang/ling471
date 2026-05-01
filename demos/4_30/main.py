import random

n = 1_000_000
n_h = sum(random.choices([0, 1], k=n))
print(n_h / n)

n_h = sum(x >= 1 for x in random.choices(range(10), k=n))
print(n_h / n)

curr_max_x = 0
curr_max_p = 0

for x in range(0, 1000, 1):
    x /= 1000
    p = x**3 * (1 - x) ** 2
    if p > curr_max_p:
        curr_max_p = p
        curr_max_x = x
print(f'value of theta: {curr_max_x}, p: {curr_max_p}')