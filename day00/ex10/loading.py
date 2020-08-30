# **************************************************************************** #
#                                                                              #
#                                                         ::::::::             #
#    loading.py                                         :+:    :+:             #
#                                                      +:+                     #
#    By: pde-bakk <pde-bakk@student.codam.nl>         +#+                      #
#                                                    +#+                       #
#    Created: 2020/08/31 00:11:52 by pde-bakk      #+#    #+#                  #
#    Updated: 2020/08/31 00:11:52 by pde-bakk      ########   odam.nl          #
#                                                                              #
# **************************************************************************** #

import time, sys, os
bar_width = 40

def ft_progress(listy):
	starttime = time.time()
	for i in listy:
		yield i
		os.system("clear")
		elapsed_time = time.time() - starttime
		print(f"ETA: idk s [00%")

listy = range(1000)
ret = 0
test = ft_progress(listy)
print(test)
for elem in ft_progress(listy):
	ret += (elem + 3) % 5
	# print("haha ret = ", ret)
	time.sleep(0.01)
print()
print(ret)
