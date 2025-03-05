from function_variables.indoor import indoor

string_input = "Hello, world2!"

def test_indoor(monkeypatch, capsys):
    monkeypatch.setattr('builtins.input', lambda: string_input)
    indoor()
    captured = capsys.readouterr()
    assert captured.out.strip()  == string_input.lower()
