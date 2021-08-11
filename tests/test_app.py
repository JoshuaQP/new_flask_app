import pytest

MOCK_DICTIONARY = {
    "first_name": "joshua",
    "last_name": "palmier",
    "active": 1,
    "age": 100,
    "username":"JoshuaPalmier"
}

def test_dictionary_has_valid_age():
    assert isinstance(MOCK_DICTIONARY["age"], int)


def test_dictionary_has_valid_username():
    assert (MOCK_DICTIONARY.get("username") == "JoshuaPalmier")



  