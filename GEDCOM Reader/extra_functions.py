
from Family import *
from Person import *
from datetime import *
import datetime

# Dictionary that converts between a month and its numerical
months = {
        'JAN' : ["01", 31],
        'FEB' : ["02", 28],
        'MAR' : ["03", 31],
        'APR' : ["04", 30],
        'MAY' : ["05", 31],
        'JUN' : ["06", 30],
        'JUL' : ["07", 31],
        'AUG' : ["08", 31],
        'SEP' : ["09", 30],
        'OCT' : ["10", 31],
        'NOV' : ["11", 30],
        'DEC' : ["12", 31]}

# Tags broken down into indexes that correspond with their acceptable level number
tags = [["INDI", "FAM", "HEAD", "TRLR", "NOTE"],["NAME", "SEX", "BIRT", "DEAT", "FAMC", "FAMS", "MARR", "HUSB", "WIFE", "CHIL", "DIV"],["DATE"]]

# Where id is ID to find, L is list of people
# Converts from ID to Name

def is_Leap_Year(year):
    year = int(year)
    if (year % 4) == 0:
        if (year % 100) == 0:
            if (year % 400) == 0:
                return True
            else:
                return False
        else:
            return True
    else:
        return False

def ids_to_names(ids, L):
    names = []
    for person in L:
        if person.ID in ids:
            names = names + [person.name]
    return names

# Converts from a date string to a list of integer values
def date_string_to_list(s):
    date = s.split('-')
    date = list(map(int, date))
    return date

# Converts from a list of integer values back to date string
def date_list_to_string(L):
    L = list(map(str, L))
    for item in range(len(L)):
        if len(L[item]) == 1:
            L[item] = '0' + str(L[item])
    date = '-'.join(L)
    return date

def validate_date(L):
    print()

#validate_date(['2', 'FEB', '1969'])