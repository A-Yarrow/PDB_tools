#!/usr/bin/env python
from sys import argv
H_strip, file_name = argv

def H_strip(file_name):
    
    infile = open(file_name, 'r')
    target = open(file_name[0:-4]+'_stripH.pdb', 'w')
    for line in infile:
        if "  H  "not in line:
            target.write(line)
    target.close()
    infile.close()
    
if __name__ == '__main__':
    H_strip(file_name)
        
    