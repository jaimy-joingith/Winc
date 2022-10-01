__winc_id__ = "ae539110d03e49ea8738fd413ac44ba8"
__human_name__ = "files"

#1 Use Python's standard library to find the password. Clean_cache: takes no arguments and creates an empty folder named cache in the current directory. If it already exists, it deletes everything in the cache folder.

import os
import glob
import zipfile

def clean_cache():
    path = './files/cache'
    if os.path.exists(path):
        files = glob.glob(path + '/*')
        for f in files:
            os.remove(f)
    else:
        os.mkdir(path)

#2 cache_zip: takes a zip file path (str) and a cache dir path (str) as arguments, in that order.

def cache_zip(target_path, destination_path):
    with zipfile.ZipFile(target_path, 'r') as zip_ref:
        zip_ref.extractall(destination_path)

#3 cached_files: takes no arguments and returns a list of all the files in the cache. The file paths should be specified in absolute terms.

def cached_files():
    file_list = []
    path = './files/cache'
    files = glob.glob(path + '/*')
    for f in files:
        file_list.append(os.path.abspath(f))
    return file_list

#4 find_password: takes the list of file paths from cached_files as an argument. This function should read the text in each one to see if the password is in there.

def find_password(file_list):
    for file in file_list:
        with open(file, 'r') as f:
            data = f.read()
            if 'password' in data:
                chunks = data.split('\n')
                for chunk in chunks:
                    if 'password' in chunk:
                        return chunk[chunk.find(' ')+1:]