import pytest
from Design_document.FileSize import fileSize

def test_sizeCheck():
	r = fileSize(40)
	assert r == True