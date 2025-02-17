import os
import sys
import pytest
from app.components.folder_scanner import FolderScanner
from app.components.zip_file_handler import ZipArchive
from conftest import *
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))


class TestFileScannerReqursion:

    def test_scan_all(self):
        print("\n")
        self.file_to_find = "moApplica"
        scanner = FolderScanner(ZIPS_ROOT)
        found = scanner.find_file_using_scandir_contains(self.file_to_find)
        print(f"\nThe following found: {found}")