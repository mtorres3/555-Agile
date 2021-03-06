
from datetime import *
from extra_functions import *
import datetime
from extra_functions import * 
today = str(datetime.date.today())

def create_BIRT(birt_date, individual):
    if(birt_date > today):
        print("ID: "+individual.ID+" | INVALID INDIVIDUAL: birth after today")
        return "INVALID DATE"
    else:
        return birt_date

def create_DEAT(deat_date, next_line):
        if("DATE" not in next_line):
            return "Not Found"
        elif(deat_date > today):
            print("ID: "+individual.ID+" | INVALID INDIVIDUAL: death after today")
            return "INVALID DATE"
        else:
            return deat_date

# US08, US09
def create_CHIL(families, individuals, line):
    
    child = line[-1][1:-1]
    
    # Get husband death date, wife death date, and child birthday
    for person in individuals: 
            
        # 4 Checks for invalid child birth date
        
        # Check for child birthday before parents marriage
        if person.ID == child:
            childbirthday = person.birthday
            if (childbirthday < families[-1].married) and (families[-1].married != "INVALID DATE"):
                print("ID: "+child+" | Invalid child birth date, before marriage")
        # Check for child birthday before parents marriage
        if families[-1].divorced != "NA":
            div = datetime.datetime.strptime(families[-1].divorced, '%Y-%m-%d')
            divplusnine = div + timedelta(weeks=39)
            if childbirthday != "INVALID DATE":
                childbirthdate = datetime.datetime.strptime(childbirthday, '%Y-%m-%d')
                if (childbirthdate > divplusnine):
                    print("ID: "+child+" | Invalid child birth date, after divorce plus 9 months")
        # Check for child birthday before parents marriage
        if person.ID == families[-1].wife_id:
            temp_wife_death = person.death
            if person.ID == child:
                childbirthday = person.birthday
                if (childbirthday > temp_wife_death):
                    print("ID: "+child+" | Invalid child birth date, after mother's death")
        # Check for child birthday before parents marriage
        if person.ID == families[-1].husband_id:
            temp_husband_death = person.death
            if temp_husband_death != "NA":
                husbdeath = datetime.datetime.strptime(temp_husband_death, '%Y-%m-%d')
                husbdeathplusnine = husbdeath + timedelta(weeks=39)
                if childbirthday != "INVALID DATE":
                        childbirthdate = datetime.datetime.strptime(childbirthday, '%Y-%m-%d')
                        if (childbirthdate > husbdeathplusnine):
                            print("ID: "+child+" | Invalid child birth date, after father's death plus 9 months")
        # Append child to family, husband, and wife lists
        families[-1].children.append(child)
        for person in individuals:
            if person.ID == families[-1].husband_id:
                person.child.append(child)
            if person.ID == families[-1].wife_id:
                person.child.append(child)
        return [individuals, families]

# US02
def validate_DEAT(individual):

    birt_check = False
    deat_check = False

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
        print("ID: "+individual.ID+" | INVALID INDIVIDUAL: death before birth")
        individual.death = "INVALID DATE"
    return individual

def husband(families, individuals, newLine, next_line):
    families[-1].husband_id = newLine[-1][1:-1]
    families[-1].wife_id = next_line[-1][1:-1]
    for person in individuals:
        if person.ID == families[-1].husband_id:
            families[-1].husband_name = person.name
            #US21: Correct gender for role
            if(person.gender == "F"):
                print("ID: "+person.ID+" | INVALID INDIVIDUAL: gender wrong for role")
                person.gender = "INVALID GENDER"
            person.spouse.append(families[-1].wife_id)
            check_bigamy(individuals, families[-1].husband_id)
    return [individuals, families]

def wife(families, individuals, newLine):
    families[-1].wife_id = newLine[-1][1:-1]
    for person in individuals:
        if person.ID == families[-1].wife_id:
            families[-1].wife_name = person.name
            #US21: Correct gender for role
            if(person.gender == "M"):
                print("ID: "+person.ID+" | INVALID INDIVIDUAL: gender wrong for role")
                person.gender = "INVALID GENDER"
            person.spouse.append(families[-1].husband_id)
            check_bigamy(individuals, families[-1].wife_id)
    return [individuals, families]

