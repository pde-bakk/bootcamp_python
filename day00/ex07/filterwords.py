# **************************************************************************** #
#                                                                              #
#                                                         ::::::::             #
#    filterwords.py                                     :+:    :+:             #
#                                                      +:+                     #
#    By: pde-bakk <pde-bakk@student.codam.nl>         +#+                      #
#                                                    +#+                       #
#    Created: 2020/08/30 20:36:12 by pde-bakk      #+#    #+#                  #
#    Updated: 2020/08/30 20:53:26 by pde-bakk      ########   odam.nl          #
#                                                                              #
# **************************************************************************** #

import sys
import string

if len(sys.argv) != 3:
	print("ERROR")
	exit()

words = sys.argv[1].split(' ')
try:
	length = int(sys.argv[2])
except:
	pass
	print("WTF dude, you didnt give me an integer?!?!??")
	exit()
out = [w.strip(string.punctuation) for w in words if len(w) > length]
print(out)

