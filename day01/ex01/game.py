
class GotCharacter:
    def __init__(self, first_name, family_name, house_words, is_alive=True):
        self.first_name = first_name
        self.family_name = family_name
        self.house_words = house_words
        self.is_alive = is_alive

    def print_house_words(self):
        print(self.house_words)

    def die(self):
        self.is_alive = False


class Stark(GotCharacter):
    """A class representing the Stark family. Or when bad things happen to good people."""
    def __init__(self, first_name=None, is_alive=True, family_name="Stark", house_words="Winter is coming"):
        super().__init__(first_name=first_name, family_name=family_name, house_words=house_words, is_alive=is_alive)


class Lannister(GotCharacter):
    """Wtf happened to Tyrions story arc?"""
    def __init__(self, first_name=None, is_alive=True, family_name="Lannister", house_words="A Lannister always pays his debts"):
        super().__init__(first_name=first_name, family_name=family_name, house_words=house_words, is_alive=is_alive)


class Baratheon(GotCharacter):
    """Bobby B"""
    def __init__(self, first_name=None, is_alive=True, family_name="Baratheon", house_words="Ours is the Fury"):
        super().__init__(first_name=first_name, family_name=family_name, house_words=house_words, is_alive=is_alive)
