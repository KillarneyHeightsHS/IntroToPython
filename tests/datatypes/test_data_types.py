# File: tests/test_datatypes.py

import pytest
from datatypes.data_types import print_data_type

@pytest.mark.parametrize("value, expected_type", [
    (123, "int"),
    ("hello", "str"),
    ('test', "str"),
    (True, "bool"),
    ([], "list"),
    ({}, "dict"),
    ((1, 2, 3), "tuple"),
    (None, "NoneType"),
    (3.14, "float")
])
def test_print_data_type(value, expected_type, capsys):
    print_data_type(value)
    
    captured = capsys.readouterr()
    assert captured.out.strip()  == expected_type

