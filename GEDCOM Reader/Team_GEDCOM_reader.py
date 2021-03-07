'''
@Author: Jonathan Cucci, Joe Letizia, Markell Torres, Erik Buczek
SSW555 Proj-2
GEDCOM Reader
'''
from Person import *
from Family import *
from datetime import *
import datetime

today = str(datetime.date.today())

# Opens GEDCOM file as fam variable
with open('Letizia_GEDTEST.ged.txt') as fam:
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
            birt_date = next_line[-1] + "-" + months[next_line[-2]] + "-" + next_line[-3]
            try:
                if(birt_date > today):
                    individuals[-1].birthday = birt_date + " - INVALID DATE - BIRTH DATE AFTER CURRENT DATE"
                else:
                    individuals[-1].birthday = birt_date
            except KeyError:
                individuals[-1].birthday = next_line[-1]

            #US02/US03: Birth before Marriage/Death
            birt_check = False
            try:
                birt_obj = datetime.datetime.strptime(individuals[-1].birthday, '%Y-%m-%d')
                birt_check = True
            except:
                pass

        elif("DEAT" in newLine):
            individuals[-1].alive = False
            next_line = line_point + 1
            next_line = text[next_line].split()
            deat_date = next_line[-1] + "-" + months[next_line[-2]] + "-" + next_line[-3]
            if("DATE" not in next_line):
                individuals[-1].death = "Not Found"
            else:
                try:
                    if(deat_date > today):
                        individuals[-1].death = deat_date + " - INVALID DATE - DEATH DATE AFTER CURRENT DATE"
                    else:
                        individuals[-1].death = deat_date
                except KeyError:
                    individuals[-1].death = next_line[-1]

            #US03: Birth before Death
            deat_check = False
            try:
                deat_obj = datetime.datetime.strptime(individuals[-1].death, '%Y-%m-%d')
                deat_check = True
            except:
                pass

            if (birt_check == True and deat_check == True and birt_obj.date() < deat_obj.date()):
                pass
            else:
                print("Individual ID: "+individuals[-1].ID+" | INVALID INDIVIDUAL: death before birth")

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
                div_date = next_line[-1] + "-" + months[next_line[-2]] + "-" + next_line[-3]
                for person in individuals:
                    if person.ID == families[-1].husband_id:
                        families[-1].husband_death_date = person.death
                    if person.ID == families[-1].wife_id:
                        families[-1].wife_death_date = person.death
                try:
                    if(div_date > today):
                        families[-1].divorced = div_date + " - INVALID DATE - DIVORCE DATE AFTER CURRENT DATE"
                    elif(div_date > families[-1].wife_death_date or div_date > families[-1].husband_death_date):
                        families[-1].divorced = div_date + " - INVALID DATE - DIVORCE OCCURED AFTER DEATH"

                    #US04: Marriage before divorce
                    elif(next_line[-3:] == marr_date[-3:] or next_line[-1] > marr_date[-1] or (next_line[-1] == marr_date[-1] and months[next_line[-2]] > months[marr_date[-2]]) or (months[next_line[-2]] == months[marr_date[-2]] and next_line[-3] > marr_date[-3])):
                        families[-1].divorced = next_line[-1] + "-" + months[next_line[-2]] + "-" + next_line[-3]
                    else:
                        families[-1].divorced = "INVALID DATE"
                except KeyError:
                    families[-1].divorced = next_line[-1]
            else:
                families[-1].divorced = "Date not found"

        elif("MARR" in newLine):
            #marr_exists = True
            if "DATE" in text[line_point+1].split():
                next_line = text[line_point+1].split()
                marr_date_string = next_line[-1] + "-" + months[next_line[-2]] + "-" + next_line[-3]
                marr_date_array = [next_line[-3], months[next_line[-2]], next_line[-1]]
                try:
                    if(marr_date_string > today):
                        families[-1].married = marr_date_string + " - INVALID DATE - MARRIAGE DATE AFTER CURRENT DATE"
                    else:
                        families[-1].married = marr_date_string
                except KeyError:
                    families[-1].married = next_line[-1]
                    
            #US05: Marriage before death
                if(individuals[-1].alive == False):
                    deat_date = individuals[-1].death.split("-")
                elif(individuals[-2].alive == False):
                    deat_date = individuals[-2].death.split("-")
                try:
                    if(individuals[-1].alive == False or individuals[-2].alive == False):
                        if(marr_date_array[2] > deat_date[0] or (marr_date[2] == deat_date[0] and marr_date[1] > deat_date[1]) or (marr_date[1] == deat_date[1] and marr_date[0] > deat_date[2])):
                            families[-1].married = "INVALID DATE"
                            families[-1].divorced = "INVALID DATE"
                        else:
                            families[-1].married = marr_date_array[2] + "-" + marr_date_array[1] + "-" + marr_date_array[0]
                    else:
                        families[-1].married = next_line[-1] + "-" + months[next_line[-2]] + "-" + next_line[-3]
                except KeyError:
                    families[-1].married = next_line[-1]
                
            #US02: Birth before Marriage
            marr_check = False
            try:
                marr_obj = datetime.datetime.strptime(families[-1].death, '%Y-%m-%d')
                marr_check = True
            except:
                pass
            '''
            #US02 INCOMPLETE
            NEED TO FIX THIS CODE, #US02 REQUIRES PULLING INDIVIDUAL IDs based on Family IDs
            if (birt_check == True and marr_check == True and birt_obj.date() < marr_obj.date()):
                print("Family ID: "+families[-1].ID+" | VERIFIED BIRTHS BEFORE MARRIAGE")
                pass
            else:
                print("Family ID: "+families[-1].ID+" | INVALID FAMILY: marriage before birth")
            '''

        line_point += 1


    # Updates everyones age
    for individual in individuals:

        today = date.today()
        birth = individual.birthday.split('-')
        birth = date(int(birth[0]), int(birth[1]), int(birth[2]))

        if individual.birthday == "NA":
            individual.age = 0

        elif individual.death == "NA":
            individual.age = today.year - birth.year - ((today.month, today.day) < (birth.month, birth.day))

        elif individual.death != "NA":
            death = individual.death.split('-')
            death = date(int(death[0]), int(death[1]), int(death[2]))
            individual.age = death.year - birth.year - ((death.month, death.day) < (birth.month, birth.day))

        else: 
            individual.age = 0

    #Formatting between Validity Checks and Individual/Family List
    print()
    print("----------------------------------------------------------------------------------------------------------------------------")
    print()

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
