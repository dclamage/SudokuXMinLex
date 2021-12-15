import time
import sudokux_minlex

num_tests = 10000
start_time = time.time()
for i in range(1, num_tests):
	minlexed = sudokux_minlex.minlex('..............1....3....4...2.....................5......34....1.6....7....8.....')
end_time = time.time()
print(minlexed)

elapsed_time_sec = end_time - start_time
elapsed_time_us = elapsed_time_sec * 1000000.0
print("--- %sμs ---" % (elapsed_time_us / float(num_tests)))
