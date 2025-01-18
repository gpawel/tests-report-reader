import os
from zipfile import ZipFile
import shutil
import time


class ZipArchive:

    def __init__(self, file_to_unzip: str):
        self.file_to_unzip = file_to_unzip
        rnd = round(time.time() * 1000)
        self.temp_folder = os.path.dirname(self.file_to_unzip) + os.sep + "temp" + str(rnd)

    def unzip_file(self) -> str:
        zipper = ZipFile(self.file_to_unzip, "r")
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
