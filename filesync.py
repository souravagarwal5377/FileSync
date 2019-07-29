import os
import time
import stat
from datetime import datetime
from shutil import copyfile

def timestampCompare(timeA,timeB):
    t1 = datetime.strptime(timeA, "%a %b %d %H:%M:%S %Y")
    t2 = datetime.strptime(timeB, "%a %b %d %H:%M:%S %Y")

    difference = t1-t2
    if t1>t2:
        return 1
    return 0

#acceptiung folder names as inputs

folderA = input()
folderB = input()

#getting all files in each folder

filesA = os.listdir(folderA)
filesB = os.listdir(folderB)

for files in filesA :
    if files in filesB:
        fileStatsObjA = os.stat (folderA + "\\" + files)
        fileStatsObjB = os.stat (folderB + "\\" + files)
        modTimeA = time.ctime(fileStatsObjA [ stat.ST_MTIME ])
        modTimeB = time.ctime(fileStatsObjB [ stat.ST_MTIME ])
        result = timestampCompare(modTimeA,modTimeB)
        if result == 1:
            os.remove(folderB+"\\"+files)
            copyfile(folderA+"\\"+files,folderB+"\\"+files)
        else:
            os.remove(folderA+"\\"+files)
            copyfile(folderB+"\\"+files,folderB+"\\"+files)
    else:
        copyfile(folderA+"\\"+files,folderB+"\\"+files)

for files in filesB:
    if files not in filesA:
        copyfile(folderB+"\\"+files,folderA+"\\"+files)

print("Done")




