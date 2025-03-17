# test_converter.py

import pytest
from datatypes.converter import number_system_converter

@pytest.mark.parametrize(
    "value, from_base, to_base, expected",
    [
        ("1101", "binary", "decimal", 13),
        ("42", "decimal", "binary", "101010"),
        ("FF", "hex", "binary", "11111111"),
        ("1101", "binary", "hex", "D"),
    ],
)
def test_number_system_converter(value, from_base, to_base, expected):
    result = number_system_converter(value, from_base, to_base)
    assert result == expected

if __name__ == "__main__":
    pytest.main()