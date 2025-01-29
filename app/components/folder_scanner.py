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


def use_os_scandir(root_folder: str, file_to_find: str, found=[]):
    print(f"scanning {root_folder}")
    for entry in os.scandir(root_folder):
        print(f"    entry: {entry.path}")
        if entry.is_file():
            folder, file_part = os.path.split(entry.path)
            print(f"    file part: {file_part}")
            if file_part == file_to_find:
                print(f"FILE IS FOUND: {file_part}")
                found.append(os.path.join(root_folder, file_to_find))
                return found
        elif entry.is_dir():
            use_os_scandir(entry.path, file_to_find, found)
    return found


class FolderScanner:

    def __init__(self, folder: str):
        self.folder = folder

    def find_files_using_walk(self, file_name):
        use_os_walk(self.folder, file_name)

    def find_file_using_scandir(self, file_name):
        return use_os_scandir(self.folder, file_name)




