import unittest
from Team_GEDCOM_reader import *

class TestGEDCOMReader(unittest.TestCase):
    
    '''
    WE NEED TO MAKE MASTER GEDCOM FILE FOR TESTING PURPOSE, MAKE TESTS ONLY ON THIS FILE (DO THIS IN REFACTORING MEETING)
    def test_marr_before_div(self):
        self.assertTrue(families[0].divorced == "1975-09-13", msg="Error1")
        self.assertTrue(families[1].divorced == "1980-10-13", msg="Error2")
        self.assertTrue(families[2].divorced == "1980-09-14", msg="Error3")
        self.assertTrue(families[3].divorced == "1980-09-13", msg="Error4")
        self.assertTrue(families[4].divorced == "INVALID DATE", msg="Error5")
    
    def test_marr_before_deat(self):
        self.assertTrue(families[0].married == "INVALID DATE", msg="Error1")
        self.assertTrue(families[1].married == "1980-09-13", msg="Error2")
        self.assertTrue(families[2].married == "1980-09-13", msg="Error3")
        self.assertTrue(families[3].married == "INVALID DATE", msg="Error4")
        self.assertTrue(families[4].married == "INVALID DATE", msg="Error5")
    '''

    # Test whether invalid birth date is caught
    # def test_birtTest(self):
    #     obj1 = individuals[0].birthday
    #     obj2 = 'INVALID DATE'
    #     message = 'Test failed, these two parameters are not equal.'
    #     self.assertEqual(obj1, obj2, message)

    # Test whether invalid death date is caught
    # def test_deatTest(self):
    #     obj1 = individuals[1].death
    #     obj2 = 'INVALID DATE'
    #     message = 'Test failed, these two parameters are not equal.'
    #     self.assertEqual(obj1, obj2, message)

    # # Test whether invalid marriage date is caught
    # def test_marrTest(self):
    #     obj1 = families[0].married
    #     obj2 = 'INVALID DATE'
    #     message = 'Test failed, these two parameters are not equal.'
    #     self.assertEqual(obj1, obj2, message)

    # Test whether invalid divorce date is caught
    def test_divTest1(self):
        obj1 = families[5].divorced
        obj2 = 'INVALID DATE'
        message = 'Test failed, these two parameters are not equal.'
        self.assertEqual(obj1, obj2, message)

    # # Test whether valid divorce date is outputted
    # def test_divTest2(self):
    #     obj1 = families[4].divorced
    #     obj2 = '2010-04-13'
    #     message = 'Test failed, these two parameters are not equal.'
    #     self.assertEqual(obj1, obj2, message)


    #Checking Individuals existence
    def test_individual(self):
    	self.assertIsNotNone(individuals[-1], msg=None)

    #Seeing if Birth Date Exists
    def test_birtCheck(self):
    	self.assertTrue(birt_check, msg=None)

    #Seeing if Birth Date fills to date time correctly
    def test_birtDate(self):
    	self.assertIsNotNone(birt_obj, msg=None)

    #Seeing if Death Date Exists
    def test_deatCheck(self):
    	self.assertTrue(deat_check, msg=None)

    #Seeing if Death Date fills to date time correctly
    def test_deatDate(self):
    	self.assertIsNotNone(deat_obj, msg=None)

        
if __name__ == '__main__':
    unittest.main()                        
