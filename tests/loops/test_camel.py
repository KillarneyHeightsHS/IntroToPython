import pytest
from loops.camel import camel_to_snake

testdata = [
    ('name', 'name'),
    ('firstName', 'first_name'),
    ('lastName', 'last_name'),
    ('userName', 'user_name'),
    ('isUserLoggedIn', 'is_user_logged_in'),
]

@pytest.mark.parametrize("name,expected", testdata)
def test_deep(name, expected):
    # Add your test cases here
    result = camel_to_snake(name)
    assert expected == result