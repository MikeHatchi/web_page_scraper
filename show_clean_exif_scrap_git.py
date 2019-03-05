#!/Users/Home/anaconda3/bin/python
# -*- coding: utf-8 -*-


import piexif
import os


# works!!!
path_master = '/Users/Home/folder_directory_where_your_picts_are_located'

for subdir, dirs, files in os.walk(path_master):
    for file in files:
        # print(os.path.join(subdir, file))

        full_path = os.path.join(subdir, file)
        if full_path == subdir + '/.DS_Store':
            continue
        data = piexif.load(full_path)
        # print("Exif:", data)
        piexif.remove(full_path)
        empty = piexif.load(full_path)
        print("cleaning done:", empty)
