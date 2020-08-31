# **************************************************************************** #
#                                                                              #
#                                                         ::::::::             #
#    loading.py                                         :+:    :+:             #
#                                                      +:+                     #
#    By: pde-bakk <pde-bakk@student.codam.nl>         +#+                      #
#                                                    +#+                       #
#    Created: 2020/08/31 00:11:52 by pde-bakk      #+#    #+#                  #
#    Updated: 2020/08/31 11:14:32 by pde-bakk      ########   odam.nl          #
#                                                                              #
# **************************************************************************** #

import time, sys, os
bar_width = 40

def ft_progress(listy):
	for max in listy:
		maxR = max + 1
	# print("max = ", max, ", maxR = ", maxR)
	starttime = time.time()
	for i in listy:
		yield i
		os.system("clear")
		elapsed_time = time.time() - starttime
		estimated_time = elapsed_time * (maxR - i) / 1000
		print("maxR - i = ", maxR - i)
		progress = int((i * bar_width) / maxR)
		fill = bar_width - 1 - progress
		# print(f"ETA: idk s [00%][",bar_width * '=', '] ', i, '/', maxR)
		print(f"ETA: {estimated_time:.2f}s [{round(((i*100) / maxR)):3}%] [{progress * '='}>{fill * ' '}] {i+1}/{maxR} | elapsed time {elapsed_time:.2f}s")
listy = range(1000)
print(listy)
ret = 0
print(ft_progress(listy))
for elem in ft_progress(listy):
	ret += (elem + 3) % 5
	# time.sleep(0.01)
print()
print(ret)
