import os
#import pylab
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns


#wt-171-87-water list
def count_water_171_87():
    os.chdir('/Users/yarrowmadrona/Laboratory/MD/NAMD/DosS-GAFA/analysis/water_bridge')
    filehandle = open('wt_water.txt', 'wb')
    wt_water_list_171_87 = []
    wt_frame_list = []
    current_dir = os.getcwd()
    for root, dirs, files in os.walk(current_dir):
        for filename in files:
            statinfo = os.stat(filename)
            if statinfo.st_size > 0:
                if filename.startswith('water_0'):
                    wt_water_list_171_87.append(filename)
                    wt_frame_list.append(int(filename[11:15]))
                    filehandle.write(filename+'\n')


#set value for 171-87 water bridge H-bond to 1
    
    value_171_87_list = []
    for water in wt_water_list_171_87:
        value_171_87_list.append(int(1))
        
    wt_No_waters = len(wt_water_list_171_87)
    wt_percent_occ = float(wt_No_waters) / 4301*100
    #print "frames:", wt_frame_list#, "waters"+wt_water_list_171_87 
    print "Y171-E87 share a water bridge %s percent of the time" %(wt_percent_occ)
    filehandle.close()
    return value_171_87_list, wt_frame_list
count_water_171_87()

def count_water_87_89():
    filehandle = open('wt_E87-H89-water.txt', 'wb')
    wt_water_list_87_89 = []
    wt_87_89_frame_list = []
    current_dir = os.getcwd()
    for root, dirs, files in os.walk(current_dir):
        for filename in files:
            statinfo = os.stat(filename)
            if statinfo.st_size > 0:
                if filename.startswith('water_87_89'):
                    wt_water_list_87_89.append(filename)
                    wt_87_89_frame_list.append(int(filename[17:21]))
                    filehandle.write(filename+'\n')
#set value for 87-89 water bridge H-bond to 1
    value_87_89_list = []
    for water in wt_water_list_87_89:
        value_87_89_list.append(int(2))
    wt_87_89_No_waters = len(wt_water_list_87_89)
    #print 'wt_87_89_No_waters', wt_87_89_No_waters
    wt_87_89_percent_occ = float(wt_87_89_No_waters) / 4301*100
    print "E87-H89 share a water bridge %s percent of the time" %(wt_87_89_percent_occ)
    filehandle.close() 
    return value_87_89_list, wt_87_89_frame_list
count_water_87_89()

def count_water_overlap():
    filehandle = open('wt_water_overlap.txt', 'wb')
    wt_87_89_frame_list = count_water_87_89()[1]  
    wt_frame_list = count_water_171_87()[1]
    water_overlap = []
    value_water_overlap = []
    for water in wt_87_89_frame_list:
        if water in wt_frame_list:
            water_overlap.append(water)
            filehandle.write(str(water)+'\n')
            value_water_overlap.append(int(3))
    overlap_water_occ = float(len(water_overlap)) / 4301 * 100
    filehandle.close()
    print "Both E87-Y171 and E87-H89 bridge waters at the same time %s percent of the time" %(overlap_water_occ)
    return value_water_overlap, water_overlap
count_water_overlap()
'''
The 171 OH to OE is bieng considered as an H Bond, while with distance max of 3.5
Make a dictionary with keys set to the frame number and values set to the distance but
only if the distance is less than 3.5.
Then make sorted lists of tuples from the dictionary.
'''

def count_hbond_171_87():
    os.chdir('/Users/yarrowmadrona/Laboratory/MD/NAMD/DosS-GAFA/analysis/distances2')
    current_dir = os.getcwd()
    filehandle1 = open('TyrOH-GluOE1.dat', 'r')
    filehandle2 = open('TyrOH-GluOE2.dat','r')
    out_file = open('TyrOH-GluOE1-OE2_dis.txt', 'wb')
    hbond_171_87_OE1_OE2_dict = {}
    
    for line in filehandle1:
        line = line.strip().split(' ')
        if float(line[1]) <= 3.5:
            frame= int(line[0])
            dis = float(line[1])
            hbond_171_87_OE1_OE2_dict[frame] = dis
        else:
            pass
    filehandle1.close()
    
    for line in filehandle2:
        line = line.strip().split(' ')
        if float(line[1]) <= 3.5:
            frame = int(line[0])
            dis = float(line[1])
            if hbond_171_87_OE1_OE2_dict.has_key(frame):
                pass
            else:
                hbond_171_87_OE1_OE2_dict[frame] = dis
    filehandle2.close()
    
    hbond_171_87_OE1_OE2_list = []
    for frame, dis in hbond_171_87_OE1_OE2_dict.items():
        hbond_171_87_OE1_OE2_list.append((frame, round(dis,2)))
        hbond_171_87_OE1_OE2_list.sort()
    list_as_strings = [str(element).strip('(').strip(')')+'\n' for element in hbond_171_87_OE1_OE2_list]
    out_file.writelines(list_as_strings)
    out_file.close()
    return hbond_171_87_OE1_OE2_list

