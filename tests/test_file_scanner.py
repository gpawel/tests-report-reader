import os
import sys
import pytest
from app.components.folder_scanner import FolderScanner
from app.components.zip_file_handler import ZipArchive
from conftest import *
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))


def setup():
    archive = ZipArchive(ZIP_FILE_PATH)
    temp = os.path.join(ZIPS_ROOT, archive.unzip())
    file_to_find = "DemoApplication.java"
    scanner = FolderScanner(temp)
    return archive, temp, file_to_find, scanner


def test_find_file_using_walk():
    archive, temp, file_to_find, scanner = setup()
    print(f"\nfile to find {file_to_find}")
    scanner.find_files_using_walk(file_to_find)


def test_find_file_using_scandir():
    archive, temp, file_to_find, scanner = setup()
    print(f"\nfile to find {file_to_find}")
    found = scanner.find_file_using_scandir(file_to_find)
    print(f"\nThe following found: {found}")
