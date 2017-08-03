import os
import glob
TARGET_DIR = '.'
#define varriables
#FILE_NEW = FILE_OLD.replace(E2, E1)
#FILE_OLD = TARGET_DIR
#prevName = "filename*"
#newName = "mscyp189se_1_E1_*"

#define the function
for FILE_OLD in os.listdir(TARGET_DIR):
    #FILE_OLD = TARGET_DIR + FILE_OLD
    print FILE_OLD
    FILE_NEW = FILE_OLD.replace("E2","E1")
    print FILE_NEW
    #FILE_NEW = TARGET_DIR + FILE_NEW
    os.rename(FILE_OLD, FILE_NEW)
