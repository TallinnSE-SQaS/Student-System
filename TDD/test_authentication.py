import pytest
from authentication import *

def test_auth():
    result = authentication("user","password")
    assert result == True