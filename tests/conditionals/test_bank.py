import pytest
from conditionals.bank import greeting

testdata = [
    ('Hello', 0),
    ('Hello, Newman', 0),
    ('G`day', 100),
    ('howzit', 20),
]

@pytest.mark.parametrize("greet,expected", testdata)
def test_deep(greet, expected):
    # Add your test cases here
    result = greeting(greet)
    assert expected == result