from csv import *
def crystal():

    file = raw_input("Please enter the crystal screen name")
    handle = open(file, 'r')

    list = file.readlines() #make a list from the lines in the file.

    conditions = dict() #initialize the empty dictionary
    line = line.strip().split(" ")
    for line in list:
        key = line[0]
        value = line [1]
        conditions[key] = = counts.get(value, 0) 
        print conditions

    
   
