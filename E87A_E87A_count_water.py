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

def count_E87G_double_water():
    os.chdir("/Users/yarrowmadrona/Laboratory/MD/NAMD/dosE87A/analysis/water_bridge/pdb")
    filehandle = open('E87G_double_water.txt', 'wb')
    E87G_water_list_double = []
    E87G_double_frame_list = []
    current_dir = os.getcwd()
    for root, dirs, files in os.walk(current_dir):
        for filename in files:
            statinfo = os.stat(filename)
            if statinfo.st_size > 0:
                if filename.startswith('E87G_double'):
                    E87G_water_list_double.append(filename)
                    E87G_double_frame_list.append(int(filename[23:27])+1)
                    filehandle.write(filename+'\n')
    
    value_frame_double_list = []
    for water in E87G_water_list_double:
        value_frame_double_list.append(int(2))
        
    E87G_no_bridge_water = len(E87G_water_list_double)
    E87G_doub_perc_occ = float(E87G_no_bridge_water) / 4102 * 100
    filehandle.write("The E87G mutant has a Y171-wat-wat-H89 water bridge %3d percent of the time" %(E87G_doub_perc_occ))
    filehandle.close()
    print "The E87G mutant has a Y171-wat-wat-H89 water bridge %3d percent of the time" %(E87G_doub_perc_occ)
    #print "water list:%s"%(E87G_water_list_double)
    return value_frame_double_list, E87G_double_frame_list


def plot_water_bridge():
    y1, x1 = count_E87A_single_water()
    y2, x2 = count_E87A_double_water()
    y3, x3 = count_E87G_double_water()
    plt.figure("WT water bridge", figsize = (8, 3))
    plt.scatter(x1, y1, color = 'blue', s=650, lw = '0.03', facecolor='None') 
    plt.scatter(x2, y2, color = 'green', s=650, lw = '0.03', facecolor='None')
    plt.scatter(x3, y3, color = 'orange', s=450, lw = '0.03', facecolor="None")
    plt.axis([-1, 4000, 0.5, 2.5])
    #plt.xlabel("Nanoseconds")
    plt.grid(False)
    plt.savefig('E87A_water_plot')
    plt.show()
    
plot_water_bridge()
    
    