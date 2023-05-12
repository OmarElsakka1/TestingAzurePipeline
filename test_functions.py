import pytest
from functions import Adding 

def test_add_numbers():
    assert Adding(2, 3) == 5
    assert Adding(0, 0) == 0
    assert Adding(-1, 1) == 0




