
from Family import *
from Person import *
from datetime import *
import datetime

# Dictionary that converts between a month and its numerical
MONTHS = {
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
TAGS = (("INDI", "FAM", "HEAD", "TRLR", "NOTE"),("NAME", "SEX", "BIRT", "DEAT", "FAMC", "FAMS", "MARR", "HUSB", "WIFE", "CHIL", "DIV"),("DATE"))

# searches list L for person with ID
def ids_to_names(ids, L):
    names = []
    for person in L:
        if person.ID in ids:
            names = names + [person.name]
    return names

def id_to_person(id, L):
    for person in L:
        if id == person.ID:
            return person

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

# validates a date in the form of a string yyyy-mm-dd
def validate_date(S):
    date = date_string_to_list(S)
    try :
        datetime.datetime(date[0],date[1],date[2])
        return True
    except ValueError :
        return False

# day month year list to year-month-day
def create_DATE(L):
    return date_list_to_string([L[2], MONTHS[L[1]][0], L[0]])
