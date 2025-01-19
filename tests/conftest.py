import os
import pytest

CURRENT = os.path.dirname(__file__)
ROOT = os.path.dirname(CURRENT)
ZIPS_ROOT = os.path.join(ROOT, "zips")



@pytest.fixture()
def get_paths():
    return ROOT, ZIPS_ROOT
