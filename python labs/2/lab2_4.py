import time

start_time = time.time()

L = [n ** 2 for n in range(100000)]

end_time = time.time()

elapsed_time = end_time - start_time
print('Elapsed time: ', elapsed_time)