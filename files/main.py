__winc_id__ = "ae539110d03e49ea8738fd413ac44ba8"
__human_name__ = "files"

#1 Use Python's standard library to find the password. Clean_cache: takes no arguments and creates an empty folder named cache in the current directory. If it already exists, it deletes everything in the cache folder.
import os
import shutil
from zipfile import ZipFile

def clean_cache ():
    if not os.path.exists('files/cache'):
        os.makedirs('files/cache')
    else: 
        shutil.rmtree('files/cache')
        os.makedirs('files/cache')
    return dir

#2 Cache_zip: takes a zip file path (str) and a cache dir path (str) as arguments, in that order.
def cache_zip(zip_file_path, cache_dir_path):
    with ZipFile(zip_file_path, 'r') as zipObj:
        zipObj.extractall(cache_dir_path)
    return zipObj

#3 Cached_files: takes no arguments and returns a list of all the files in the cache. The file paths should be specified in absolute terms.
def cached_files():
    path= os.path.abspath('files\cache')
    list_cached_files = [os.path.join(path, file) for file in os.listdir(path)]
    return list_cached_files

#4 Find_password: takes the list of file paths from cached_files as an argument. This function should read the text in each one to see if the password is in there.
def find_password(list_cached_files):
    for file in list_cached_files:
        open_file = open(file,'r')
        text = open_file.readlines()
        if 'password' in str(text):
            for string in text:
                if 'password' in string:
                    password = (string[string.find(' ')+1:-1])
    return password

if __name__ == '__main__':
    clean_cache() 
    cache_zip('files/data.zip', 'files/cache' )
    print(cached_files()) 
    print(find_password(cached_files()))