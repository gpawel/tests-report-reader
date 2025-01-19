import sys
import os
from conftest import *
from app.components.zip_file_handler import ZipArchive

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))


def test_zip_file_extraction():
    file_name = "demo.zip"
    file_path = os.path.join(ZIPS_ROOT, file_name)
    print("\nFILE PATH: " + file_path)
    archive = ZipArchive(file_path)
    temp = os.path.join(ZIPS_ROOT, archive.unzip())
    assert os.path.exists(temp)
    assert os.path.isdir(temp)
    archive.remove_temp_folder()
    assert not (os.path.exists(temp))


def test_zips_folder_path():
    print("\nCURRENT: " + CURRENT + "\nROOT: " + ROOT + "\nZIPS: " + ZIPS_ROOT)
