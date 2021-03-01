import unittest
from Team_GEDCOM_reader import *

# Testing US01, Dates before current date

class test_TEAM_GEDCOM_reader(unittest.TestCase):
    
    # Test whether invalid birth date is caught
    def test_birtTest(self):
        obj1 = individuals[0].birthday
        obj2 = '2023-07-9 - INVALID DATE - BIRTH DATE AFTER CURRENT DATE'
        message = 'Test failed, these two parameters are not equal.'
        self.assertEqual(obj1, obj2, message)

    # Test whether invalid death date is caught
    def test_deatTest(self):
        obj1 = individuals[1].death
        obj2 = '2030-04-10 - INVALID DATE - DEATH DATE AFTER CURRENT DATE'
        message = 'Test failed, these two parameters are not equal.'
        self.assertEqual(obj1, obj2, message)
    
    # Test whether invalid marriage date is caught
    def test_marrTest(self):
        obj1 = families[0].married
        obj2 = '2022-03-22 - INVALID DATE - MARRIAGE DATE AFTER CURRENT DATE'
        message = 'Test failed, these two parameters are not equal.'
        self.assertEqual(obj1, obj2, message)
    
    # Test whether invalid divorce date is caught
    def test_divTest1(self):
        obj1 = families[1].divorced
        obj2 = '2050-01-3 - INVALID DATE - DIVORCE DATE AFTER CURRENT DATE'
        message = 'Test failed, these two parameters are not equal.'
        self.assertEqual(obj1, obj2, message)
    
    # Test whether valid divorce date is outputted
    def test_divTest2(self):
        obj1 = families[4].divorced
        obj2 = '2010-04-13'
        message = 'Test failed, these two parameters are not equal.'
        self.assertEqual(obj1, obj2, message)

if __name__ == '__main__':
    unittest.main()