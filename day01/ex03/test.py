from matrix import Matrix

m1 = Matrix([
    [0.0, 1.0, 2.0, 3.0],
    [0.0, 2.0, 4.0, 6.0]
])

m2 = Matrix([[0.0, 1.0],
             [2.0, 3.0],
             [4.0, 5.0],
             [6.0, 7.0]])
# print("Matrix m1:")
# m1.print()
#
# print("Adding m1 and m2")
#
# (m1 + m1).print()

mul1 = Matrix([[1, 2, 3], [4, 5, 6]])
print("mul1 has shape ", mul1.shape, ":")
print(mul1)
mul2 = Matrix([[7, 8], [9, 10], [11, 12]])
print("mul2 has shape ", mul2.shape, ":")
print(mul2)

print(mul1 * mul2)

print(repr(m1))
