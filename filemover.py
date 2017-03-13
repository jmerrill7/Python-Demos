####This simple program moves the contents of Folder_A to Folder_B on
####the desktop and prints out the names of the files moved.

import shutil
import os
import os.path

source = (r"C:\Users\James\Desktop\Folder_A")
dest = (r"C:\Users\James\Desktop\Folder_B")

for file in os.listdir(source):
    file = os.path.join(source, file)
    if (file.endswith(".txt")):
        shutil.move(file, dest)
        print file
