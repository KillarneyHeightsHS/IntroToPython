from datatypes.translator import text_to_decimal, decimal_to_text

def test_text_to_decimal():
    # Test with a simple message
    result = text_to_decimal("hello")
    assert result == [104, 101, 108, 108, 111]

    # Test with an empty string
    result = text_to_decimal("")
    assert result == []

def test_decimal_to_text():
    # Test with a list of decimal values
    result = decimal_to_text([104, 101, 108, 108, 111])
    assert result == "hello"

    # Test with an empty list
    result = decimal_to_text([])
    assert result == ""