def check_bigamy(individuals, ID):
    for person in individuals:
        if ID == person.ID:
            if (len(person.spouse) > 1):
                print("ID: "+ person.ID + " | INVALID MARRIAGE: Bigamy")

# if 'DIV'
def check_DIV(family, individuals, next_line, marr_date, div_date):

    for person in individuals:
        if person.ID == family.husband_id:
            temp_husband_death = person.death
        if person.ID == family.wife_id:
            temp_wife_death = person.death
    try:
        if(div_date > today):
            print("ID: "+family.ID+" | INVALID FAMILY: divorce after today")
            family.divorced = "INVALID DATE"
        elif(div_date > temp_wife_death or div_date > temp_husband_death):
            print("ID: "+family.ID+" | INVALID FAMILY: divorce after death of spouse")
            family.divorced = "INVALID DATE"

        #US04: Marriage before divorce
        elif(next_line[-3:] == marr_date[-3:] or next_line[-1] > marr_date[-1] or (next_line[-1] == marr_date[-1] and MONTHS[next_line[-2]][0] > MONTHS[marr_date[-2]][0]) or (MONTHS[next_line[-2]][0] == MONTHS[marr_date[-2]][0] and next_line[-3] > marr_date[-3])):
            family.divorced = next_line[-1] + "-" + MONTHS[next_line[-2]][0] + "-" + next_line[-3]
        else:
            print("ID: "+family.ID+" | INVALID FAMILY: divorce before marriage")
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
            elif(marr_date_array[2] > deat_date[0] or (marr_date[2] == deat_date[0] and marr_date[1] > deat_date[1]) or (marr_date[1] == deat_date[1] and marr_date[0] > deat_date[2])):
                print("ID: "+family.ID+" | INVALID FAMILY: marriage after death of spouse")
                family.married = "INVALID DATE"
                family.divorced = "INVALID DATE"
            else:
                family.married = marr_date_array[2] + "-" + marr_date_array[1] + "-" + marr_date_array[0]
        elif(family.married == "INVALID DATE"):
            pass
        else:
            family.married = next_line[-1] + "-" + MONTHS[next_line[-2]][0] + "-" + next_line[-3]
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
            print("ID: "+family.ID+" | INVALID FAMILY: marriage after today")
            family.married = "INVALID DATE"
        elif(husband_age < 14 or wife_age < 14):
            print("ID: "+family.ID+" | INVALID FAMILY: spouse too young at marriage")
            family.married = "INVALID DATE"
        elif(temp_husband_birth > marr_date_string or temp_wife_birth > marr_date_string):
            print("ID: "+family.ID+" | INVALID FAMILY: marriage before birth of spouse")
            family.married = "INVALID DATE"
        else:
            family.married = marr_date_string
    except KeyError:
        family.married = next_line[-1]

#US12
def old_parents(family, individuals):
    dad = id_to_person(family.husband_id, individuals)
    mom = id_to_person(family.wife_id, individuals)
    count = 0
    for child in family.children:
        kid = id_to_person(family.children[count], individuals)
        if ((mom.age - kid.age) >= 60) or ((dad.age - kid.age) >= 80):
            print ("ID: "+kid.ID+" | INVALID INDIVIDUAL: born after mother >= 60 or father >= 80")
            kid.age = "INVALID AGE"
        count += 1

#US13
def sibling_spacing(family, individuals):
    if len(family.children) in [0,1]:
        return True
    for s1 in family.children:
        for s2 in family.children:
            try:
                s1_ = id_to_person(s1, individuals)
                s1_BIRT = date_string_to_list(s1_.birthday)
                s1_BIRT = datetime.datetime(s1_BIRT[0], s1_BIRT[1], s1_BIRT[2])
                s2_ = id_to_person(s2, individuals)

                if s1_.ID == s2_.ID:
                    continue

                else:
                    s2_BIRT = date_string_to_list(s2_.birthday)
                    s2_BIRT = datetime.datetime(s2_BIRT[0], s2_BIRT[1], s2_BIRT[2])
                    diff_days = abs((s1_BIRT - s2_BIRT).days)
                    if diff_days > 2 and diff_days < 240:
                        return False
            except ValueError:
                continue
    return True

