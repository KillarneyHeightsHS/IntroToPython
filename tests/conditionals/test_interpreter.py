import pytest
from conditionals.interpreter import calculate

testdata = [
    ('1','+','1',2.0),
    ('2','*','3',6.0),
    ('4','-','5',-1.0),
    ('6','/','2',3.0),
    ('50','/','5',10.0),
]
@pytest.mark.parametrize("x,y,z,expected", testdata)
def test_deep(x, y, z, expected):
    # Add your test cases here
    result = calculate(x, y, z)
    assert expected == result