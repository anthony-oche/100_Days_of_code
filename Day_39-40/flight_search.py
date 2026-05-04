import os
import requests
from dotenv import load_dotenv

load_dotenv()

FLIGHT_ENDPOINT = "https://serpapi.com/search"

class FlightSearch:
    #This class is responsible for talking to the Flight Search API.
    def __init__(self):
        self._api_key = os.getenv("FLIGHT_API_KEY")


    def check_flights(self, origin_city_code, destination_city_code, from_time, to_time, is_direct=True):

        query = {
            "engine": "google_flights",
            "departure_id": origin_city_code,
            "arrival_id": destination_city_code,
            "outbound_date": from_time.strftime("%Y-%m-%d"),
            "return_date": to_time.strftime("%Y-%m-%d"),
            "type": 1,
            "adults": 1,
            "currency": "USD",
            "api_key": self._api_key
        }

        if is_direct:
            query["stops"] = "1"

        response = requests.get(url=FLIGHT_ENDPOINT, params=query)

        if response.status_code != 200:
            print(f"check_flights() response code: {response.status_code}")
            return None

        data = response.json()
        if "error" in data:
            print(f"check_flights() response code: {response.status_code}")
            return None
        return data
