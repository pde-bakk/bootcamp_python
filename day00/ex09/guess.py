# **************************************************************************** #
#                                                                              #
#                                                         ::::::::             #
#    guess.py                                           :+:    :+:             #
#                                                      +:+                     #
#    By: pde-bakk <pde-bakk@student.codam.nl>         +#+                      #
#                                                    +#+                       #
#    Created: 2020/08/30 21:47:14 by pde-bakk      #+#    #+#                  #
#    Updated: 2020/08/30 21:58:17 by pde-bakk      ########   odam.nl          #
#                                                                              #
# **************************************************************************** #

import random

random.seed()
nb = random.randint(1, 99)
tries = 1
print(	"This is an interactive guessing game!",
		"You have to enter a number between 1 and 99 to find out the secret number.", 
		"Type 'exit' to end the game.",
		"Good luck!\n", sep='\n')
while (1):
	print(">> ", end='')
	guess = input()
	try:
		guess = int(guess)
	except:
		pass
		if guess.lower() == "exit":
			exit()
		else:
			print("maybe try typing a number?")
	if guess == nb:
		if nb == 42:
			print("The answer to the ultimate question of life, the universe and everything is 42.")
		if tries == 1:
			print("Congratulations! You got it on your first try!")
		else:
			print("Congratulations, you've got it!")
			print("You won in", tries, "attempts!")
		exit()
	if guess > nb:
		print("Too high!")
	else:
		print("Too low!")
	tries += 1
