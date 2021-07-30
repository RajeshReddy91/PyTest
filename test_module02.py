# test class
class TestMyStuff():
    def test_type(self):
        assert type(1.3) == float

    def test_strs(self):
        assert str.upper('python') == 'PYTHON'
        assert 'python'.capitalize() == 'Python'

'''
when you want to run particular class in cmd prompt, first activate venv.
pytest -v -- will run all the test modules
pytest -v pytest_topics\test_module02.py::TestMyStuff                # TestMyStuff is a class name
pytest -v pytest_topics\test_module02.py::TestMyStuff::test_type     # TestMyStuff is a class name, test_type is a method name
'''

