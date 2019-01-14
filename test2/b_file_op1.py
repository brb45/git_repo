from shutil import copyfile, copy2 #copytree
import os
import shutil
from pathlib import Path

cur_dir = os.getcwd()#<class 'str'>
# C:\Users\jsun\Documents\pyProjects\Auto_Jenkins\unzipped_content
src_file = "doc_dir.txt"
dst_file = "doc_dir_cpy.txt"
copyfile(src_file, dst_file) #copyfile(src, dst) #destination needs writable; existing file be replaced; dst must be file name
dst_dir = "doc_dir"
copy2(src_file, dst_dir) # dst1 can be file name or directory name, src_file can't be dir.

"""
it allows dst to be a directory
it preserves the original modification and access info (mtime and atime) in the file metadata 
copy and copy2 accept directory as destination while copyfile only takes filename
copy2 copys metadata too  
copy, copy2, copyfile
"""
"""
shutil.copy(src, dst, *, follow_symlinks=True):

Copies the file src to the file or directory dst. src and dst should be strings. 
If dst specifies a directory, the file will be copied into dst using the base filename from src. 
Returns the path to the newly created file.
copy() copies the file data and the file’s permission mode (see os.chmod()). 
Other metadata, like the file’s creation and modification times, is not preserved. 
To preserve all file metadata from the original, use copy2() instead."""

"""
"""
#if os.path.isfile(dst): #fine
if os.path.isfile("log_temp.zip"): # relative path is fine, search working directory for files automatically
    print("copy file success")
if os.path.isdir(dst1):
    print("copy directory Success")
"""
dir_src = "doc_dir"
dir_dst = "doc_dir_cp2"
shutil.copytree(dir_src, dir_dst)
if os.path.isdir(dir_dst):
    print("Success")
