import os
import sys
import pytest
from app.components.folder_scanner import FolderScanner
from app.components.zip_file_handler import ZipArchive
from conftest import *
from app.components.report_data_collector import *

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))


class TestFileScannerReqursion:

    def test_scan_all(self):
        print("\n")
        self.file_to_find = "moApplica"
        scanner = FolderScanner(ZIPS_ROOT)
        found = scanner.find_file_using_scandir_contains(self.file_to_find)
        print(f"\nThe following found: {found}")

    def test_collect_data(self):
        print("\n")
        self.file_to_find = "JUnit_Report"
        scanner = FolderScanner(ZIPS_ROOT)
        data_collector = scanner.collect_report_data_searching_using_contains_check(self.file_to_find)
        data_collector.print_report()
        data_collector.to_csv_file(os.path.join(ZIPS_ROOT, "report.csv"))
