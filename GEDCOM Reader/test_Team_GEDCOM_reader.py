import unittest
from Team_GEDCOM_reader import *

class TestGEDCOMReader(unittest.TestCase):
    '''
    def test_marr_before_div(self):
        self.assertTrue(families[0].divorced == "1975-09-13", msg="Error1")
        self.assertTrue(families[1].divorced == "1980-10-13", msg="Error2")
        self.assertTrue(families[2].divorced == "1980-09-14", msg="Error3")
        self.assertTrue(families[3].divorced == "1980-09-13", msg="Error4")
        self.assertTrue(families[4].divorced == "INVALID DATE", msg="Error5")
    '''
    def test_marr_before_deat(self):
        self.assertTrue(families[0].married == "INVALID DATE", msg="Error1")
        self.assertTrue(families[1].married == "1980-09-13", msg="Error2")
        self.assertTrue(families[2].married == "1980-09-13", msg="Error3")
        self.assertTrue(families[3].married == "INVALID DATE", msg="Error4")
        self.assertTrue(families[4].married == "INVALID DATE", msg="Error5")

        
if __name__ == '__main__':
    unittest.main()                        
