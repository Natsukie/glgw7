import pytest

A=1;
B=2;
C=3;
D=0;
E=0;

def testData():
    D=A*B+A*C
    return D

def testData2():
	E=A*(B+C)
	return E

