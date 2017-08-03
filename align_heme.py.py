#pymol -qrc script.py arg1 arg2

"""Usage: run from command line by typing, pymol align-heme.py PDB1 PDB2 Chain X Chain Y
#Where PDB1 and PDB2 are the PDB's you want to align and chain X and chain Y are 
#their respective chains. pymol align-heme.py funky.pdb smelly.pdb chain A chain B
#would align chain A of funnk.pdb with chain B of smelly.pdb
"""

from sys import argv
from pymol import cmd, stored 
PDB1, PDB2, chain1, chain2 = argv

print "O.k, we will align the hemes of %s and %s" %(PDB1, PDB2)

color_PDB1 = raw_input("what color would you like for PDB1?" )
color_PDB2 = raw_input("what color would you like for PDB2?" )

print "O.k here goes something....."

def align_heme(PDB1, PDB2):
 	print "Making pretty picture of %s aligned with %s" %(PDB1, PDB2)
 	return PDB1, PDB2
 	cmd.load(PDB1)
	cmd.load(PDB2)
	cmd.hide(lines, "all")
	cmd.color(color_PDB1, PDB1)
	cmd.color(color_PDB2, PDB2)
	cmd.show(cartoon, PDB1)
	cmd.show(cartoon, PDB2)
	cmd.set_bond(stick_radius, 0.3, "all")
	cmd.align(("PDB1 and resname HEME"),("PDB2 and resname HEME")) 
	cmd.bg_color(color = white)
	
cmd.extend("align_heme", align_heme)	
	
	
    '''
DESCRIPTION
 
    Brief description what this function does goes here
    '''
    #
    # Your code goes here
    #
    print "Hello, PyMOLers"
    print "You passed in %s and %s" % (arg1, arg2)
    print "I will return them to you in a list.  Here you go."
    return (arg1, arg2)
 """
cmd.extend("align_heme",align_heme)

