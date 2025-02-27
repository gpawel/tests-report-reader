import os
import filecmp
from app.components.zip_file_handler import ZipArchive
from app.components.report_data_collector import *


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
    return use_os_scandir_gen(root_folder, file_to_find, __is_equal, found)


def use_os_scandir_contains(root_folder: str, file_to_find: str, found=[]):
    return use_os_scandir_gen(root_folder, file_to_find, __is_contain, found)


def collect_data_using_equal_comparison(root_folder: str, file_to_find: str, data_collector):
    return collect_data_gen(root_folder, file_to_find, __is_equal, data_collector)


def collect_data_using_contains_check(root_folder: str, file_to_find: str, data_collector):
    return collect_data_gen(root_folder, file_to_find, __is_contain, data_collector)


def use_os_scandir_gen(root_folder: str, file_to_find: str, comparison_function, found=[]):
    result = []
    for entry in os.scandir(root_folder):
        if entry.is_file():
            folder, file_part = os.path.split(entry.path)
            if file_part.endswith(".zip"):
                process_zip_archive(entry, file_to_find, comparison_function, result)
                if len(result) > 0:
                    found.append( result )
            if comparison_function(file_to_find, file_part):
                found.append( os.path.join(root_folder, file_part) )
        elif entry.is_dir():
            use_os_scandir_gen( entry.path, file_to_find, comparison_function, result)
    return found


def collect_data_gen(root_folder: str, file_to_find: str, comparison_function, data_collector: DataCollector):
    for entry in os.scandir(root_folder):
        if entry.is_file():
            folder, file_part = os.path.split(entry.path)
            if file_part.endswith(".zip"):
                process_zip_archive_to_collect_data(entry, file_to_find, comparison_function, data_collector)
            if comparison_function(file_to_find, file_part):
                data_collector.process_report_file(entry)
        elif entry.is_dir():
            collect_data_gen(entry.path, file_to_find, comparison_function, data_collector)
    return data_collector


def process_zip_archive(zip_file, file_to_find, comparison_function, found):
    archive = ZipArchive(zip_file)
    print(f"UNZIPING {zip_file}")
    temp = os.path.join(zip_file.path, archive.unzip())
    print(f"TEMP FOLDER: {temp}")
    result = use_os_scandir_gen(temp, file_to_find, comparison_function, found)
    archive.remove_temp_folder()
    return result


def process_zip_archive_to_collect_data(zip_file, file_to_find, comparison_function, data_collector: DataCollector):
    archive = ZipArchive(zip_file)
    print(f"UNZIPING {zip_file}")
    temp = os.path.join(zip_file.path, archive.unzip())
    print(f"TEMP FOLDER: {temp}")
    result = collect_data_gen(temp, file_to_find, comparison_function, data_collector)
    archive.remove_temp_folder()
    return result


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

    def collect_report_data_searching_file_using_equal_comparison(self, file_name, data_collector: DataCollector):
        return collect_data_using_equal_comparison(self.folder, file_name, data_collector)

# DataCollector('//testsuite')
    def collect_report_data_searching_using_contains_check(self, file_name, data_collector: DataCollector):
        return collect_data_using_contains_check(self.folder, file_name, data_collector)



