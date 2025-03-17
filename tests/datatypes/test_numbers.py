import pytest
from datatypes.numbers import binary_to_decimal_visual, decimal_to_binary_visual

@pytest.mark.parametrize("binary_num, expected", [
    ("0", 0),
    ("1", 1),
    ("10", 2),
    ("11", 3),
    ("101", 5),
    ("110", 6),
    ("1010", 10),
    ("1011", 11),
    ("1111", 15),
])
def test_binary_to_decimal_visual(binary_num, expected):
    assert binary_to_decimal_visual(binary_num) == expected

@pytest.mark.parametrize("decimal_num, expected", [
    (0, "0"),
    (1, "1"),
    (2, "10"),
    (3, "11"),
    (5, "101"),
    (6, "110"),
    (10, "1010"),
    (11, "1011"),
    (15, "1111"),
])
def test_decimal_to_binary_visual(decimal_num, expected):
    assert decimal_to_binary_visual(decimal_num) == expected