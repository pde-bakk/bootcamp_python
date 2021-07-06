# in the_bank.py

class Account(object):
	ID_COUNT = 1

	def __init__(self, name, **kwargs) -> None:
		self.id = self.ID_COUNT
		self.name = name
		self.__dict__.update(kwargs)
		if hasattr(self, 'value'):
			self.value = 0
		Account.ID_COUNT += 1

	def transfer(self, amount) -> None:
		self.value += amount

	def is_corrupted(self) -> bool:
		if len(self.__dict__) % 2 == 1:
			return True
		if any(map(lambda x: x.startswith(('b', 'zip', 'addr')), self.__dict__)):
			return True
		# for attr in self.__dict__:
		# 	if attr.startswith(('b', 'zip', 'addr')):
		# 		return True
		if not {'name', 'id', 'value'}.issubset(self.__dict__):
			return True
		return False

	def fix(self) -> bool:
		if not self.is_corrupted():
			return True

		self.__dict__ = {k: v for k, v in self.__dict__.items() if not k.startswith(('b', 'zip', 'addr'))}
		self.__dict__.setdefault('name', 'Peer')
		if self.__dict__.get('id') != self.__dict__.setdefault('id', Account.ID_COUNT):
			Account.ID_COUNT += 1
		self.__dict__.setdefault('value', 0)
		if len(self.__dict__) % 2 == 1:
			if 'dummy' in self.__dict__:
				del self.__dict__['dummy']
			else:
				self.__dict__.setdefault('dummy')
		return not self.is_corrupted()


class Bank(object):
	"""The bank"""

	def __init__(self) -> None:
		self.account = []

	def add(self, account) -> None:
		self.account.append(account)

	def transfer(self, origin, dest, amount) -> bool:
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
		if origin_acc is None or dest_acc is None:
			print(f'Could not find account')
			return False
		if (origin_acc.is_corrupted() and not origin_acc.fix()) or (dest_acc.is_corrupted() and not dest_acc.fix()):
			print(f'Could not fix account')
			return False
		if amount > origin_acc.value:
			print(
				f'Not enough money, origin account only has {origin_acc.value} money and you try to transfer {amount} money')
			return False
		dest_acc.transfer(amount)
		origin_acc.transfer(-amount)
		return True

	def fix_account(self, account) -> bool:
		"""
			fix the corrupted account
			@account: int(id) or str(name) of the account
			@return         True if success, False if an error occured
		"""
		for a in self.account:
			if (type(account) is int and a.id == account) or (type(account) is str and a.name == account):
				return a.fix()
		return False
