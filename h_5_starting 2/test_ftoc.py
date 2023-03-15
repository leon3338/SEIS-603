#
# test_ftoc.py -> h5-2
#

# Be sure to copy your f2c() function from h5-1 below!

def f2c(fahr):
    return 0.0

# Your ten test functions of f2c() should follow:

def test_boiling_fahr():
    assert f2c(212.0) == 100.0

def test_freezing_fahr():
    assert f2c(32.0) == 0.0

def test_minus_40():
    assert f2c(-40.0)==-40.0
