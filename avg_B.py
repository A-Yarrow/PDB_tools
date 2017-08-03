#!/usr/bin/python

def pdbstats():
    import math
    try:
        txt = raw_input("please enter filename: ")
        handle = open(txt, "r")
    
    except IOError:
        print "Cannot find the file '%s'" %(txt)
        
    else:
        print "Found file"
    
    LIG = raw_input("please enter ligand name: ")

    input = handle.readlines()

    B_sum = 0
    no_atoms = 0
    B_sum_het = 0
    no_atoms_het = 0

    for line in input:
    
        if line[0:4] == "ATOM":
            #print line
            B_sum = B_sum + float(line[60:64])
            no_atoms = no_atoms + 1
    
        elif line[0:6] == "HETATM" and line[17:20] != "HOH": 
            B_sum_het = B_sum_het +float(line[60:64])
            no_atoms_het = no_atoms_het + 1

    B_total = 0
    atoms_total = 0

    for line in input:
        if line[0:4] == "ATOM" or line[0:6] == "HETATM":
            B_total = B_total + float(line[60:64])
            atoms_total = atoms_total + 1

    B_LIG = 0
    atoms_LIG = 0

    for line in input:
        if line[17:20] == LIG:
            B_LIG = B_LIG + float(line[60:64])
            atoms_LIG = atoms_LIG + 1

    no_wat = 0        
    for line in input:
        if line[0:4] == "HETA" and line[17:20] == 'HOH':
            #print line
            no_wat = no_wat + 1


    Avg_B_protein = B_sum / no_atoms
    Avg_B_het = B_sum_het / no_atoms_het
    Avg_B_total = B_total / atoms_total
    Avg_B_LIG = B_LIG / atoms_LIG


    print "The number of protein atoms is %s" %no_atoms
    print "The number of waters is %i" %(no_wat)
    print "The number of heteroatoms is %s" %no_atoms_het
    print "The average B for protein atoms is %s" %Avg_B_protein
    print "The standard deviation is %s"
    print "The average B for heteroatoms is %s" %Avg_B_het
    print "The overall average B is %s" %Avg_B_total
    print "The overall average B for %s is %s" %(LIG, Avg_B_LIG)


pdbstats()

    
        
     
