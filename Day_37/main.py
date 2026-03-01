import requests
from datetime import datetime
from dotenv import load_dotenv
import os

load_dotenv()

USERNAME = os.getenv("USERNAME")
TOKEN = os.getenv("TOKEN")

pixela_endpoint = "https://pixe.la/v1/users"

#Todo: creating a pixela account
user_params = {
    "token": TOKEN,
    "username": USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes",
}

# response = requests.post(url=pixela_endpoint, json=user_params)
# print(response.text)

#Todo: creating a graph
graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"

graph_json = {
    "id": "graph1",
    "name": "Cycling graph",
    "unit": "km",
    "type": "float",
    "color": "sora",
}
headers = {
    "X-USER-TOKEN": TOKEN,
}

response = requests.post(url=graph_endpoint, json=graph_json, headers=headers)
print(response.text)

#Todo: posting a value to the graph
today = datetime(2025, 12, 13)
value_endpoint = f"{graph_endpoint}/graph1"

value_params = {
    "date": today.strftime("%Y%m%d"),
    "quantity": "11.5"
}

# response = requests.post(url=value_endpoint, json=value_params, headers=headers)
# print(response.text)

#Todo: updating the graph
update_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/graph1/{today.strftime("%Y%m%d")}"

update_params = {
    "quantity": "5"
}
# response = requests.put(url=update_endpoint, json=update_params, headers=headers)
# print(response.text)

#Todo: deleting a pixel
delete_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/graph1/{value_params['date']}"

# response = requests.delete(url=delete_endpoint, headers=headers)
# print(response.text)