####This simple program moves the contents of Folder_A
####that have been edited/modified within the past 24 hours
####and moves them to Folder_B. 

import shutil
import os
import os.path
import datetime

source = (r"C:\Users\James\Desktop\Folder_A")
dest = (r"C:\Users\James\Desktop\Folder_B")

for file in os.listdir(source):
    from datetime import date, datetime, time, timedelta
    file = os.path.join(source, file)
    now = datetime.now()
    before = now - timedelta(hours=24)
    last_modified_date = datetime.fromtimestamp(os.path.getmtime(file))
    if  file.endswith(".txt") and last_modified_date > before:
        shutil.move(file, dest)
        print "The following file has been moved to Folder_B:{}".format(file)

