#! python3
# - backAndRename.py - Learning the copytree and move functions of shutil

import shutil, os

os.chdir('S:\\Documents\\GitHub')
# Copies all folder content to new folder
shutil.copytree('S:\\Documents\\GitHub\\ATBS\\Chapter_9', 'S:\\Documents\\GitHub\\ATBS_C9')
