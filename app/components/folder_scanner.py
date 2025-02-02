import os
import filecmp


def use_os_walk(root_folder: str, file_to_find: str):
    for dirpath, dirnames, filenames in os.walk(root_folder):
        print(f"dirpath: {dirpath}")
        for dir_name in dirnames:
            print(f"    dir: {os.path.join(dirpath, dir_name)}")
            for file_name in filenames:
                print(f"        checking file: {file_name}")
                if file_name == file_to_find:
                    print(f"filenames: {os.path.join(os.path.join(dirpath, dir_name), file_name)} ")


def use_os_scandir_equal(root_folder: str, file_to_find: str, found=[]):
    return use_os_scandir_gen(root_folder, file_to_find, __is_equal, found=[])


def use_os_scandir_contains(root_folder: str, file_to_find: str, found=[]):
    return use_os_scandir_gen(root_folder, file_to_find, __is_contain, found=[])


def use_os_scandir_gen(root_folder: str, file_to_find: str, comparison_function, found=[]):
    print(f"scanning {root_folder}")
    for entry in os.scandir(root_folder):
        print(f"    entry: {entry.path}")
        if entry.is_file():
            folder, file_part = os.path.split(entry.path)
            print(f"    file part: {file_part}")
            if comparison_function(file_to_find, file_part):
                print(f"FILE IS FOUND: {file_part}")
                found.append(os.path.join(root_folder, file_to_find))
                return found
        elif entry.is_dir():
            use_os_scandir_gen(entry.path, file_to_find, comparison_function, found)
    return found


def __is_equal(s_1:str, s_2:str):
    return s_1 == s_2


def __is_contain(this_str:str, in_this_str:str):
    if this_str not in in_this_str:
        return False
    return True


class FolderScanner:

    def __init__(self, folder: str):
        self.folder = folder

    def find_files_using_walk(self, file_name):
        use_os_walk(self.folder, file_name)

    def find_file_using_scandir_equal(self, file_name):
        return use_os_scandir_equal(self.folder, file_name)

    def find_file_using_scandir_contains(self, file_name):
        return use_os_scandir_contains(self.folder, file_name)



