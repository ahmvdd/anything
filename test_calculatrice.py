from calculatrice import addition, soustraction

def test_addition():
    assert addition(2, 3) == 5
    assert addition(-1, 1) == 0

def test_soustraction():
    assert soustraction(10, 5) == 5
    assert soustraction(0, 7) == -7