import pytest

from module import Rectangle

@pytest.fixture
def rect():
    r = Rectangle(2, 10)
    yield r

def test_area(rect):
    assert rect.area() == 20

def test_perimerer(rect):
    assert rect.perimeter() ==24

def test_area2(rect):
    assert rect.area() == 15