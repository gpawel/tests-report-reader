import os
import pytest

CURRENT = os.path.dirname(__file__)
ROOT = os.path.dirname(CURRENT)
ZIPS_ROOT = os.path.join(ROOT, "zips")
ZIP_FILE_NAME = "demo.zip";
ZIP_FILE_PATH = os.path.join(ZIPS_ROOT, ZIP_FILE_NAME)




@pytest.fixture()
def get_paths():
    return ROOT, ZIPS_ROOT, ZIP_FILE_NAME, ZIP_FILE_PATH
