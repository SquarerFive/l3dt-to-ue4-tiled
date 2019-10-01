## (C) Aiden Soedjarwo 2019
#
# Python 3.7
#
# This is used to batch rename all heightmaps with the xy suffix to x_y
# eg : Landscape_x0y0 -> Landscape_x0_y0


import os
import time
directory = str(input("Enter Directory: "))
print(directory)
for file in os.listdir(directory):
    source = directory + "/" + file
    
    sourceNew = source.replace('y','_y')
    tag = '{}'.format(directory)
    sourceNew = sourceNew.replace(tag, '')
    sourceNew = directory + sourceNew
    os.rename(source, sourceNew)
   # print(source)
    print(sourceNew)
print("Finished Renaming")
print("Exiting...")
time.sleep(5)
quit()
