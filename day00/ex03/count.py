# **************************************************************************** #
#                                                                              #
#                                                         ::::::::             #
#    count.py                                           :+:    :+:             #
#                                                      +:+                     #
#    By: pde-bakk <pde-bakk@student.codam.nl>         +#+                      #
#                                                    +#+                       #
#    Created: 2020/08/27 17:07:11 by pde-bakk      #+#    #+#                  #
#    Updated: 2020/08/27 18:24:07 by pde-bakk      ########   odam.nl          #
#                                                                              #
# **************************************************************************** #

import string

def text_analyzer(text = ""):
	if text == "":
		print("What is the text to analyse?")
		text_analyzer(input())
		return
	char_count = uppercase = lowercase = puncts = spaces = 0
	for i in text:
		char_count += 1
		if i in string.whitespace : spaces += 1
		if i in string.punctuation: puncts += 1
		if i in string.ascii_lowercase : lowercase += 1
		if i in string.ascii_uppercase : uppercase += 1
	print("The text contains", char_count, "characters:")
	print("-", uppercase, "upper letters")
	print("-", lowercase, "lower letters")
	print("-", puncts, "punctuation marks")
	print("-", spaces, "spaces")

# text_analyzer()
