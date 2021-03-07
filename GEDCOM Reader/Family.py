class Family:
    def __init__(self, ID = "", Married = "Date Not Found", Divorced = "NA", Husband_ID = "", Husband_Name = "", Husband_death_date = "NA" ,Wife_ID = "", Wife_Name = "", Wife_death_date = "NA", Children = None):
        self.ID = ID # String
        self.married = Married # String
        self.divorced = Divorced # String
        self.husband_id = Husband_ID # String
        self.husband_name = Husband_Name # String
        self.husband_death_date = Husband_death_date # String
        self.wife_id = Wife_ID # String
        self.wife_name = Wife_Name # String
        self.wife_death_date = Wife_death_date # String
        if Children is None:
            Children = []
        self.children = Children # List