import pytest
from conditionals.meal import convert

testdata = [
    ('7:00','breakfast time'),
    ('12:34','lunch time'),
    ('18:00','dinner time'),
    ('19:01','nothing'),
]

@pytest.mark.parametrize("time,expected", testdata)
def test_deep(time, expected):
    # Add your test cases here
    result = convert(time)
    assert expected == result