import pytest
from conditionals.extension import extension

testdata = [
    ('happy.jpg','image/jpeg'),
    ('document.pdf', 'application/pdf'),
    ('python.exe', 'application/octet-stream'),
    ('download.ZIP', 'application/zip'),
    (' image.png ', 'image/png'),
]

@pytest.mark.parametrize("filename,expected", testdata)
def test_deep(filename, expected):
    # Add your test cases here
    result = extension(filename)
    assert expected == result