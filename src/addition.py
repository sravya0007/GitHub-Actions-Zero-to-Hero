# app.py
# This is a test commit
def add(a, b):
    return a + b

def test_add():
    assert add(1, 5) == 6
    assert add(1, -1) == 0
