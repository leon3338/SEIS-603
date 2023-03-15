#Andrew Leonard
# test_ftoc.py -> h5-2
#

# Be sure to copy your f2c() function from h5-1 below!
def f2c(fahr):
    celsius = (fahr-32.0) * (5/9)
    return round(celsius, 2)

# Your ten test functions of f2c() should follow:

def test_boiling_fahr():
    assert f2c(212.0) == 100.0

def test_freezing_fahr():
    assert f2c(32.0) == 0.0

def test_minus_40():
    assert f2c(-40.0)==-40.0

def test_minus_100():
    assert f2c(-100.0)==-73.33

def test_100_fahr():
    assert f2c(100.0)==37.78

def test_zero_fahr():
    assert f2c(0.0)==-17.78

def test_50_fahr():
    assert f2c(50.0)==10.00

def test_19_fahr():
    assert f2c(19.0)==-7.22

def test_1000_fahr():
    assert f2c(1000.0)==537.78

def test_1000000000_fahr():
    assert f2c(1000000000.0)== 555555537.78