#US29
def printDead(individuals):
    Deceased = []
    for item in individuals:
        if item.alive == False:
            Deceased.append(item.name + " (" + item.ID + ")")
    return Deceased

#US30
list_marr0 = []
def living_married(family, individuals):
    husb = id_to_person(family.husband_id, individuals)   
    wife = id_to_person(family.wife_id, individuals)

    if ((family.married != "INVALID DATE") & ((family.divorced == "NA") or (family.divorced == "INVALID DATE"))):
        if husb.death == "NA":
            list_marr0.append(husb.name + " (" + husb.ID + ")")
        if wife.death == "NA":
            list_marr0.append(wife.name + " (" + wife.ID + ")")
        
    return list_marr0          

#US32
name_array_list = []
def multiple_births(family, individuals):
    same_bday = []
    if len(family.children) > 0:
        x = family.children[0]
        #print(ids_to_names(x, individuals))
    
    for y in range(1,len(family.children)):
        if id_to_person(x, individuals).birthday == id_to_person(family.children[y], individuals).birthday and id_to_person(x, individuals).name != id_to_person(y, individuals).name:
            if id_to_person(x, individuals).name not in same_bday:
                same_bday += id_to_person(x, individuals).name + " (" + id_to_person(x, individuals).ID + ")"
                same_bday += '|'
            same_bday += id_to_person(family.children[y], individuals).name + " (" +\
                         id_to_person(family.children[y], individuals).ID + ")"
            same_bday += '|'
    
    names_list = ''.join(same_bday)
    names_list = names_list[:len(same_bday)//2]
    if len(names_list) > 0:
        name_array = names_list.split('|')
        name_array_list.append(name_array)
    multi = name_array_list
    return multi


def multiple_births_v2(family, individuals):
    bday_pair_list = [] #Multiple pairs of same bdays in family
    same_bday = [] #Same exact bday

    child_list = family.children
    
    for x in child_list:
        first_bday = id_to_person(x, individuals).birthday
        first_name = id_to_person(x, individuals).name
        for y in child_list:
            second_bday = id_to_person(y, individuals).birthday
            second_name = id_to_person(y, individuals).name
            
            if first_bday == second_bday and first_name != second_name:
                same_bday.append(first_name)
                same_bday.append(second_name)

        same_bday_single = list(dict.fromkeys(same_bday))
        
    if len(same_bday) > 1:
        bday_pair_list.append(same_bday_single)
    output = bday_pair_list
    #US14
    if len(same_bday) > 5:
        print("INVALID MULTIPLE BIRTHS")
        return []
    elif output != []:
        print("Multiple births in ", family.ID, ": ", output)
        return output
    
    
#US34
marr_2age0 = []
def marriage_double_age(family, individuals):
    husb = id_to_person(family.husband_id, individuals)   
    wife = id_to_person(family.wife_id, individuals)

    if ((family.married != "INVALID DATE") & (husb.birthday != "INVALID DATE") & (wife.birthday != "INVALID DATE")):
        
        family_int = datetime.datetime.strptime(family.married, '%Y-%m-%d')
        husb_int = datetime.datetime.strptime(husb.birthday, '%Y-%m-%d')
        wife_int = datetime.datetime.strptime(wife.birthday, '%Y-%m-%d')
        husb_ref = family_int - husb_int
        wife_ref = family_int - wife_int

        if (husb_ref > (2*wife_ref)) or (wife_ref > (2*husb_ref)):
            marr_2age0.append(husb.name + " (" + husb.ID + ") - " + wife.name + " (" + wife.ID + ")")

    return marr_2age0

#US18
def siblings_married(family, individuals):
    child_list = []
    for c in family.children:
        child_list.append(id_to_person(c, individuals))
    if len(child_list) <= 1:
        return
    else:
        for sibling in child_list:
            spouses = []
            for s in sibling.spouse:
                spouses.append(id_to_person(s, individuals))
            if any(e in child_list for e in spouses):
                sibling.spouse = "INVALID SPOUSE"
                print ("ID: "+sibling.ID+" | INVALID INDIVIDUAL: married to sibling")
                print ("ID: "+family.ID+" | INVALID FAMILY: parents are siblings")
            else:
                continue
