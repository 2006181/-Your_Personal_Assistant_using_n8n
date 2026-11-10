import requests


user_message = "Can you tell me about black holes in 3-4 lines"

request_message = {"message": user_message}

url = "https://rahul23012006.app.n8n.cloud/webhook-test/5467c41d-d072-41bd-b2f8-22190b2f1bad"

response = requests.post(url, json=request_message)

print(response.status_code)

print(response.json()[0]["output"])
