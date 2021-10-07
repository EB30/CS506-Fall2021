import pytest
from cs506 import matrix


A0 = [[1,2],[3,4]]
A1 = [[1,2,3],[4,5,6],[7,8,9]]
A2 = [[1,2,3],[4,5,6],[7,8]]
A3 = []
A4 = [[-1,1,2],[6,7,9],[7,4,2]]
A5 = [[-2,3,1],[0,70,1],[-5,4,2]]

print(matrix.get_determinant(A0,len(A0)))
print(matrix.get_determinant(A1, len(A1)))
print(matrix.get_determinant(A2,len(A2)))
print(matrix.get_determinant(A3, len(A3)))
print(matrix.get_determinant(A4,len(A4)))
print(matrix.get_determinant(A5, len(A5)))

def test_determinant():
    # sanity checks
    try:
        matrix.get_determinant(A3,0)
    except ValueError as e:
        assert str(e) == "the matrix cannot be empty"
    try:
        matrix.get_determinant(A2, 2)
    except ValueError as e:
        assert str(e) == "the matrix must be a n by n matrix"

    assert (matrix.get_determinant(A0,len(A0))== -2)
    assert(matrix.get_determinant(A1,len(A1))==0)
    assert (matrix.get_determinant(A4,len(A4)))
    assert(matrix.get_determinant(A5,len(A5)))

test_determinant()