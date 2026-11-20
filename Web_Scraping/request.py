
import requests

url = "https://jsonplaceholder.typicode.com/users"

try:
    response = requests.get(
        url,
        headers={"User-Agent": "Mozilla/5.0"},
        timeout=15
    )

    response.raise_for_status()

    data = response.json()

    print("Status Code:", response.status_code)

    for user in data:
        print(user["name"], user["email"])

except requests.exceptions.RequestException as e:
    print("Error:", e)
