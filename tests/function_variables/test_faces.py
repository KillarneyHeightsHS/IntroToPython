from function_variables.faces import convert

def test_faces():
    # Add your test cases here
    result = convert("Hello :) Goodbye :(")
    assert "Hello 🙂 Goodbye 🙁" == result
