# **************************************************************************** #
#                                                                              #
#                                                         ::::::::             #
#    exec.py                                            :+:    :+:             #
#                                                      +:+                     #
#    By: pde-bakk <pde-bakk@student.codam.nl>         +#+                      #
#                                                    +#+                       #
#    Created: 2020/08/26 19:38:35 by pde-bakk      #+#    #+#                  #
#    Updated: 2020/08/27 16:00:01 by pde-bakk      ########   odam.nl          #
#                                                                              #
# **************************************************************************** #

import sys

s = sys.argv[1:]
s.reverse()
for i in s:
	print(i[::-1].swapcase(), sep=' ', end='')
print()
