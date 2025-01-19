import os
from zipfile import ZipFile
import shutil
import time


class ZipArchive:

    def __init__(self, file_to_unzip: str):
        self.temp_folder = None
        self.file_to_unzip = file_to_unzip

    def unzip(self, tmp_fldr='') -> str:
        zipper = ZipFile(self.file_to_unzip, "r")
        if tmp_fldr == '':
            tmp_fldr = self.__get_temp_folder()
        self.temp_folder = tmp_fldr
        zipper.extractall(self.temp_folder)
        return self.temp_folder

    def remove_temp_folder(self) -> bool:
        try:
            shutil.rmtree(self.temp_folder)
            return True
        except OSError as ex:
            print(f"Error, {ex.strerror}: {self.temp_folder}")
            return False

    def get_temp_folder(self) -> str:
        return self.temp_folder

    def __get_temp_folder(self):
        rnd = round(time.time() * 1000)
        return os.path.dirname(self.file_to_unzip) + os.sep + "temp" + str(rnd)
