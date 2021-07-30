'''
__init__.py help us to create files with same filename in multiple sub directories
when we create python package, __init__.py is automatically created

Always use test in file name to create a pytest file ex: test_filename or filename_test, because pytest will automatically
identify test files or else we have to explicitly tell pytest about the test files

if you want to share this project with anyone then we have to share the packages (pytest) we are using with them,
to do that we can run below statement,

>. pip freeze >requirements.txt

all the packages will be listed in requirements.txt file and we can share this with anyone who want to work on this project

Note: you can run just single test by placing cursor anywhere near the braces () near test name and run.
'''

def test_a1():
    assert 5 + 5 == 10        # assert statement is used to validate if LHS = RHS
    assert 5 - 5 == 0         # we should not use multiple assert in single test, each test should be testing only one scenario
    assert 5 / 5 == 1         # this test is only for demo purpose so we are using multiple assertions here
    assert 5 * 5 == 25
'''
when you run above function alone, in output we will see "1 passed" because we are running only one function or test
'''
def test_a2():
    assert 9/5 == 1.5, "failed test intentionally"   # we can also put our comment in ""
# when u run both functions we will see 1 failed, 1 passed in o/p

def test_a3():
    assert 9//5 == 1


'''
when u want to run this in cmd prompt,
got to cmd and run,
venv\Scripts\activate           # this will activate virtual environment

and then run the code,
pytest -v pytest_topics

'''