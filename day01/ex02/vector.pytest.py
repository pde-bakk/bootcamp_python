
class Vector:
	def __init__(self, arg):
		self.values = list()
		if isinstance(arg, int):
			for i in range(arg):
				self.values.append(float(i))
		elif isinstance(arg, tuple):
			for i in range(arg[0], arg[1]):
				self.values.append(float(i))
		elif isinstance(arg, list) and isinstance(arg[0], float):
			self.values = arg
		self.size = len(self.values)

	def print(self):
		print("(Vector ", self.values, ")", sep="")

	def __add__(self, other):
		try:
			out = list()
			if type(other) == int:
				for i in self.values:
					out.append(i + other)
				return Vector(out)
			if len(self.values) != len(other.values):
				raise IndexError
			for i in range(self.size):
				out.append(self.values[i] + other.values[i])
			return Vector(out)
		except IndexError:
			print("Error. Vectors are not of equal length")

	def __radd__(self, other):
		return self + other

	def __sub__(self, other):
		try:
			out = list()
			if type(other) == int:
				for i in self.values:
					out.append(i - other)
				return Vector(out)
			if len(self.values) != len(other.values):
				raise IndexError
			for i in range(self.size):
				out.append(self.values[i] - other.values[i])
			return Vector(out)
		except IndexError:
			print("Error. Vectors are not of equal length")

	def __rsub__(self, other):
		return self - other

	def __truediv__(self, other):
		try:
			out = list()
			for n in self.values:
				out.append(n / other)
			return out
		except ValueError:
			print("Error. Whats going on here")

	def __rtruediv__(self, other):
		return self / other

	def __mul__(self, other):
		try:
			out = list()
			for n in self.values:
				out.append(n * other)
			return out
		except ValueError:
			print("Error. Whats going on here")

	def __rmul__(self, other):
		return self * other

	def __str__(self):
		out = "(Vector "
		out += str(self.values)
		return out + ")"

	def __repr__(self):
		out = "{" + "values: " + str(self.values) \
			+ ", size: " + str(self.size) + "}"
		return out


V1 = Vector([0.0, 1.0, 2.0, 3.0])
V2 = Vector(3)
V3 = Vector((10, 15))

V1.print()
V2.print()
V3.print()

print(V1 + V2)
print(V2 - V3)
print(V1 - V1)
print(V3 * 3)
print(V2 / 2)
print(str(V2))
