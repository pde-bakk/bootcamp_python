

def generator(text, sep=" ", option=None):
	"""Option is an optional arg, sep is mandatory"""
	try:
		words = text.split(sep)
		if option == "shuffle":
			words.sort(reverse=True, key=len)
		elif option == "ordered":
			words.sort()
		if option is None or option == "shuffle" or option == "ordered":
			for each in words:
				yield each
		else:
			raise SyntaxError

	except TypeError:
		print("Must give string as parameter")
	except SyntaxError:
		print("Not a valid option: \"shuffle\" or \"ordered\"")


txt = "Le lorem Ipsum est simplement du faux texte."

# for word in generator(txt):
# 	print(word)

# for word in generator(txt, option="shuffle"):
# 	print(word)

for word in generator(txt, option="ordered"):
	print(word)

