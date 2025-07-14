# Python Testing & Packaging Guide

This README provides an overview of Python testing using `unittest` and `pytest`, data mocking, and packaging with `setuptools`.

## 1. Testing with `unittest`

`unittest` is Python's built-in testing framework.

**Example:**

```python
# test_math.py
import unittest

def add(a, b):
    return a + b

class TestMath(unittest.TestCase):
    def test_add(self):
        self.assertEqual(add(2, 3), 5)

if __name__ == '__main__':
    unittest.main()
```

Run tests:
```bash
python test_math.py
```

## 2. Testing with `pytest`

`pytest` is a popular third-party testing tool.

**Example:**

```python
# test_math_pytest.py
def add(a, b):
    return a + b

def test_add():
    assert add(2, 3) == 5
```

Run tests:
```bash
pytest test_math_pytest.py
```

## 3. Data Mocking

Mocking allows you to replace parts of your system under test.

**Example with `unittest.mock`:**

```python
from unittest.mock import Mock

mock = Mock()
mock.return_value = 10
assert mock() == 10
```

**Example with `pytest` fixture:**

```python
import pytest

@pytest.fixture
def mock_data():
    return {'key': 'value'}

def test_mock_data(mock_data):
    assert mock_data['key'] == 'value'
```

## 4. Packaging with `setuptools`

Create a `setup.py` file:

```python
from setuptools import setup, find_packages

setup(
    name='my_package',
    version='0.1',
    packages=find_packages(),
    install_requires=[
        # dependencies
    ],
)
```

Build and install:

```bash
python setup.py sdist bdist_wheel
pip install .
```

## References

- [unittest documentation](https://docs.python.org/3/library/unittest.html)
- [pytest documentation](https://docs.pytest.org/)
- [setuptools documentation](https://setuptools.pypa.io/en/latest/)