import os
def changefilename():
    #file_list = []
    os.chdir('/Users/yarrowmadrona/Laboratory/MD/NAMD/dosE87A/analysis/fpocket/PDB')
    current_dir = os.getcwd()
    print current_dir
    for root, dirs, files in os.walk(current_dir):
        print files
        for filename in files:
            if filename.endswith('pdb'):
                os.rename(filename, 'wt'+filename[4:])
                
changefilename()
                