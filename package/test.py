import time
import sudokux_minlex

input_puzzle = '..............1....3....4...2.....................5......34....1.6....7....8.....'
print(input_puzzle)

num_tests = 10000
start_time = time.time()
for i in range(0, num_tests):
	minlexed = sudokux_minlex.minlex(input_puzzle)
end_time = time.time()
print(minlexed)
elapsed_time_sec = end_time - start_time
elapsed_time_us = elapsed_time_sec * 1000000.0
print("--- %.2fμs ---" % (elapsed_time_us / float(num_tests)))

count_start_time = time.time()
count1 = 0
count2 = 0
for i in range(0, num_tests):
	count1 = sudokux_minlex.solution_count(input_puzzle, 0)
	count2 = sudokux_minlex.solution_count(minlexed, 0)
count_end_time = time.time()
print('Solution count (input): %d (%s)' % (count1, (count1 == 4 and 'correct' or 'incorrect')))
print('Solution count (minlex): %d (%s)' % (count2, (count2 == 4 and 'correct' or 'incorrect')))
elapsed_time_sec = count_end_time - count_start_time
elapsed_time_us = elapsed_time_sec * 1000000.0
print("--- %.2fμs ---" % (elapsed_time_us / float(num_tests)))

solve_start_time = time.time()
solved1 = ''
solved2 = ''
for i in range(0, num_tests):
	solved1 = sudokux_minlex.solve(minlexed, False)
	solved2 = sudokux_minlex.solve(minlexed, False)
solve_end_time = time.time()
print('Solved (input): %s' % solved1)
print('Solved (minlex): %s' % solved2)
elapsed_time_sec = solve_end_time - solve_start_time
elapsed_time_us = elapsed_time_sec * 1000000.0
print("--- %.2fμs ---" % (elapsed_time_us / float(num_tests)))
