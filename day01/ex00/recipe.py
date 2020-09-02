# **************************************************************************** #
#                                                                              #
#                                                         ::::::::             #
#    recipe.py                                          :+:    :+:             #
#                                                      +:+                     #
#    By: pde-bakk <pde-bakk@student.codam.nl>         +#+                      #
#                                                    +#+                       #
#    Created: 2020/09/01 16:04:43 by pde-bakk      #+#    #+#                  #
#    Updated: 2020/09/02 18:56:28 by pde-bakk      ########   odam.nl          #
#                                                                              #
# **************************************************************************** #

class Error(Exception):
   """Base class for other exceptions"""
   pass

class CookingLvlException(Error):
   """Raised when cooking level is invalid"""
   pass

class CookingTimeException(Error):
   """Raised when the cooking time is negative"""
   pass

class IngredientsException(Error):
   """Raised when the ingredient is not a string"""
   pass

class RecipeTypeException(Error):
   """Raised when the recipe doesnt have a valid type"""
   pass

class Recipe:
	def __init__(self, name: str, cooking_lvl: int, cooking_time: int, ingredients: tuple, recipe_type: str, description:str=""):
		try:
			if cooking_lvl <= 0 or cooking_lvl > 5: raise CookingLvlException
			if cooking_time < 0: raise CookingTimeException
			for ingredient in ingredients:
				if not isinstance(ingredient, str): raise IngredientsException
			if recipe_type != "starter" and recipe_type != "lunch" and recipe_type != "dessert": raise RecipeTypeException
		except CookingLvlException:
			print("Please enter a level between 1 and 5")
			exit(1)
		except CookingTimeException:
			print("Please enter a valid duration in minutes")
			exit(1)
		except IngredientsException:
			print("Pleaase enter a list or tuple of ingredients in string form")
			exit(1)
		except RecipeTypeException:
			print("Please enter a recipe of type \'starter\', \'lunch\' or \'dessert\'")
			exit(1)
		self.name = name
		self.cooking_lvl = cooking_lvl
		self.cooking_time = cooking_time
		self.ingredients = ingredients
		self.description = description
		self.recipe_type = recipe_type

	def __str__(self):
		txt = "Recipe name: " + self.name + '\n\t' \
			+ "Cooking level: " + str(self.cooking_lvl) + '\n\t' \
			+ "Cooking_time: " + str(self.cooking_time) + " minutes" + '\n\t' +"Ingredients: " 
		ingrs = ', '.join(stri for stri in self.ingredients)
		txt += ingrs + '\n\t' + "Description: " + self.description + '\n\t' \
			+ "Recipe_type: " + self.recipe_type + '\n'
		return txt
