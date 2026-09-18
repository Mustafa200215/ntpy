from ntpy import crt
def test_crt():
    assert crt([5,3],[3,2])==(15,8)
    assert crt([2, 3, 5], [1, 2, 3]) == (30, 23)
    assert crt([5, 7, 11], [2, 3, 4]) == (385, 367)
    assert crt([3, 4], [2, 3]) == (12, 11)
    assert crt([4, 5], [1, 2]) == (20, 17)
    assert crt([5, 6], [2, 3]) == (30, 27)
    assert crt([7, 9], [3, 4]) == (63, 31)
    assert crt([2, 3, 5], [0, 0, 0]) == (30, 0)
