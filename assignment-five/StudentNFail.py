import pytest
from Design_document.StudentNumber import StudentN

def test_StudentN():
	r = StudentN(200000000)
	assert r == True