import sys
import os
from conftest import *
from app.components.zip_file_handler import ZipArchive

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))


def test_zip_extraction_using_default_temp_folder_name():
    __check_zip_file_extraction()


def test_zip_extraction_user_custom_temp_folder_name():
    __check_zip_file_extraction("temp_folder_name")


def test_zips_folder_path():
    print("\nCURRENT: " + CURRENT + "\nROOT: " + ROOT + "\nZIPS: " + ZIPS_ROOT)


def __check_zip_file_extraction(folder_name = '' ):
    # file_name = "demo.zip"
    # file_path = os.path.join(ZIPS_ROOT, file_name)
    # print("\nFILE PATH: " + file_path)
    archive = ZipArchive(ZIP_FILE_PATH)
    temp = os.path.join(ZIPS_ROOT, archive.unzip(folder_name))
    assert os.path.exists(temp)
    assert os.path.isdir(temp)
    assert os.listdir(temp)
    archive.remove_temp_folder()
    assert not (os.path.exists(temp))