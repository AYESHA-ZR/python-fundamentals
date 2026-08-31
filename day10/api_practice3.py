# api+ user input
import requests
while True:
   
    try:
        user_id = int(input("Enter user ID (1-10) = "))

        if 1 <= user_id <= 10:
            break
        else:
            print("Please enter a number between 1 and 10.")

    except ValueError:
        print("Please enter a valid number...")
try:
    response = requests.get( f"https://jsonplaceholder.typicode.com/users/{user_id}")
    response.raise_for_status()

    user = response.json()
    print("\n----- USER INFO -----")
    print("Name     =", user["name"])
    print("Username =", user["username"])
    print("Email    =", user["email"])
    
except requests.exceptions.RequestException:
    print("user not found and API request failed")