#count_hbond_171_87()
#Count the number of salt bridges less than 4 angstroms between either OE1 of E87 or OE2 of E87 to H89
#There are four ways a salt bridge can form between His89 and Glu87:
#HisNE2-GluOE1, HisNE2-GluOE2, HisND1-GluOE1, HisND1-GluOE2  
def count_hbond_87_89():
    os.chdir('/Users/yarrowmadrona/Laboratory/MD/NAMD/DosS-GAFA/analysis/distances2')
    filehandle1 = open('HisNE2-GluOE1.dat', 'r')
    filehandle2 = open('HisNE2-GluOE2.dat', 'r')
    filehandle3 = open('HisND1-GluOE1.dat', 'r')
    filehandle4 = open('HisND1-GluOE2.dat', 'r')
    out_file = open('HisNE2-GluOE1-OE2_dis.txt', 'wb')
    hbond_89_87_OE1_OE2_dict = {}
    
    for line in filehandle1:
        line = line.strip().split(' ')
        if float(line[1]) <= 4.0:
            frame= int(line[0])
            dis = float(line[1])
            hbond_89_87_OE1_OE2_dict[frame] = dis
        else:
            pass
    filehandle1.close()
    
    for line in filehandle2:
        line = line.strip().split(' ')
        if float(line[1]) <= 4.0:
            frame = int(line[0])
            dis = float(line[1])
            if hbond_89_87_OE1_OE2_dict.has_key(frame):
                pass
            else:
                hbond_89_87_OE1_OE2_dict[frame] = dis
    filehandle2.close()
    
    for line in filehandle3:
        line = line.strip().split(' ')
        if float(line[1]) <= 4.0:
            frame = int(line[0])
            dis = float(line[1])
            if hbond_89_87_OE1_OE2_dict.has_key(frame):
                pass
            else:
                hbond_89_87_OE1_OE2_dict[frame] = dis
    filehandle2.close()
    
    for line in filehandle4:
        line = line.strip().split(' ')
        if float(line[1]) <= 4.0:
            frame = int(line[0])
            dis = float(line[1])
            if hbond_89_87_OE1_OE2_dict.has_key(frame):
                pass
            else:
                hbond_89_87_OE1_OE2_dict[frame] = dis
    filehandle2.close()
    
    hbond_89_87_OE1_OE2_list = []
    for frame, dis in hbond_89_87_OE1_OE2_dict.items():
        hbond_89_87_OE1_OE2_list.append((frame, round(dis,2)))
        hbond_89_87_OE1_OE2_list.sort()
    list_as_strings = [str(element).strip('(').strip(')')+'\n' for element in hbond_89_87_OE1_OE2_list]
    out_file.writelines(list_as_strings)
    out_file.close()
    return hbond_89_87_OE1_OE2_list

def count_overlap_171_87_89():
    outfile = open("overlap_171_87_89_nowat.txt", "wb")
    
    
    x = count_hbond_87_89()
    y = count_hbond_171_87()
    frame_87_89 = set()
    frame_171_87 = set()
    for element in x:
        frame_87_89.add(element[0])
    for element in y:
        frame_171_87.add(element[0])
    
    overlap = set.intersection(frame_87_89, frame_171_87)   
    overlap_frame_list = list(overlap)
    overlap_list = []
    
    for element in x:
        if element[0] in overlap_frame_list:
            overlap_list.append(element)
            outfile.write(str(element).strip(')').strip('(')+'\n')
        else: pass
            
    for element in y:
        if element[0] in overlap_frame_list and not overlap_list:
            overlap_list.append(element)
            outfile.write(str(element).strip(')').strip('(')+'\n')
        else: pass
            
    overlap_list.sort()
    percent_overlap = float(len(overlap_list)) / 4301 * 100
    print "Y171, E84, and H87 for an Hbond/ionic bridge (without waters) %s percent of the time."%(round(percent_overlap, 2)) 
    outfile.write("Y171, E84, and H87 for an Hbond/ionic bridge (without waters) %s percent of the time."%(round(percent_overlap, 2)))
    
    overlap_list_dis = [x[1] for x in overlap_list]
    overlap_list_value = [int(4) for x in overlap_list_dis]
    overlap_list_frame = [x[0] for x in overlap_list]
    return overlap_list, overlap_list_value, overlap_list_frame
count_overlap_171_87_89()

def plot_water_bridge():
    y1, x1 = count_water_171_87()
    y2, x2 = count_water_87_89()
    y3, x3 = count_water_overlap()
    y4, x4 = count_overlap_171_87_89()[1:3]
    plt.figure("WT water bridge", figsize = (8, 3))
    # add 1 to frames since frames are labeled starting at 0
    plt.scatter([t+1 for t in x1], y1, color = 'blue', s=450, lw = '0.03', facecolor='None') 
    plt.scatter([t+1 for t in x2], y2, color = 'green', s=450, lw = '0.03', facecolor='None')
    plt.scatter([t+1 for t in x3], y3, color = 'orange', s=450, lw = '0.03', facecolor="None")
    plt.scatter([t+1 for t in x4], y4, color = 'black', s=450, lw = '0.03', facecolor="None")
    plt.axis([-150, 4500, 0.5, 4.5])
    #plt.xlabel("Nanoseconds")
    plt.grid(False)
    
    plt.savefig('wt_water_salt_plot')
    plt.show()
    
plot_water_bridge()
        