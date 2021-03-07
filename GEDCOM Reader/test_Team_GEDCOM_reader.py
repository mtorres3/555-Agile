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
        
    # Checks to see if individual ID matches the GEDCOM file
    def individual_ID(self):
        self.assertEqual(fil.individuals[0].ID, "I1")
        self.assertEqual(fil.individuals[0].name, "Jonathan Cucci")

    # Checks to see if fam ID matches GEDCOM file, as well as the husband and wife IDs and Names.
    def family_ID(self):
        self.assertEqual(fil.families[0].ID, "F1")
        self.assertEqual(fil.families[0].husband_id, "I1")
        self.assertEqual(fil.families[0].husband_name, "Jonathan Cucci")
        self.assertEqual(fil.families[0].wife_id, "I2")
        self.assertEqual(fil.families[0].wife_name, "Valery Dzevel")

    # Testing to see if Children match to the correct family
    def family_children(self):
        self.assertEqual(fil.families[1].ID, "F2")
        self.assertEqual(fil.families[1].children, ["I1", "I5"])
        self.assertEqual(fil.families[1].husband_name, "Michael Cucci")
        self.assertEqual(fil.families[1].wife_name, "Katherine Isacson")

    # Testing to ensure Unique Individual IDs
    def unique_individual_IDs(self):
        unique_IDs = []
        for num in range(len(fil.individuals)):
            unique_IDs.append(fil.individuals[num].ID)
        for ID in range(len(unique_IDs)):
            self.assertEqual(unique_IDs.count(unique_IDs[ID]), 1)

    # Testing to ensure Unique Family IDs
    def unique_family_IDs(self):
        unique_Fam_IDs = []
        for num in range(len(fil.families)):
            unique_Fam_IDs.append(fil.families[num].ID)
        for ID in range(len(unique_Fam_IDs)):
            self.assertEqual(unique_Fam_IDs.count(unique_Fam_IDs[ID]), 1)

        
if __name__ == '__main__':
    unittest.main()                        
