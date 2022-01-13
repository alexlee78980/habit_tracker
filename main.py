import requests
import datetime
pixela_endpoint = "https://pixe.la/v1/users"
TOKEN = "asdasfafasjfasfjasfa"
USERNAME = "alexlee"
user_params = {
    "token": TOKEN,
    "username": USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes"
}
# response = requests.post(url=pixela_endpoint, json=user_params)
# print(response.text)
GRAPH_ID = "graph1"
graph_params = {
    "id": GRAPH_ID,
    "name": "daily tasks",
    "unit": "completed",
    "type": "int",
    "color": "sora"
}
headers = {
    "X-USER-TOKEN": TOKEN
}
# graph_endpoint = f'{pixela_endpoint}/{USERNAME}/graphs'
# graph_response = requests.post(url=graph_endpoint, json=graph_params, headers=headers)
# print(graph_response.text)

today = datetime.date.today()
date = ""
for s in str(today):
    try:
        int(s)
    except ValueError:
        pass
    else:
        date += s
print(date)
quantity = input("How many tasks did you complete today?: ")
post_params = {
    "date": date,
    "quantity": quantity
}
post_endpoint = f'{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}'
post_response = requests.post(url=post_endpoint, json=post_params, headers=headers)
print(post_response)