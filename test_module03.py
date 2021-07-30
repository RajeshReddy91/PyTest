'''
pytest.raises - exception handling in pytest

'''

import pytest

def test_case01():
    assert (1/0)        # ZeroDivisionError: division by zero

def test_case02():
    with pytest.raises(Exception):
        assert (1/0)    # testcase passed

def test_case03():
    with pytest.raises(ZeroDivisionError):  #if we know the error then we can specify it in pytest.raises()
        assert (1/0)                        # but if we specify wrong error then testcase will fail

def test_case04():
    with pytest.raises(Exception) as excinfo:
        assert (1,2,3) == (1,2,4)
    print(excinfo)                          # print the exception

def func1():                                # this func will raise error which ever we define in it
    raise ValueError("Exception func raised")

def test_case05():
    with pytest.raises(Exception) as excinfo:
        func1()
    print (str(excinfo))                          # print the exception
    assert (str(excinfo.value)) == 'Exception func raised'  # checking if the exception raised is same as the one we defined in func

##################### Catching error
def func1():                                # this func will raise error which ever we define in it
    raise ValueError("IndexError func1 raised")

def test_case05():
    with pytest.raises(Exception) as excinfo:
        func1()
    print (str(excinfo))                          # print the exception
    assert (str(excinfo.value)) == 'Exception func raised'




