import requests

url = "https://xray.cloud.getxray.app/api/v2/authenticate"

headers = {
    "Content-Type": "application/json"
}

with open("xray_auth.json", "r") as file:
    data = file.read()

response = requests.post(url, headers=headers, data=data)

# Removing double quotes from the response
cleaned_response = response.text.replace('"', '')

print(cleaned_response)
