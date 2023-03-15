#
# HTT Ch 12 code example:
#
# Section 12.5, example 1: ch12_sparse
#

matrix = {(0, 3): 1, (2, 1): 2, (4, 3): 3}
print(matrix.get((0,3)))

print(matrix.get((1, 3), 0))

print(matrix)