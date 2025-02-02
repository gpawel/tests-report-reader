import os
import sys
import pytest
from app.components.folder_scanner import FolderScanner
from app.components.zip_file_handler import ZipArchive
from conftest import *
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))


class TestFileScanner:

    def setup_method(self, method):
        self.archive = ZipArchive(ZIP_FILE_PATH)
        self.temp = os.path.join(ZIPS_ROOT, self.archive.unzip())
        self.file_to_find = "DemoApplicationTests.java"
        self.scanner = FolderScanner(self.temp)

    def teardown_method(self, methods):
        self.archive.remove_temp_folder()

    def test_find_file_using_walk(self):
        print(f"\nfile to find {self.file_to_find}")
        self.scanner.find_files_using_walk(self.file_to_find)

    def test_find_file_using_scandir_equal(self):
        print(f"\nfile to find {self.file_to_find}")
        found = self.scanner.find_file_using_scandir_equal(self.file_to_find)
        print(f"\nThe following found: {found}")

    def test_find_file_using_scandir_contains_full_name(self):
        print(f"\nfile to find {self.file_to_find}")
        found = self.scanner.find_file_using_scandir_contains(self.file_to_find)
        print(f"\nThe following found: {found}")

    def test_find_file_using_scandir_contains_part(self):
        self.file_to_find = "moApplica"
        print(f"\nfile to find {self.file_to_find}")
        found = self.scanner.find_file_using_scandir_contains(self.file_to_find)
        print(f"\nThe following found: {found}")
