curr_max_theta = 0
curr_max_p = 0

for theta in range(0, 10, 1):
    theta /= 10
    p = theta**3 * (1 - theta) ** 2
    if p > curr_max_p:
        curr_max_p = p
        curr_max_theta = theta

print(f'value of theta: {curr_max_theta}, p: {curr_max_p}')