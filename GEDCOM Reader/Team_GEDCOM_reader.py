'''
@Author: Jon Cucci
SSW555 Proj-2
GEDCOM Reader
'''

from Person import *
from Family import *
from datetime import *

# Opens GEDCOM file as fam variable
with open('test_JonCucci.ged.txt') as fam:
    text = fam.readlines()
    # Tags broken down into indexes that correspond with their acceptable level number
    tags = [["INDI", "FAM", "HEAD", "TRLR", "NOTE"],["NAME", "SEX", "BIRT", "DEAT", "FAMC", "FAMS", "MARR", "HUSB", "WIFE", "CHIL", "DIV"],["DATE"]]
    months = {
        'JAN' : "01",
        'FEB' : "02",
        'MAR' : "03",
        'APR' : "04",
        'MAY' : "05",
        'JUN' : "06",
        'JUL' : "07",
        'AUG' : "08",
        'SEP' : "09",
        'OCT' : "10",
        'NOV' : "11",
        'DEC' : "12"}
    individuals = []
    families = []
    line_point = 0

    # Goes through each line of the GEDCOM file
    for line in text:
        newLine = line.split()
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
            try:
                individuals[-1].birthday = next_line[-1] + "-" + months[next_line[-2]] + "-" + next_line[-3]
            except KeyError:
                individuals[-1].birthday = next_line[-1]
        elif("DEAT" in newLine):
            individuals[-1].alive = False
            next_line = line_point + 1
            next_line = text[next_line].split()
            if("DATE" not in next_line):
                individuals[-1].death = "Not Found"
            else:
                try:
                    individuals[-1].death = next_line[-1] + "-" + months[next_line[-2]] + "-" + next_line[-3]
                except KeyError:
                    individuals[-1].death = next_line[-1]
        elif("FAM" in newLine):
            families.append(Family())
            families[-1].ID = newLine[1][1:-1]
        elif("HUSB" in newLine):
            families[-1].husband_id = newLine[-1][1:-1]
            for person in individuals:
                if person.ID == families[-1].husband_id:
                    families[-1].husband_name = person.name
        elif("WIFE" in newLine):
            families[-1].wife_id = newLine[-1][1:-1]
            for person in individuals:
                if person.ID == families[-1].wife_id:
                    families[-1].wife_name = person.name

        elif("CHIL" in newLine):
            families[-1].children.append(newLine[-1][1:-1])

        elif("DIV" in newLine):
            if "DATE" in text[line_point+1].split():
                next_line = text[line_point+1].split()
                marr_date = text[line_point-1].split()
                try:
                    if(next_line[-3:] == marr_date[-3:] or next_line[-1] > marr_date[-1] or (next_line[-1] == marr_date[-1] and months[next_line[-2]] > months[marr_date[-2]]) or (months[next_line[-2]] == months[marr_date[-2]] and next_line[-3] > marr_date[-3])):
                        families[-1].divorced = next_line[-1] + "-" + months[next_line[-2]] + "-" + next_line[-3]
                    else:
                        families[-1].divorced = "INVALID DATE"
                except KeyError:
                    families[-1].divorced = next_line[-1]
            else:
                families[-1].divorced = "Date not found"
        elif("MARR" in newLine):
            if "DATE" in text[line_point+1].split():
                next_line = text[line_point+1].split()
                try:
                    families[-1].married = next_line[-1] + "-" + months[next_line[-2]] + "-" + next_line[-3]
                except KeyError:
                    families[-1].married = next_line[-1]

        line_point += 1

    for person in individuals:
        info = vars(person)
        print(', '.join("%s: %s" % value for value in info.items()))

    for family in families:
        info_f = vars(family)
        print(', '.join("%s: %s" % value for value in info_f.items()))

'''

        # if there is a tag in the first index value that can be found
        # in the TAG list corresponding its level val and manipulate
        #  the string to add Y

        if(newLine[1] in tags[int(newLine[0])]):
            newLine[1] = "|" + newLine[1] + "|" + "Y|"

        # Else if the list after slicing is larger than 2 pieces, and the
        # index 2 element is in the TAGS list with a corresponding level value,
        # change the 1st index to the tag and put the id after

        elif(len(newLine) > 2 and newLine[2] in tags[int(newLine[0])]):
            temp = newLine[2]
            newLine[2] = newLine[1]
            newLine[1] = "|" + temp + "|" + "Y|"

        # Else, manipulate index 1 to add N. It is not a compatable TAG.
        else:
             newLine[1] = "|" + newLine[1] + "|" + "N|"

        # Input / Output formatting
        line = "--> " + line
        printLine = "<--"

        # Concatenation
        for bit in newLine:
            printLine = printLine + " " + bit

        # Annnnnnnnd Print
        print(line[:-1])
        print(printLine + "\n")
'''
