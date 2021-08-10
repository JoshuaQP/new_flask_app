import requests


TEST_USER = {
    "first_name": "Joshua",
    "last_name": "Palmier",
    "hobbies": "skiing and playing ping pong",
    "active": 1


}

URL= "http://127.0.0.1:5000/users"


def test_user_creation():
    out = requests.post(URL, json=TEST_USER)
    if out.status_code == 201:
        print(out.json())
    else:
        print("something went wrong.")


def test_user_deavtivate():
    out = requests.delete("%s/2" % URL)
    if out.status_code == 200:
        print(out.json())

    else:
        print("somewthing went wrong")

if __name__ == "main":
    test_user_creation()
    test_user_deavtivate()
    