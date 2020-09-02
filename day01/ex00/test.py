# **************************************************************************** #
#                                                                              #
#                                                         ::::::::             #
#    test.py                                            :+:    :+:             #
#                                                      +:+                     #
#    By: pde-bakk <pde-bakk@student.codam.nl>         +#+                      #
#                                                    +#+                       #
#    Created: 2020/09/01 16:04:29 by pde-bakk      #+#    #+#                  #
#    Updated: 2020/09/02 19:22:52 by pde-bakk      ########   odam.nl          #
#                                                                              #
# **************************************************************************** #

from book import Book
from recipe import Recipe

myBook = Book("myBook")
try:
	SpeculaasTaart = Recipe("Speculaas taart", 3, 45, ("Speculaas", "boter", "creme fraiche", "eieren", "suiker"), "dessert", "goed lekkere taart Freddy")
	Pasta = Recipe("Pasta", 1, 20, ("Literally", "Just", "Pasta"), "starter")
	Kapsalon = Recipe("kapsalon", 5, 10, ("Fries", "Salad", "Doner", "Sauce"), "lunch")
	InvalidRecipe = Recipe("idk", 0, 283, ("not", "a", "valid", "recipe"), "dessert")
except:
	pass
myBook.add_recipe(SpeculaasTaart)
myBook.add_recipe(Pasta)
# myBook.add_recipe(InvalidRecipe)
myBook.add_recipe(Kapsalon)
print(str(myBook.get_recipe_by_name("kapsalon")))


