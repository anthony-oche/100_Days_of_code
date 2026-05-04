import requests
import os
from dotenv import load_dotenv
from requests.auth import HTTPBasicAuth

load_dotenv()

SHEETY_ENDPOINT = "https://api.sheety.co/7f84b0932b9959a9097034e354f19116/flightDeals/prices"
SHEETY_USER_ENDPOINT = "https://api.sheety.co/7f84b0932b9959a9097034e354f19116/flightDeals/users"


class DataManager:
    #This class is responsible for talking to the Google Sheet.
    def __init__(self):
        self._user = os.getenv("SHEETY_USERNAME")
        self._password = os.getenv("SHEETY_PASS")
        self._authorization = HTTPBasicAuth(self._user, self._password)
        self.destination_data = {}
        self.customer_data = {}

    def get_destination_data(self):
        response = requests.get(url=SHEETY_ENDPOINT, auth=self._authorization)
        data = response.json()
        # print(data)
        self.destination_data = data["prices"]
        return self.destination_data




    # =========================== Updated the price in the spreadsheet ====================

    def update_lowest_price(self, row_id, new_price):

        new_data = {
            "price": {
                "lowestPrice": new_price
            }
        }
        requests.put(url=f"{SHEETY_ENDPOINT}/{row_id}", json=new_data, auth=self._authorization)


    # ============================ Customers ==============================================

    def get_customer_emails(self):

        response = requests.get(url=SHEETY_USER_ENDPOINT, auth=self._authorization)

        data = response.json()
        self.customer_data = data["users"]
        return self.customer_data



