from datetime import *
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