import pytest
from calculator import multiply

def test_multiply_positive():
    # Expect 3 * 4 == 12, but current implementation returns 7
    assert multiply(3, 4) == 12

def test_multiply_negative():
    # Expect -2 * 3 == -6, but current implementation returns 1
    assert multiply(-2, 3) == -6