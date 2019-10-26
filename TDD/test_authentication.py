import pytest
from authentication import *

def test_goodAuth():
    result = authentication("user","goodPassword")
    assert result == True

def test_badAuth():
    result = authentication("user","badPassword")
    assert result == False