#!/usr/bin/env python
#!/usr/local/bin/python

import sys
import os

filename = sys.argv[1]
chain = sys.argv[2]

def get_chain(filename, chain):
   
    read_file = open(filename, 'r')
    out_file = open(filename[0:-4]+"_"+chain+".pdb", 'w')
   
    test = 0
    for line in read_file:
        if line[0:4] == "ATOM" and line[21] == chain:
            line = line.strip()
            print line
            out_file.write(line+'\n')
            test = 1
    
    out_file.write("END")
    
    read_file.close()
    out_file.close()
    
    if test != 1:
        os.remove(filename[0:-4]+"_"+chain+".pdb")
        print "Sorry, chain", chain, "does not exist"
    
if __name__ == '__main__':   
    get_chain(filename, chain )