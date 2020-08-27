# **************************************************************************** #
#                                                                              #
#                                                         ::::::::             #
#    kata02.py                                          :+:    :+:             #
#                                                      +:+                     #
#    By: pde-bakk <pde-bakk@student.codam.nl>         +#+                      #
#                                                    +#+                       #
#    Created: 2020/08/28 00:11:55 by pde-bakk      #+#    #+#                  #
#    Updated: 2020/08/28 00:11:55 by pde-bakk      ########   odam.nl          #
#                                                                              #
# **************************************************************************** #

import datetime as dt

t = (3,30,2019,9,25)

date = dt.datetime(month=t[3], day=t[4], year=t[2], hour=t[0], minute=t[1])
print(date.strftime("%m/%d/%y %H:%M"))
