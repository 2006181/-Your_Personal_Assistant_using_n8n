import requests


user_message = "Can you tell me about black holes in 3-4 lines"

request_message = {"message": user_message}

WEBHOOK_URL = st.secrets["WEBHOOK_URL"]  # replace with your n8n webhook URL

response = requests.post(url, json=request_message)

print(response.status_code)

print(response.json()[0]["output"])
