# **************************************************************************** #
#                                                                              #
#                                                         ::::::::             #
#    operations.py                                      :+:    :+:             #
#                                                      +:+                     #
#    By: pde-bakk <pde-bakk@student.codam.nl>         +#+                      #
#                                                    +#+                       #
#    Created: 2020/08/27 18:39:09 by pde-bakk      #+#    #+#                  #
#    Updated: 2020/08/27 18:57:50 by pde-bakk      ########   odam.nl          #
#                                                                              #
# **************************************************************************** #

import sys

def err():
	print("Usage python operations.py <number1> <number2>")
	print("Example:")
	print("\tpython operations.py 10 3")
	exit()
	

if len(sys.argv) != 3:
	if len(sys.argv) > 3:
		print("InputError: too many arguments\n")
	err()
try:
	nb1 = int(sys.argv[1])
	nb2 = int(sys.argv[2])
except ValueError:
	pass
	print("InputError: only numbers")
	err()

print("{0:<12}".format("Sum:"), end=' ')
print(nb1 + nb2)

print("{0:<12}".format("Difference:"), end=' ')
print(nb1 - nb2)

print("{0:<12}".format("Product:"), end=' ')
print(nb1 * nb2)

print("{0:<12}".format("Quotient:"), end=' ')
print("ERROR (div by zero)") if nb2 == 0 else print(nb1 / nb2)

print("{0:<12}".format("Remainder:"), end=' ')
print("ERROR (modulo by zero)") if nb2 == 0 else print(nb1 % nb2)
