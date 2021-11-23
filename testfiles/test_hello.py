import sys
import pytest


sys.path.append(r'C:\Users\40010046\Desktop\Misc\pyBazel3\sourcefiles')


import hello


def test_hello_world1():
    assert hello.hello_world() == "Hello World"


if __name__ == "__main__":
    sys.exit(pytest.main([__file__]))
    #pytest.main([__file__])
    