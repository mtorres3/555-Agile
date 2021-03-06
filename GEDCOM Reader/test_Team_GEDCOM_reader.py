import unittest
from Team_GEDCOM_reader import *
from functions import *
from extra_functions import *

class TestGEDCOMReader(unittest.TestCase):

    #Checking marriage befpre death
    def test_marr_before_div(self):
        self.assertTrue(families[0].divorced == "2003-02-18", msg="Error1")
        self.assertTrue(families[1].divorced == "INVALID DATE", msg="Error2")
        self.assertTrue(families[2].divorced == "NA", msg="Error3")
        self.assertTrue(families[3].divorced == "NA", msg="Error4")
        self.assertTrue(families[4].divorced == "2010-04-13", msg="Error5")

    #Checking marriage before death date
    def test_marr_before_deat(self):
        self.assertTrue(families[0].married == "1992-03-22", msg="Error1")
        self.assertTrue(families[1].married == "INVALID DATE", msg="Error2")
        self.assertTrue(families[2].married == "1969-02-2", msg="Error3")
        self.assertTrue(families[3].married == "INVALID DATE", msg="Error4")
        self.assertTrue(families[4].married == "1994-04-13", msg="Error5")

    #Checking Individuals existence
    def test_individual(self):
        self.assertIsNotNone(individuals[-1], msg=None)

    #Seeing if Birth Date Exists
    def test_birtCheck(self):
        self.assertTrue(birt_date, msg=None)

    #Seeing if Birth Date fills to date time correctly
    def test_birtDate(self):
        self.assertIsNotNone(birt_date, msg=None)

    #Seeing if Death Date Exists
    def test_deatCheck(self):
        self.assertTrue(deat_date, msg=None)

    #Seeing if Death Date fills to date time correctly
    def test_deatDate(self):
        self.assertIsNotNone(deat_date, msg=None)
        
    # Checks to see if individual ID matches the GEDCOM file
    def test_individual_ID(self):
        self.assertEqual(individuals[0].ID, "I1")

    # Checks to see if fam ID matches GEDCOM file, as well as the husband and wife IDs and Names.
    def test_family_ID(self):
        self.assertEqual(families[0].ID, "F1")
        self.assertEqual(families[0].husband_id, "I2")
        self.assertEqual(families[0].wife_id, "I3")

    # Testing to see if Children match to the correct family
    def test_family_children(self):
        self.assertEqual(families[1].ID, "F2")
        self.assertEqual(families[1].children, ["I2", "I8", "I9",'I25', 'I24', 'I23'])

    # Testing to ensure Unique Individual IDs
    def test_unique_individual_IDs(self):
        unique_IDs = []
        for num in range(len(individuals)):
            unique_IDs.append(individuals[num].ID)
        for ID in range(len(unique_IDs)):
            self.assertEqual(unique_IDs.count(unique_IDs[ID]), 1)

    # Testing to ensure Unique Family IDs
    def test_unique_family_IDs(self):
        unique_Fam_IDs = []
        for num in range(len(families)):
            unique_Fam_IDs.append(families[num].ID)
        for ID in range(len(unique_Fam_IDs)):
            self.assertEqual(unique_Fam_IDs.count(unique_Fam_IDs[ID]), 1)

    # Testing to ensure that each role has the proper gender
    def test_gender_for_role(self):
        self.assertEqual(individuals[1].gender, "M")
        self.assertEqual(individuals[2].gender, "F")

    # Testing to ensure that the input line is numbered correctly
    def test_input_line_number(self):
        self.assertEqual(line_count, len(families)+len(individuals))

    # Testing to ensure there is a 15 child limit
    def test_fifteen_children_limit(self):
        self.assertEqual(families[1].children, ["I2", "I8", "I9",'I25', 'I24', 'I23'])
        self.assertEqual(families[4].children, ['I14', 'I11'])

    # Testing invalidation of sibling marriages
    def test_siblings_marriage(self):
        self.assertEqual(families[4].children, ['I14', 'I11'])
        self.assertEqual(individuals[10].spouse, "INVALID SPOUSE")
        self.assertEqual(individuals[13].spouse, "INVALID SPOUSE")

    # Testing to ensure there is an parent vs. child age difference limit
    def test_old_parents(self):
        birth_parent = datetime.datetime.strptime(individuals[1].birthday, '%Y-%m-%d')
        birth_child = datetime.datetime.strptime(individuals[0].birthday, '%Y-%m-%d')
        #29497 days is equal to 80.814 years
        self.assertEqual(birth_child - birth_parent, datetime.timedelta(days=29497))
        self.assertEqual(individuals[0].age, "INVALID AGE")

    #Testing to make sure that all of the last names are the same
    def test_same_last_name(self):
        self.assertEqual(individuals[0].name, 'INVALID LAST NAME')
    
    # Testing to see if deceased individuals are printed correctly
    #def test_list_deceased(self):
        #printDead(individuals)
        #self.assertTrue(len(Deceased), 5)
        
if __name__ == '__main__':
    unittest.main()                        
