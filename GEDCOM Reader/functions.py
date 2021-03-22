from datetime import *
from extra_functions import *
import datetime
today = str(datetime.date.today())

def create_BIRT(birt_date):
    if(birt_date > today):
        return "INVALID DATE"
    else:
       return birt_date

def create_DEAT(deat_date, next_line):
        if("DATE" not in next_line):
            return "Not Found"
        elif(deat_date > today):
            return "INVALID DATE"
        else:
           return deat_date

def create_CHIL(families, individuals, line):
    families[-1].children.append(line[-1][1:-1])
    for person in individuals:
        if person.ID == families[-1].husband_id:
            person.child.append(line[-1][1:-1])
        if person.ID == families[-1].wife_id:
            person.child.append(line[-1][1:-1])
    return [individuals, families]

# US02
def validate_DEAT(individual):

    #birt_check = False
    #deat_check = False

    try:
        birt_obj = datetime.datetime.strptime(individual.birthday, '%Y-%m-%d')
        birt_check = True
    except:
        birt_check = False

    try:
        deat_obj = datetime.datetime.strptime(individual.death, '%Y-%m-%d')
        deat_check = True
    except:
        deat_check = False

    if (birt_check == True and deat_check == True and birt_obj.date() < deat_obj.date()):
        pass
    else:
        individual.death = "INVALID DATE"
        print("Individual ID: "+individual.ID+" | INVALID INDIVIDUAL: death before birth")
    return individual

# if 'DIV'
def check_DIV(family, individuals, next_line, marr_date, div_date):
    
    for person in individuals:
        if person.ID == family.husband_id:
            temp_husband_death = person.death
        if person.ID == family.wife_id:
            temp_wife_death = person.death
    try:
        if(div_date > today):
            family.divorced = "INVALID DATE"
        elif(div_date > temp_wife_death or div_date > temp_husband_death):
            family.divorced = "INVALID DATE"

        #US04: Marriage before divorce
        elif(next_line[-3:] == marr_date[-3:] or next_line[-1] > marr_date[-1] or (next_line[-1] == marr_date[-1] and months[next_line[-2]][0] > months[marr_date[-2]][0]) or (months[next_line[-2]][0] == months[marr_date[-2]][0] and next_line[-3] > marr_date[-3])):
            family.divorced = next_line[-1] + "-" + months[next_line[-2]][0] + "-" + next_line[-3]
        else:
            family.divorced = "INVALID DATE"
    except KeyError:
        family.divorced = next_line[-1]
    
#MARR before DIV
def check_MARR_before_DEAT(family, individuals, next_line, marr_date_string, marr_date_array):
    if(individuals[-1].alive == False):
        deat_date = individuals[-1].death.split("-")
    elif(individuals[-2].alive == False):
        deat_date = individuals[-2].death.split("-")
    try:
        if(individuals[-1].alive == False or individuals[-2].alive == False):
            if(family.married == "INVALID DATE"):
                pass
            elif(family.married == "INVALID MARRIAGE AGE"):
                pass
            elif(marr_date_array[2] > deat_date[0] or (marr_date[2] == deat_date[0] and marr_date[1] > deat_date[1]) or (marr_date[1] == deat_date[1] and marr_date[0] > deat_date[2])):
                family.married = "INVALID DATE"
                family.divorced = "INVALID DATE"
            else:
                family.married = marr_date_array[2] + "-" + marr_date_array[1] + "-" + marr_date_array[0]
        elif(family.married == "INVALID DATE"):
            pass
        elif(family.married == "INVALID MARRIAGE AGE"):
            pass
        else:
            family.married = next_line[-1] + "-" + months[next_line[-2]][0] + "-" + next_line[-3]
    except KeyError:
        family.married = next_line[-1]

#MARR after BIRT
def check_MARR_after_BIRT(family, individuals, next_line, marr_date_string, marr_date_array):
    for person in individuals:
        if person.ID == family.husband_id:
            temp_husband_birth = person.birthday
            temp_husband_birth_date = datetime.datetime.strptime(person.birthday, '%Y-%m-%d')
            marriage_date = datetime.datetime.strptime(marr_date_string, '%Y-%m-%d')
            husband_age = marriage_date.year - temp_husband_birth_date.year - ((marriage_date.month, marriage_date.day) < (temp_husband_birth_date.month, temp_husband_birth_date.day))

        if person.ID == family.wife_id:
            temp_wife_birth = person.birthday
            temp_wife_birth_date = datetime.datetime.strptime(person.birthday, '%Y-%m-%d')
            marriage_date = datetime.datetime.strptime(marr_date_string, '%Y-%m-%d')
            wife_age = marriage_date.year - temp_wife_birth_date.year - ((marriage_date.month, marriage_date.day) < (temp_wife_birth_date.month, temp_wife_birth_date.day))
    try:
        if(marr_date_string > today):
            family.married = "INVALID DATE"
        elif(husband_age < 14 or wife_age < 14):
            family.married = "INVALID MARRIAGE AGE"
        elif(temp_husband_birth > marr_date_string or temp_wife_birth > marr_date_string):
            family.married = "INVALID DATE"
            print("Family ID: "+family.ID+" | INVALID INDIVIDUAL: marriage before birth")
        else:
            family.married = marr_date_string
    except KeyError:
        family.married = next_line[-1]   
