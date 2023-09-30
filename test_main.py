"""
Test goes here

"""

from mylib.extract import extract
from mylib.transform_load import load
from mylib.query import query
import os

def test_extract():
    file_path = extract()
    assert os.path.exists(file_path)

def test_load():
    load()

def test_query():
    result = query()
