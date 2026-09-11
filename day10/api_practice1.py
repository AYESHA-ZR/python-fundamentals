# API practice
import requests
url = "https://jsonplaceholder.typicode.com/users"

response = requests.get(url)

print(response.status_code)

Data = response.json()
print(Data)
print(type(Data))


for user in Data:
    print("name = ",user["name"])
    print("email = ",user["email"])
    print()
    
# next
# API Filtering
print("name and email of those  id is greater than 5")
for user in Data:
    if user["id"]>5:
        print("Name = ",user["name"])
        print("Email = ",user["email"])
        print()
    
    
    
    import requests

try:
    response = requests.get("https://jsonplaceholder.typicode.com/users")
    response.raise_for_status()

    data = response.json()

    for user in data:
        print("NAME =", user["name"])
        print("EMAIL =", user["email"])
        print()

except requests.exceptions.RequestException:
    print("API request failed")