import exo9

# content of test_sample.py
def inc(x):
    return x + 1


def test_answer():
    # test KO avec cet assert
    assert inc(3) == 5
    # test OK avec cet assert
    # assert inc(4) == 5

def test_exo9():
    assert exo9.est_premier(5) #== True
    assert exo9.est_premier(6) #== False
    assert exo9.est_premier(7) #== True
    assert exo9.est_premier(8) #== False