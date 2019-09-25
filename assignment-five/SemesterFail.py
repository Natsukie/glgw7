import pytest
from Design_document.Semester import myfunc

def testSpecialAssertions():
	with pytest.raises(ValueError, match = r".* 2020 .*"):
		myfunc()
		