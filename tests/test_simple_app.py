import pytest
import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from app.ex import Simple


def test_simple_app():
    s = Simple("bla")
    assert s.get_name() == "bla"
