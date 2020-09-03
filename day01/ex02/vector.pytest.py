
class Vector:
	def __init__(self, arg):
		if isinstance(arg, list):
			self.items = arg
		elif isinstance(arg, int):
			i = 0
			self.items = list()
			while i < arg:
				self.items.append(float(i))
				# print(f"items[{i}] = {self.items[i]}")
				i += 1
		elif isinstance(arg, tuple):
			# print("its a tuple")
			begin = arg[0]
			end = arg[1]
			self.items = list()
			while begin < end:
				self.items.append(float(begin))
				begin += 1

	def __add__(self, add):
		for i in range(len(self.items)):
			self.items[i] += add
		return self.items

	def __sub__(self, sub):
		for i in range(len(self.items)):
			self.items[i] -= sub
		return self.items

	def __str__(self):
		return "Vector " + str(self.items)

peervec = Vector([0.0, 1.0, 2.0, 3.0])
print(str(peervec))

peervec2 = Vector(4)
print(peervec2)

peervec3 = Vector((10, 15))
peervec3 += 5
print(peervec3)

