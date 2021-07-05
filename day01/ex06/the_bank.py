# in the_bank.py

class Account(object):
	ID_COUNT = 1

	def __init__(self, name, **kwargs):
		self.id = self.ID_COUNT
		self.name = name
		self.__dict__.update(kwargs)
		if hasattr(self, 'value'):
			self.value = 0
		Account.ID_COUNT += 1

	def transfer(self, amount):
		self.value += amount

	def is_corrupted(self) -> bool:
		if len(self.__dict__) % 2 == 1:
			return True
		for attr in self.__dict__:
			if attr.startswith(('b', 'zip', 'addr')):
				return True
		if not {'name', 'id', 'value'}.issubset(self.__dict__):
			return True
		return False


class Bank(object):
	"""The bank"""
	def __init__(self):
		self.account = []

	def add(self, account):
		self.account.append(account)

	def transfer(self, origin, dest, amount):
		"""
			@origin:  int(id) or str(name) of the first account
			@dest:    int(id) or str(name) of the destination account
			@amount:  float(amount) amount to transfer
			@return         True if success, False if an error occured
		"""
		origin_acc, dest_acc = None, None
		for acc in self.account:
			if (type(origin) == int and acc.id == origin) or (type(origin) == str and acc.name == origin):
				origin_acc = acc
			if (type(dest) == int and acc.id == dest) or (type(dest) == str and acc.name == dest):
				dest_acc = acc
		if origin_acc is None or dest_acc is None or not origin_acc.fix_account() or not dest_acc.fix_account():
			return False
		if amount > origin_acc.value:
			print(f'Not enough money, origin account only has {origin_acc.value} money and you try to transfer {amount} money')
			return False
		dest_acc.transfer(amount)
		origin_acc.transfer(-amount)
		return True

	def fix_account(self, account):
		"""
			fix the corrupted account
			@account: int(id) or str(name) of the account
			@return         True if success, False if an error occured
		"""
