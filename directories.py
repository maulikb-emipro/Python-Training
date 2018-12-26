import os
from os.path import isdir
from pydoc import ispath


class Directories:
    "Displays all dirs and files in Directories"

    def get_directory(self, path):
        """
        func :- Retrives all files and sub directories of given path.
        param :- path of directory - string.
        return :- files and sub directories from given path.
        """
        list_of_files = os.listdir(path)
        a = []
        for dirs in list_of_files:
            new_path = path + '/' + dirs
            if isdir(new_path):
                a = self.get_directory(new_path)
                print(new_path, "directory has", len(a), "items.")
            else:
                continue
            print(a)
        return list_of_files


directory_obj = Directories()
while 1:
    path = input("Enter path of Directory :-")
    if ispath(path):
        list_of_items = directory_obj.get_directory(path)
        print(path, "has", len(list_of_items), "items.")
        print(list_of_items)
        break
    else:
        print("It's not valid path. Please enter valid path.")
