import requests # type: ignore
response = requests.get("https://google.com")
print(response.text)
