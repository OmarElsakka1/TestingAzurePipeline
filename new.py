import pytest

def factorial(n):
    if (n == 0):
        return 1
    else:
        return n * factorial(n-1)
    

@pytest.mark.parametrize('n, expected', [
    (0,1),
    (1,1),
    (2,2),
    (3,6),
    (4,24)
])

def test_factorial(n,expected):
    assert factorial(n) == expected