from ntpy import euler_phi , mobius
def test_euler_phi():
    assert euler_phi(1) == 1
    assert euler_phi(2) == 1
    assert euler_phi(5) == 4
    assert euler_phi(10) == 4
    assert euler_phi(12) == 4
    assert euler_phi(36) == 12

def test_mobius():
    assert mobius(1) == 1

    assert mobius(2) == -1
    assert mobius(3) == -1
    assert mobius(5) == -1

    assert mobius(4) == 0
    assert mobius(9) == 0

    assert mobius(6) == 1
    assert mobius(10) == 1
    assert mobius(15) == 1

    assert mobius(12) == 0
    assert mobius(18) == 0

    assert mobius(30) == -1
