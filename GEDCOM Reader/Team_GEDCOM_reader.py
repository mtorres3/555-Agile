'''
@Author: Jonathan Cucci, Joe Letizia, Markell Torres, Erik Buczek
SSW555 Proj-2
GEDCOM Reader
'''
from Person import *
from Family import *
import os.path
from os import path
from datetime import *
import datetime
import sqlite3
from extra_functions import *
from functions import *

#list_marr = []


# Opens GEDCOM file as fam variable
with open('Letizia_GEDTEST.ged.txt') as fam:
    text = fam.readlines()
    individuals = []
    families = []
    today = str(datetime.date.today())
    line_point = 0

    # Goes through each line of the GEDCOM file
    for line in text:
        newLine = line.split()

        # US42 Date Validation
        if ("DATE" in newLine):
            date_to_check = create_DATE(newLine[-3:])
            if not validate_date(date_to_check):
                print("Individual ID: {} | Invalid date input: {}".format(individuals[-1].ID, date_to_check))
                raise IndexError

        if ("INDI" in newLine):
            # pointer += 1
            individuals.append(Person())
            individuals[-1].ID = newLine[1][1:-1]

        elif("NAME" in newLine):
            individuals[-1].name = newLine[-2] + " " + newLine[-1][1:-1]

        elif("SEX" in newLine):
            individuals[-1].gender = newLine[-1]

        elif("BIRT" in newLine):
            next_line = line_point + 1
            next_line = text[next_line].split()
            birt_date = next_line[-1] + "-" + MONTHS[next_line[-2]][0] + "-" + next_line[-3]
            individuals[-1].birthday = create_BIRT(birt_date)

        elif("DEAT" in newLine):
            individuals[-1].alive = False
            next_line = line_point + 1
            next_line = text[next_line].split()
            deat_date = next_line[-1] + "-" + MONTHS[next_line[-2]][0] + "-" + next_line[-3]
            individuals[-1].death = create_DEAT(deat_date, next_line)
            individuals[-1] = validate_DEAT(individuals[-1])

        elif("FAM" in newLine):
            families.append(Family())
            families[-1].ID = newLine[1][1:-1]

        elif("HUSB" in newLine):
            next_line = text[line_point+1].split()
            husband(families, individuals, newLine, next_line)

        elif("WIFE" in newLine):
            wife(families, individuals, newLine)

        elif("CHIL" in newLine):
            changes = create_CHIL(families, individuals, newLine)
            individuals = changes[0]
            families = changes[1]

        elif("DIV" in newLine):
            if "DATE" in text[line_point+1].split():
                next_line = text[line_point+1].split()
                marr_date = text[line_point-1].split()
                div_date = next_line[-1] + "-" + MONTHS[next_line[-2]][0] + "-" + next_line[-3]

                check_DIV(families[-1], individuals, next_line, marr_date, div_date)
            else:
                families[-1].divorced = "Date not found"

        elif("MARR" in newLine):
            if "DATE" in text[line_point+1].split():
                next_line = text[line_point+1].split()
                marr_date_string = next_line[-1] + "-" + MONTHS[next_line[-2]][0] + "-" + next_line[-3]
                marr_date_array = [next_line[-3], MONTHS[next_line[-2]][0], next_line[-1]]

                check_MARR_after_BIRT(families[-1], individuals, next_line, marr_date_string, marr_date_array)

            #US05: Marriage before death
            check_MARR_before_DEAT(families[-1], individuals, next_line, marr_date_string, marr_date_array)


        line_point += 1

    # Updates everyones age
    for individual in individuals:

        today = date.today()
        if (individual.birthday != "INVALID DATE"):
            birth = individual.birthday.split('-')
            birth = date(int(birth[0]), int(birth[1]), int(birth[2]))

        if individual.birthday == "NA":
            individual.age = 0

        elif individual.death == "NA":
            individual.age = today.year - birth.year - ((today.month, today.day) < (birth.month, birth.day))

        elif (individual.death != "NA" and individual.death != "INVALID DATE"):
            death = individual.death.split('-')
            death = date(int(death[0]), int(death[1]), int(death[2]))
            individual.age = death.year - birth.year - ((death.month, death.day) < (birth.month, birth.day))

        else:
            individual.age = 0

        if (individual.age >= 150):
            individual.age = "INVALID AGE"

    #Test code to make sure 15 child limit works
    #families[2].children = ["I20","I21","I22","I23","I24","I25","I26","I27",
    #                        "I28","I29","I30","I31","I32","I33","I34","I35"]


    for family in families:

        #US30
        list_marr0 = []
        if ((family.married != "INVALID DATE") & ((family.divorced == "NA") or (family.divorced == "INVALID DATE"))):
            list_marr0 += living_married(family, individuals)


        # US15 family has < 15 children
        if len(family.children) >= 15:
            print("Family {} has too many children. ({})".format(family.ID, len(family.children)))
        
        if not sibling_spacing(family, individuals):
            print("Family {} has improper sibling spacing.".format(family.ID))
        
    #Formatting between Validity Checks and Individual/Family List
    print()
    print("----------------------------------------------------------------------------------------------------------------------------")
    print()

    #US40: Include input line numbers
    line_count = 0

    for person in individuals:
        info = vars(person)
        print(line_count,', '.join("%s: %s" % value for value in info.items()))
        line_count += 1

    for family in families:
        info_f = vars(family)
        print(line_count,', '.join("%s: %s" % value for value in info_f.items()))
        line_count += 1

    conn = sqlite3.connect('GEDCOM.db')
    c = conn.cursor()
    c.execute("DROP TABLE IF EXISTS INDIVIDUALS")
    c.execute("DROP TABLE IF EXISTS FAMILIES")

    c.execute(''' CREATE TABLE INDIVIDUALS (
                    [ID] TEXT PRIMARY KEY,
                    [name] TEXT,
                    [gender] TEXT,
                    [birthday] TEXT,
                    [age] INTEGER,
                    [alive] BOOLEAN,
                    [death] TEXT,
                    [children] TEXT,
                    [spouse] TEXT
            )''')

    c.execute(''' CREATE TABLE FAMILIES (
                    [ID] TEXT PRIMARY KEY,
                    [married] TEXT,
                    [divorced] TEXT,
                    [husband_id] TEXT,
                    [husband_name] TEXT,
                    [wife_id] TEXT,
                    [wife_name] TEXT,
                    [children] TEXT
            )''')


    for person in individuals:

        info = list(vars(person).values())

        for index in range(len(info)):
            if type(info[index]) is list:
                info[index] = ", ".join(ids_to_names(info[index], individuals))

        sql = '''INSERT INTO INDIVIDUALS (ID, name, gender, birthday, age, alive, death, children, spouse)
                 VALUES(?,?,?,?,?,?,?,?,?)'''
        c.execute(sql, info)


    for family in families:

        info = list(vars(family).values())

        for index in range(len(info)):
            if type(info[index]) is list:
                info[index] = ", ".join(ids_to_names(info[index], individuals))

        sql = '''INSERT INTO FAMILIES (ID, married, divorced, husband_id, husband_name, wife_id, wife_name, children)
                 VALUES(?,?,?,?,?,?,?,?)'''

        c.execute(sql, info)

    #Formatting between Individual/Family List and Living Married List
    print()
    print("----------------------------------------------------------------------------------------------------------------------------")
    print()
    print("Living Married Individuals:")
    print(list_marr0)
    
    print()
    conn.commit()
    print("successful")
