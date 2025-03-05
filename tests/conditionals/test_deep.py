import pytest
from conditionals.deep import deep_thought

testdata = [
    ('42', True),
    ('forty-two', True),
    ('Forty TWO', True),
    ('24', False),
    ('not 42', False),
]

@pytest.mark.parametrize("answer,expected", testdata)
def test_deep(answer, expected):
    # Add your test cases here
    result = deep_thought(answer)
    assert expected == result