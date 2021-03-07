class Person:
    def __init__(self, ID = "", Name = "", Gender = '', Birthday = "NA", Age = 0, Alive = True, Death = "NA", Child = None, Spouse = None):
        self.ID = ID # String
        self.name = Name # String
        self.gender = Gender # Char
        self.birthday = Birthday # String
        self.age = Age # Int
        self.alive = Alive # Boolean
        self.death = Death # String
        if Child is None:
            Child = []
        self.child = Child # List
        if Spouse is None:
            Spouse = []
        self.spouse = Spouse # List