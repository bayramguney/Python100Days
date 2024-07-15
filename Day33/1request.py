# http://open-notify.org/Open-Notify-API/ISS-Location-Now/
import requests

response = requests.get(url="http://api.open-notify.org/iss-now.json")
print(response)   # <Response [200]>

# if requests.status_codes == 404:
#     raise Exception("The resource doe not exist")
# elif response.status_code == 401:
#     raise Exception("You are not authorized to access this data")

response.raise_for_status()
data = response.json()
print(data)  # {'message': 'success', 'iss_position': {'longitude': '-20.1153', 'latitude': '27.8285'}, 'timestamp': 1720984844}
data2 = response.json()["iss_position"]
print(data2)  # {'longitude': '-20.1153', 'latitude': '27.8285'}

longitude = data["iss_position"]["longitude"]
latitude = data["iss_position"]["latitude"]
iss_position = (longitude,latitude)
print(iss_position)

