# **************************************************************************** #
#                                                                              #
#                                                         ::::::::             #
#    kata01.py                                          :+:    :+:             #
#                                                      +:+                     #
#    By: pde-bakk <pde-bakk@student.codam.nl>         +#+                      #
#                                                    +#+                       #
#    Created: 2020/08/28 00:12:00 by pde-bakk      #+#    #+#                  #
#    Updated: 2020/08/28 00:12:00 by pde-bakk      ########   odam.nl          #
#                                                                              #
# **************************************************************************** #

languages = {
    'Python': 'Guido van Rossum',
    'Ruby': 'Yukihiro Matsumoto',
    'PHP': 'Rasmus Lerdorf',
    }

s = "was created by"
for i in languages:
	print(i, s, languages[i])
