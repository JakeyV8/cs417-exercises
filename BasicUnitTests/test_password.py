import pytest
from BasicUnitTests.password import validate_password
def test_validate_password_valid():
    assert validate_password("Password123") == True
def test_validate_password_boundary():
    assert validate_password("Pass1234") == True
    assert validate_password("Pass123") == False
def test_validate_password_non_string():
    with pytest.raises(TypeError):
        validate_password(12345678)
