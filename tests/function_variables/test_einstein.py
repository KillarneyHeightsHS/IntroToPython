import pytest
from function_variables.einstein import relativity

testdata = [
    (1, 90000000000000000),
    (14, 1260000000000000000),
    (45, 4.05e+18)
]

@pytest.mark.parametrize("input, expected", testdata)
def test_relativity(input, expected):
    # Add your test cases here
    result = relativity(input)
    assert expected == result
