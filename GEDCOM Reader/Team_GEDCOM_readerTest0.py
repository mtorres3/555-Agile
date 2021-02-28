import unittest2

class Team_GEDCOM_readerTest0(unittest2.TestCase):
	#Seeing if birt_check is True [Birth Date Exists]
	def test_birtCheck(self):
		self.assertTrue(birt_check, msg=None)

	#Seeing if deat_check is True [Death Date Exists]
	def test_deatCheck(self):
		self.assertTrue(deat_check, msg=None)

	#Seeing if an Individual's birthday is stored in Person
	def test_birtExists(self):
		self.assertIn(individuals[-1].birthday, Person(), msg=None)

	#Seeing if an Individual's deathdate is stored in Person
	def test_deatExists(self):
		self.assertIn(individuals[-1].death, Person(), msg=None)

	#Seeing if Birth date is not equal to Death Date
	def test_birtNotDeat(self):
		self.assertNotEqual(birt_obj, deat_obj, msg=None)

if __name__ == '__main__':
	unittest2.main()