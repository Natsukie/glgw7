import pytest

from Design_document.Pawpint import CheckSutdent

def test_Student():
	r = CheckSutdent("abc10")
	assert r == True