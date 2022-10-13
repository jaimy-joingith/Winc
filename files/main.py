__winc_id__ = "ae539110d03e49ea8738fd413ac44ba8"
__human_name__ = "files"

from importlib.metadata import files
import os # 1, 2, 3
import shutil # 1
from zipfile import ZipFile # 2


#1 Use Python's standard library to find the password. Clean_cache: takes no arguments and creates an empty folder named cache in the current directory. If it already exists, it deletes everything in the cache folder.
def clean_cache():
    name = 'cache'
    if os.path.isdir(os.path.join(os.getcwd(),'files', 'cache')):
        shutil.rmtree(os.path.join(os.getcwd(),'files', 'cache'))
    os.makedirs(os.path.join(os.getcwd(),'files', 'cache'))
    return f'{name} is created'

#2 Cache_zip: takes a zip file path (str) and a cache dir path (str) as arguments, in that order.
def cache_zip(zip_file_path, cache_dir_path):
    with ZipFile(zip_file_path, 'r') as zip_ref:
        zip_ref.extractall(cache_dir_path)
    return 'zip is unpacked in folder'

#3 Cached_files: takes no arguments and returns a list of all the files in the cache. The file paths should be specified in absolute terms.
def cached_files():
    filelist = []
    for file in os.listdir(os.path.join(os.getcwd(),'files', 'cache')):
        filelist.append(os.path.join(os.path.abspath(os.path.join(os.getcwd(),'files', 'cache')), file))
    return filelist

#4 Find_password: takes the list of file paths from cached_files as an argument. This function should read the text in each one to see if the password is in there.
def find_password(filelist):
    for file in filelist:
        searchfile = open(file, "r")
        for line in searchfile:
            if ("password") in line:
                return line.replace("password: ", "").rstrip('\n')

if __name__ == '__main__':
    dir_path = os.path.join(os.getcwd(),'files', 'cache')
    zip_path = os.path.join(os.getcwd(),'files', 'data.zip')
    print(clean_cache())
    print(cache_zip(zip_path, dir_path))
    print(cached_files())
    print(find_password(cached_files()))