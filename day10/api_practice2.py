# API Project
# user api project
import requests
try:
    response = requests.get("https://jsonplaceholder.typicode.com/users")
    response.raise_for_status()

    data = response.json()

    for user in data:
        print("----- USER INFO -----")
        print("Name     =", user["name"])
        print("Username =", user["username"])
        print("Email    =", user["email"])
        print()
        
            
    print("greater than 5")
    for user in data:
    
         if user["id"]>5:
             print("----- USER INFO -----")
             print("Name     =", user["name"])
             print("Username =", user["username"])
             print("Email    =", user["email"])
             print()
except requests.exceptions.RequestException:
    print("API request failed")
