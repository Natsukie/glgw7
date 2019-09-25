import pytest
from Design_document.FileSize import fileSize

def test_sizeCheck():
	r = fileSize(99999999999)
	assert r == True