'''
when you use multiple assert in a single test, if first assert fails then the next assert will never run.
Untill top asserts are pass it will not go to next elements, hence its always better to use single assert in each test
'''

def test_a1():
    assert 4<5

def test_a2():
    assert 4!=5     # we can use any operator in assert statement

def test_a3():
    assert 1        # this will always pass(we can also use True), useful when testing a function which will return any value

def test_a4():
    assert 0        # this will always fail(we can also use False)

def test_a5():
    assert 'abc' == 'abc'   # we can compare strings

def test_a6():
    assert ((3-1)*4/2) == 4 # using expressions


# divmod(9,5) ---- o/p - (1, 4) output will have both quotient and reminder inside a tuple

def test_a7():
    assert 1 in divmod(9,5)     # it will check if 1 is present in (1, 4) or not

def test_a8():
    assert 'py' in 'this is pytest'

def test_a9():
    assert 'put' not in 'this is pytest'
    assert 4 in [1, 2, 3, 4]            # pass
    assert [1, 2] in [1,2,3,4]          # fail
    assert [1, 2] < [1, 2, 3, 4]        # pass
    assert [1, 2, 3, 4] == [1, 2, 3, 4] # pass
