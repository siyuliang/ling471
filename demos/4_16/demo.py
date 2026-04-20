import time

d = {i: None for i in range(1000)} 

start = time.perf_counter()

if 100 in d:
    print("yes")

# if 100 in list(range(1000)):
#     print('yes')

end = time.perf_counter()

print(f"Runtime: {end - start:.6f} seconds")

