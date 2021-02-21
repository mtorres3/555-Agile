'''
@Author: Jon Cucci
SSW555 Proj-2
GEDCOM Reader
'''

# Opens GEDCOM file as fam variable
with open('JonathanCucci.ged.txt') as fam:

    # Tags broken down into indexes that correspond with their acceptable level number
    tags = [["INDI", "FAM", "HEAD", "TRLR", "NOTE"],["NAME", "SEX", "BIRT", "DEAT", "FAMC", "FAMS", "MARR", "HUSB", "WIFE", "CHIL", "DIV"],["DATE"]]
    
    # Goes through each line of the GEDCOM file
    for line in fam:

        # Splits line into list.. easier to work with.
        newLine = line.split()

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
