#!/usr/bin/env python
#!/usr/local/bin/python
import sys

file_name = sys.argv[1]
def chainstrip(file_name):
    
    outfile = open("CYP125A1-fpocket.pdb", "w")
    f = open(file_name, "r")
    input = f.readlines()
    for line in input:
        if line[0:4] == "ATOM":
            print line
            outfile.write(line)
            
        elif line[17:20] == "HEM" and line[0:6] == "HETATM":
            outfile.write(line)
            print line
    outfile.write("END")
    f.close()

if __name__ == '__main__':
    chainstrip(file_name)