# **************************************************************************** #
#                                                                              #
#                                                         ::::::::             #
#    exec.py                                            :+:    :+:             #
#                                                      +:+                     #
#    By: pde-bakk <pde-bakk@student.codam.nl>         +#+                      #
#                                                    +#+                       #
#    Created: 2020/08/26 19:38:35 by pde-bakk      #+#    #+#                  #
#    Updated: 2020/08/26 21:21:04 by pde-bakk      ########   odam.nl          #
#                                                                              #
# **************************************************************************** #

import sys

s = sys.argv[1:]
s.reverse()
# s = sys.argv[1::-1]
for i in s:
	print(i[::-1].swapcase(), end = ' ')
