
class GotCharacter:
	def __init__(got, first_name: str, is_alive: bool=True):
		got.first_name = first_name
		got.is_alive = is_alive


class Stark(GotCharacter):
	def __init__(self, first_name: str=None, is_alive:bool=True):
		super().__init__(first_name=first_name, is_alive=is_alive)
		self.family_name = "Start"
		self.house_words = "Winter is Coming"

	def print_house_words(stark):
		print(stark.house_words)

	def die(stark):
		stark.is_alive = False


class Stark(GotCharacter):
	def __init__(self, first_name: str=None, is_alive:bool=True):
		super().__init__(first_name=first_name, is_alive=is_alive)
		self.family_name = "Start"
		self.house_words = "Winter is Coming"

	def print_house_words(stark):
		print(stark.house_words)

	def die(stark):
		stark.is_alive = False


class Baratheon(GotCharacter):
	def __init__(self, first_name: str = None, is_alive:bool = True):
		super().__init__(first_name=first_name, is_alive=is_alive)
		self.family_name = "Baratheon"
		self.house_words = "Ours is the Fury"

	def print_house_words(baratheon):
		print(baratheon.house_words)

	def die(baratheon):
		baratheon.is_alive = False


class Greyjoy(GotCharacter):
	def __init__(self, first_name: str = None, is_alive:bool = True):
		super().__init__(first_name=first_name, is_alive=is_alive)
		self.family_name = "Greyjoy"
		self.house_words = "We Do Not Sow"

	def print_house_words(greyjoy):
		print(greyjoy.house_words)

	def die(greyjoy):
		greyjoy.is_alive = False


class Martell(GotCharacter):
	def __init__(self, first_name: str = None, is_alive:bool = True):
		super().__init__(first_name=first_name, is_alive=is_alive)
		self.family_name = "Martell"
		self.house_words = "Unbowed, Unbent, Unbroken"

	def print_house_words(martell):
		print(martell.house_words)

	def die(martell):
		martell.is_alive = False


class Stark(GotCharacter):
	def __init__(self, first_name: str = None, is_alive:bool = True):
		super().__init__(first_name=first_name, is_alive=is_alive)
		self.family_name = "Stark"
		self.house_words = "Winter is Coming"

	def print_house_words(stark):
		print(stark.house_words)

	def die(stark):
		stark.is_alive = False


class Tully(GotCharacter):
	def __init__(self, first_name: str = None, is_alive:bool = True):
		super().__init__(first_name=first_name, is_alive=is_alive)
		self.family_name = "Tully"
		self.house_words = "Family, Duty, Honor"

	def print_house_words(tully):
		print(tully.house_words)

	def die(tully):
		tully.is_alive = False


class Tyrell(GotCharacter):
	def __init__(self, first_name: str = None, is_alive:bool = True):
		super().__init__(first_name=first_name, is_alive=is_alive)
		self.family_name = "Tyrell"
		self.house_words = "Growing Strong"

	def print_house_words(tyrell):
		print(tyrell.house_words)

	def die(tyrell):
		tyrell.is_alive = False


class Lannister(GotCharacter):
	def __init__(self, first_name: str = None, is_alive:bool = True):
		super().__init__(first_name=first_name, is_alive=is_alive)
		self.family_name = "Lannister"
		self.house_words = "A Lannister always pays his debts"

	def print_house_words(lannister):
		print(lannister.house_words)

	def die(lannister):
		lannister.is_alive = False


Arya = Stark("Arya")
Jamie = Lannister("Jamie")
Robert = Baratheon("Robert")
Oberyn = Martell("Oberyn")
print(Arya.__dict__)
print(Jamie.__dict__)
print(Robert.__dict__)
print(Oberyn.__dict__)
Arya.print_house_words()
print(Arya.is_alive)
Arya.die()
print(Arya.is_alive)
