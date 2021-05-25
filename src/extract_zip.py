#!/usr/local/bin/python3.8

from os.path import isdir, isfile
from os import listdir
import gzip


# list of constant
EXT = 'zip'

PATH_ZIP = '/home/ograbar/NGO/Data/saved' # store downloaded files from web site
PATH_EXTRACT = '/home/ograbar/NGO/Data/extract' # temp dir for exracting zip file
PATH_LOADED = '/home/ograbar/NGO/Data/saved' # after loaded data top DB save file to this dir




def get_files(path=PATH_ZIP):
    """
        Args
        path - path where store zip files
        Return list of zip files if file not found return None

    """
    if isdir(path):
        return [''.join([path,sfile]) for sfile in listdir(path)]
    else:
        return None

def extract(files, extract_to):
    """
    Extract zip file into directory determined in extract_to

    Return result of extraction
        0 - success extraction of  file
        1 - file not found
        2 - archive is broken
        3 - extract dir not found
    """
    pass

if __name__ == '__main__':
    print('test')
    print(get_files())
#with gzip.open('/home/joe/'file.txt.gz', 'rb') as f:
    #$file_content = f.read()

