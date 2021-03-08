
class Family:
    def __init__(self, ID = "", Married = "Date Not Found", Divorced = "NA", Husband_ID = "", Husband_Name = "", Wife_ID = "", Wife_Name = "", Children = None):
        self.ID = ID # String
        self.married = Married # String
        self.divorced = Divorced # String
        self.husband_id = Husband_ID # String
        self.husband_name = Husband_Name # String
        self.wife_id = Wife_ID # String
        self.wife_name = Wife_Name # String
        if Children is None:
            Children = []
        self.children = Children # List