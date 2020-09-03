# **************************************************************************** #
#                                                                              #
#                                                         ::::::::             #
#    book.py                                            :+:    :+:             #
#                                                      +:+                     #
#    By: pde-bakk <pde-bakk@student.codam.nl>         +#+                      #
#                                                    +#+                       #
#    Created: 2020/09/01 16:03:22 by pde-bakk      #+#    #+#                  #
#    Updated: 2020/09/02 18:55:58 by pde-bakk      ########   odam.nl          #
#                                                                              #
# **************************************************************************** #

from datetime import date
from recipe import Recipe


class Error(Exception):
	"""Base class for exceptions"""
	pass


class RecipeException(Error):
	"""Raised when the supplied recipe is invalid"""
	pass


class Book:
	def __init__(self, name: str):
		self.name = name
		self.last_update = date.today()
		self.creation_date = date.today()
		self.recipes_list = {
			"starter": [],
			"lunch": [],
			"dessert": []
		}

	def get_recipe_by_name(self, name):
		"""Print a recipe with the name 'name' and return the instance"""
		for type in self.recipes_list:
			for rec in self.recipes_list[type]:
				if rec.name == name:
					return rec
		print(f"Unfortunately, {name} does not exist in this book")
		pass
	
	def	get_recipes_by_types(self, recipe_type):
		"""Get all recipe names for a given recipe_type """
		for type in self.recipes_list:
			if type == recipe_type:
				return self.recipes_list[type]
		print(f"Unfortunately, {recipe_type} is not a valid recipe type in this book")
		pass
	
	def add_recipe(self, recipe):
		"""Add a recipe to the book and update last_update"""
		try:
			if not isinstance(recipe, Recipe):
				raise RecipeException
		except RecipeException:
			print("If you want to add a recipe, please supply a valid one...")
			exit(1)
		self.recipes_list[recipe.recipe_type].append(recipe)
		self.last_update = date.today()
		pass
