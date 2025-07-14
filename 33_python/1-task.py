import unittest
from module import Rectangle   

class TestRec(unittest.TestCase):
    def setUp(self):
        self.rect = Rectangle(2, 10)
        print("Setup method")
    def tearDown(self):
        print("Teardown method")
        self.rect = None
    def test_area(self):
        area = 20
        self.assertEqual(self.rect.area(), area, "Area calculation is incorrect")

    def test_perimeter(self):
        perimeter = 24
        self.assertEqual(self.rect.perimeter(), perimeter, "Perimeter calculation is incorrect")

    def test_area(self):
        area = 201
        self.assertEqual(self.rect.area(), area, "Area calculation is incorrect")
    
if __name__ == "__main__":
    unittest.main()
