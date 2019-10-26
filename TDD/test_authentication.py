import pytest
from authentication import *

def test_goodAuth():
    result = authentication("a.b","passwordAB")
    assert result == True

def test_badAuth():
    result = authentication("cd","wrongPasswordCD")
    assert result == False

def test_unknownUserAuth():
    result = authentication("unknown","abc")
    assert result == False