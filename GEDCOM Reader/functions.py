
from Family import *
from Person import *

# Where id is ID to find, L is list of people

def ids_to_names(ids, L):
    names = []
    for person in L:
        if person.ID in ids:
            names = names + [person.name]
    return names

