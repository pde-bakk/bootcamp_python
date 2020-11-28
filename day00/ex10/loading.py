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

import os
import time

bar_width = 40


def ft_progress(list_y):
    for maximum in list_y:
        max_r = maximum + 1
    starttime = time.time()
    for i in list_y:
        yield i
        _ = os.system("cls")  # clear for unix, cls for windows
        # _=os.system("clear")
        elapsed_time = time.time() - starttime
        estimated_time = (max_r - i) * (elapsed_time / i) if i > 0 else float('inf')
        progress = int((i * bar_width) / max_r)
        fill = bar_width - 1 - progress
        print(
            f"ETA: {estimated_time:.2f} s [{round(((i * 100) / max_r)):3}%] [{progress * '='}>{fill * ' '}] {i + 1}/{max_r} | elapsed time {elapsed_time:.2f}s")


listy = range(1000)
print(listy)
ret = 0
print(ft_progress(listy))
for elem in ft_progress(listy):
    ret += (elem + 3) % 5
    time.sleep(0.01)
print()
print(ret)
