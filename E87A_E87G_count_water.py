import os
import matplotlib.pyplot as plt
import seaborn as sns

def count_E87A_single_water():
    os.chdir("/Users/yarrowmadrona/Laboratory/MD/NAMD/dosE87A/analysis/water_bridge/pdb")
    filehandle = open('E87A_single_water.txt', 'wb')
    E87A_water_list_single = []
    E87A_single_frame_list = []
    current_dir = os.getcwd()
    for root, dirs, files in os.walk(current_dir):
        for filename in files:
            statinfo = os.stat(filename)
            if statinfo.st_size > 0:
                if filename.startswith('E87A_single'):
                    E87A_water_list_single.append(filename)
                    E87A_single_frame_list.append(int(filename[23:27])+1)
                    filehandle.write(filename+'\n')
                  
    value_frame_single_list = []
    for water in E87A_water_list_single:
        value_frame_single_list.append(int(1))
        
    E87A_no_bridge_water = len(E87A_water_list_single)
    E87A_single_perc_occ = float(E87A_no_bridge_water) / 4102 * 100
    print "The E87A mutant has a Y171-wat-H89 water bridge %3d percent of the time" %(E87A_single_perc_occ)
    filehandle.write("The E87A mutant has a Y171-wat-H89 water bridge %3d percent of the time" %(E87A_single_perc_occ))
    #print "water list:%s"%(E87A_water_list_single)
    filehandle.close()
    return value_frame_single_list, E87A_single_frame_list
    
def count_E87A_double_water():
    os.chdir("/Users/yarrowmadrona/Laboratory/MD/NAMD/dosE87A/analysis/water_bridge/pdb")
    filehandle = open('E87A_double_water.txt', 'wb')
    E87A_water_list_double = []
    E87A_double_frame_list = []
    current_dir = os.getcwd()
    for root, dirs, files in os.walk(current_dir):
        for filename in files:
            statinfo = os.stat(filename)
            if statinfo.st_size > 0:
                if filename.startswith('E87A_double'):
                    E87A_water_list_double.append(filename)
                    E87A_double_frame_list.append(int(filename[23:27])+1)
                    filehandle.write(filename+'\n')
    
    value_frame_double_list = []
    for water in E87A_water_list_double:
        value_frame_double_list.append(int(2))
        
    E87A_no_bridge_water = len(E87A_water_list_double)
    E87A_doub_perc_occ = float(E87A_no_bridge_water) / 4102 * 100
    filehandle.write("The E87A mutant has a Y171-wat-wat-H89 water bridge %3d percent of the time" %(E87A_doub_perc_occ))
    filehandle.close()
    print "The E87A mutant has a Y171-wat-wat-H89 water bridge %3d percent of the time" %(E87A_doub_perc_occ)
    #print "water list:%s"%(E87A_water_list_double)
    return value_frame_double_list, E87A_double_frame_list

def count_E87G_single_water():
    os.chdir("/Users/yarrowmadrona/Laboratory/MD/NAMD/dosE87G/analysis/water_bridge/pdb")
    E87G_single_frame_list = []
    current_dir = os.getcwd()
    for root, dirs, files in os.walk(current_dir):
        for filename in files:
            statinfo = os.stat(filename)
            if statinfo.st_size > 0:
                if filename.startswith('E87G_single_water_0'):
                    E87G_single_frame_list.append(int(filename[23:27]))
    return E87G_single_frame_list


def count_E87G_double_water():
    os.chdir("/Users/yarrowmadrona/Laboratory/MD/NAMD/dosE87G/analysis/water_bridge/pdb")
    E87G_double_frame_list = []
    current_dir = os.getcwd()
    for root, dirs, files in os.walk(current_dir):
        for filename in files:
            statinfo = os.stat(filename)
            if statinfo.st_size > 0:
                if filename.startswith('E87G_double_water_0'):
                    E87G_double_frame_list.append(int(filename[23:27]))
    return E87G_double_frame_list

    #Because there are so many cross bridges with extra water in this active site these overlap, so just look at uniques for total
    #water bridges.
def E87G_water_bridge():
    filehandle = open('E87G_water_bridge.txt', 'wb')
    E87G_double_frame_list = count_E87G_double_water()
    E87G_single_frame_list = count_E87G_single_water()
    x = set()
    y = set()
    for frame in E87G_double_frame_list:
        x.add(frame)
    for frame in E87G_single_frame_list:
        y.add(frame)
    total_unique_bridges_E87G_set = set.intersection(x, y)
    
    total_unique_bridges_E87G_list = list(total_unique_bridges_E87G_set)
    total_unique_bridges_E87G_list.sort()
        
    value_frame_unique_bridge = []
    for frame in total_unique_bridges_E87G_list:
        value_frame_unique_bridge.append(int(3))
            
    E87G_no_bridge_water = len(total_unique_bridges_E87G_list)
    E87G_bridge_perc_occ = float(E87G_no_bridge_water) / 609 * 100
    filehandle.write("The E87G mutant has a Y171 water bridge H89 %3d percent of the time" %(E87G_bridge_perc_occ))
    filehandle.close()
    print "The E87G mutant has a Y171 H89 water bridge %3d percent of the time" %(E87G_bridge_perc_occ)
    return value_frame_unique_bridge, total_unique_bridges_E87G_list

def plot_water_bridge():
    y1, x1 = count_E87A_single_water()
    y2, x2 = count_E87A_double_water()
    y3, x3 = E87G_water_bridge()
    
    plt.figure("WT water bridge", figsize = (8, 2.5))
    plt.scatter(x1, y1, color = 'blue', s=450, lw = '0.03', facecolor='None') 
    plt.scatter(x2, y2, color = 'green', s=450, lw = '0.03', facecolor='None')
    plt.scatter(x3, y3, color = 'yellow', s=450, lw = '0.03', facecolor='None')
    plt.axis([-150, 4500, 0.5, 3.5])
    #plt.xlabel("Nanoseconds")
    plt.grid(False)
    plt.savefig('E87A_E87G_water_plot')
    plt.show()
    
plot_water_bridge()
    
    