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
