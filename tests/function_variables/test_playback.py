from function_variables.playback import playback

string_input = "This is Killarney Heights!"
string_output = "This...is...Killarney...Heights!"

def test_indoor(monkeypatch, capsys):
    monkeypatch.setattr('builtins.input', lambda: string_input)
    playback()
    captured = capsys.readouterr()
    assert captured.out.strip()  == string_output
