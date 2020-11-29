import operator


class Matrix:
    """Peers matrix class"""
    def __init__(self, arg):
        self.data = list()
        if isinstance(arg, tuple):
            self.shape = arg
            for i in range(self.shape[1]):
                row = [0.0] * self.shape[0]
                self.data.append(row)
        elif isinstance(arg, list):
            listlength = len(arg[0])
            for a in arg:
                if len(a) != listlength:
                    raise ValueError
                self.data.append(a)
            self.shape = len(arg), len(arg[0])

    def print(self):
        print("Matrix", self.data)

    def __add__(self, other):
        try:
            if self.shape != other.shape:
                raise ValueError
            data = list()
            for r in range(self.shape[0]):
                data.append(list(map(sum, zip(self.data[r], other.data[r]))))
            return Matrix(data)
        except ValueError:
            print("Unable to add matrices of different dimensions")

    def __radd__(self, other):
        return self + other

    def __sub__(self, other):
        try:
            if self.shape != other.shape:
                raise ValueError
            data = list()
            for r in range(self.shape[0]):
                data.append(list(map(operator.sub, self.data[r], other.data[r])))
            return Matrix(data)
        except ValueError:
            print("Unable to subtract matrices of different dimensions")

    def __mul__(self, other):
        try:
            if self.shape[1] != other.shape[0]:
                raise ValueError
            data = list()
            for i in range(self.shape[0]):
                temp = list()
                for j in range(other.shape[1]):
                    s = 0
                    for k in range(self.shape[1]):
                        s += self.data[i][k] * other.data[k][j]
                    temp.append(s)
                data.append(temp)
            return Matrix(data)
        except ValueError:
            print("To multiply to matrices a * b, a needs to have as many columns as b does rows")

    def __rmul__(self, other):
        return self * other

    def __truediv__(self, other):
        try:
            if self.shape[1] != other.shape[0]:
                raise ValueError
            data = list()
            for i in range(0, self.shape[0]):
                temp = []
                for j in range(0, other.shape[1]):
                    s = 0
                    for k in range(0, self.shape[0]):
                        s += self.data[i][k] / other.data[k][j]
                    temp.append(s)
                data.append(temp)
            return Matrix(data)
        except ValueError:
            print("To multiply to matrices a * b, a needs to have as many columns as b does rows")

    def __rtruediv__(self, other):
        return self / other

    def __str__(self):
        out = "(Matrix "
        out += str(self.data)
        return out + ")"

    def __repr__(self):
        out = "{" + "Matrix: " + str(self.data) \
              + ", shape: " + str(self.shape) + "}"
        return out
