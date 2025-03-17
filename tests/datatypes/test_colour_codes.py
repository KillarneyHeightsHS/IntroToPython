# test_datatypes_colour_codes.py

import pytest
from datatypes.colour_codes import rgb_to_hex

@pytest.mark.parametrize("r, g, b, expected", [
    (255, 0, 0, "#FF0000"),
    (135, 206, 235, "#87CEEB"),
    (0, 0, 0, "#000000"),
    (255, 255, 255, "#FFFFFF"),
    (128, 128, 128, "#808080")
])
def test_rgb_to_hex(r, g, b, expected):
    result = rgb_to_hex(r, g, b)
    assert result == expected