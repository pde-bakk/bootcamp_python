# **************************************************************************** #
#                                                                              #
#                                                         ::::::::             #
#    recipe.py                                          :+:    :+:             #
#                                                      +:+                     #
#    By: pde-bakk <pde-bakk@student.codam.nl>         +#+                      #
#                                                    +#+                       #
#    Created: 2020/08/28 14:53:12 by pde-bakk      #+#    #+#                  #
#    Updated: 2020/08/30 14:13:18 by pde-bakk      ########   odam.nl          #
#                                                                              #
# **************************************************************************** #

def print_menu():
	print("Please select an option by typing the corresponding number:")
	print("1: Add a recipe")
	print("2: Delete a recipe")
	print("3: Print a recipe")
	print("4: Print the cookbook")
	print("5: Quit")

def	get_input():
	print(">> ", end='')
	cmd = input()
	print()
	try:
		cmd = int(cmd)
	except ValueError:
		pass
		print("This option does not exist, please type the corresponding number.")
		return get_input()
	if (cmd < 1 or cmd > 5):
		print("This option does not exist, please type the corresponding number.")
		return get_input()
	return cmd

def	add_recipe():
	print("Recipe name:", ">> ", sep='\n', end='')
	key = input()
	print("Ingredients (separated by comma's):", ">> ", sep='\n', end='')
	ingredients = input().split(',')
	print("What kind of food is it (lunch, breakfast, dinner, snack, etc...):", ">> ", sep='\n', end='')
	type = input()
	print("How many minutes does it take to prepare:", ">> ", sep='\n', end='')
	duration = input()
	cookbook[key] = [ingredients, type, duration]
	
	
def print_recipe():
	print("Please enter the recipe's name to get its details:", ">> ", sep='\n', end='')
	item = input()
	if item in cookbook:
		print("Recipe for", item, end=":\n")
		print("Ingredients list:", cookbook[item][0])
		print("To be eaten for", cookbook[item][1], end=".\n")
		print("Takes", cookbook[item][2], "minutes of cooking.")
	else:
		print("key does not exist in dictionary")

def print_cookbook():
	for item in cookbook:
		print("Recipe for", item, end=":\n")
		print("Ingredients list:", cookbook[item][0])
		print("To be eaten for", cookbook[item][1], end=".\n")
		print("Takes", cookbook[item][2], "minutes of cooking.")
		print()

def	exec_cmd(cmd):
	if (cmd == 1):
		add_recipe()
	if (cmd == 2):
		print("Please enter the recipe's name you wish to delete:", ">> ", sep='\n', end='')
		check = input()
		if check in cookbook:
			del cookbook[check]
	if (cmd == 3):
		print_recipe()
	if (cmd == 4):
		print_cookbook()
	if (cmd == 5):
		print("Cookbook closed.")
		exit()

cookbook = dict()
cookbook["sandwich"] = [["bread", "ham", "cheese", "tomatoes"], "lunch", 10]
cookbook["cake"] = [["flour", "sugar", "eggs"], "dessert", 60]
cookbook["salad"] = [["avocado", "arugula", "tomatoes", "spinach"], "lunch", 15]
while (1):
	print_menu()
	cmd = get_input()
	exec_cmd(cmd)
	print()
