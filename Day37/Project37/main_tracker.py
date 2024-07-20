# https://docs.pixe.la/
# https://requests.readthedocs.io/en/latest/api/
# https://pixe.la/
# https://www.w3schools.com/python/python_datetime.asp

import requests
from datetime import datetime

USERNAME = "guney"
TOKEN = "123456789"
GRAPH_ID = "graph1"

pixela_endpoint = "https://pixe.la/v1/users"
user_params = {
    "token":TOKEN,
    "username":USERNAME,
    "agreeTermsOfService":"yes",
    "notMinor":"yes"
}
#  create user
# response = requests.post(url=pixela_endpoint,json=user_params)   # we will run this request just to create the user
# print(response.text)

# create graph
graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"
graph_config = {
    "id":GRAPH_ID,
    "name":"Cycling Graph",
    "unit":"Km",
    "type":"float",
    "color":"kuro"
}
headers = {
    "X-USER-TOKEN":TOKEN
}
# response1 = requests.post(url=graph_endpoint,json=graph_config,headers=headers)  # second step
# print(response1.text)

# update graph
today = datetime.now()
pixel_creation_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}"
pixel_data = {
    "date":today.strftime("%Y%m%d"),
    "quantity":"9.74"
}
# response2 = requests.post(url=pixel_creation_endpoint,json=pixel_data,headers=headers)  # third step
# print(response2.text)

# update record
update_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}/{today.strftime("%Y%m%d")}"
new_pixel_data = {
    "quantity": input("How many kilometers did you cycle today")
}
response3 = requests.put(url=update_endpoint,json=new_pixel_data,headers=headers)   # step 4
print(response3)

# delete record
delete_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}/{today.strftime("%Y%m%d")}"
# response4 = requests.delete(url=delete_endpoint,headers=headers)
# print(response4)
