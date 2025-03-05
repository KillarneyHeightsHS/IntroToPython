import pytest
from function_variables.gst import calculate_gst

testdata = [
    ('$100', '10%', 10.0),
    ('$340.55', '15%', 51.08),
    ('$65.23', '17%', 11.09),
]

@pytest.mark.parametrize("price,percent,expected", testdata)
def test_relativity(price, percent, expected):
    # Add your test cases here
    result = calculate_gst(price, percent)
    assert expected == round(result, 2)