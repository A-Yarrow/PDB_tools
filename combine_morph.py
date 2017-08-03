#!/usr/bin/env python
#!/usr/local/bin/python

filename = sys.argv[1]
filename2 = sys.argv[2]
number

def combine_morph(filename1, filename2, number):

    counter = int(number)
    infile = open(filename1, 'r')
    infile2 = open(filename2, 'r')
    outfile = open('morph_combine.pdb' 'w')
    tempfiel = open('morph_temp'.pdb, 'w')
    for line in infile:
        outfile.write(line)
    
    for line in infile2:
        if not line.startswith('MODEL'):
            outfile.write(line)
        else:
            line = line.strip()
            line.replace
       

    
    
    
if __name__ == '__main__':   
    combine_morph(filename1, filename2, number )