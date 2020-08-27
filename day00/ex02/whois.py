# **************************************************************************** #
#                                                                              #
#                                                         ::::::::             #
#    whois.py                                           :+:    :+:             #
#                                                      +:+                     #
#    By: pde-bakk <pde-bakk@student.codam.nl>         +#+                      #
#                                                    +#+                       #
#    Created: 2020/08/27 16:01:31 by pde-bakk      #+#    #+#                  #
#    Updated: 2020/08/27 16:24:59 by pde-bakk      ########   odam.nl          #
#                                                                              #
# **************************************************************************** #

import sys

if len(sys.argv) != 2:
	print("ERROR")
	exit()
nb = sys.argv[1]
try:
	nb = int(nb)
except ValueError:
	print("ERROR")
	pass
	exit()
if nb == 0:
	print("I'm Zero.")
elif nb % 2:
	print("I'm Odd.")
else:
	print("I'm Even")
