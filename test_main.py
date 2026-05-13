import main

def test_add():
    assert main.add(2, 3) == 5
    assert main.add(-1, 1) == 0

def test_multiply():
    assert main.multiply(2, 3) == 6
    assert main.multiply(-2, 3) == -6