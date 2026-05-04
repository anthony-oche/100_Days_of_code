import requests_cache
from datetime import datetime, timedelta
from data_manager import DataManager
from flight_search import FlightSearch
from flight_data import FlightData, find_cheapest_flight
from pprint import pprint
from notification_manager import NotificationManager
import smtplib

# ==================== Conserve requests and preserve your free plan ====================
# Here we are not caching anything ending in *.sheety.co
# everything else is cached for 1 hour (3600 seconds).
# feel free to experiment!
requests_cache.install_cache(
    "flight_cache",
    urls_expire_after={
        "*.sheety.co*": requests_cache.DO_NOT_CACHE,
        "*": 3600,
    }
)


#============================= Talk to Sheety ==========================

data_manager = DataManager()
sheet_data = data_manager.get_destination_data()
# pprint(sheet_data)

#=============================== Set the Dates ==========================

t = datetime.now()
tomorrow = t + timedelta(days=1)
six_month_from_today = t + timedelta(weeks=24)

#============================ Do a Flight Search =====================

ORIGIN_CITY_IATA = "LHR"

flight_search = FlightSearch()
notification = NotificationManager()
customer_data = data_manager.get_customer_emails()
customer_emails = [row["whatIsYourEmail?"] for row in customer_data]

for destination in sheet_data:
    pprint(f"Getting flights for {destination['city']}...")
    flights = flight_search.check_flights(
        origin_city_code=ORIGIN_CITY_IATA,
        destination_city_code=destination["iataCode"],
        from_time=tomorrow,
        to_time=six_month_from_today
    )

    # print(flights)
    cheapest_flight = find_cheapest_flight(flights, return_date=six_month_from_today.strftime("%Y-%M-%D"))
    pprint(f"{destination['city']}:  USD {cheapest_flight.price}")

#========================== Show the Cheapest Flight ========================



    if cheapest_flight.price == "N/A":
        print(f"No direct flight to {destination['city']}. Looking for indirect flights...")
        stopover_flights = flight_search.check_flights(
            ORIGIN_CITY_IATA,
            destination["iataCode"],
            from_time=tomorrow,
            to_time=six_month_from_today,
            is_direct=False
        )
        cheapest_flight = find_cheapest_flight(stopover_flights, return_date=six_month_from_today.strftime("%Y-%m-%d"))
        print(f"Cheapest indirect flight price is: GBP {cheapest_flight.price}")

        # ==================== Send Notifications and Emails ====================

    if cheapest_flight.price != "N/A" and cheapest_flight.price < destination["lowestPrice"]:
        data_manager.update_lowest_price(destination["id"], cheapest_flight.price)
        # Customise the message depending on the number of stops
        if cheapest_flight.stops == 0:
            message = f"Low price alert! Only GBP {cheapest_flight.price} to fly direct " \
                      f"from {cheapest_flight.origin_airport} to {cheapest_flight.destination_airport}, " \
                      f"on {cheapest_flight.out_date} until {cheapest_flight.return_date}."
        else:
            message = f"Low price alert! Only GBP {cheapest_flight.price} to fly " \
                      f"from {cheapest_flight.origin_airport} to {cheapest_flight.destination_airport}, " \
                      f"with {cheapest_flight.stops} stop(s) " \
                      f"departing on {cheapest_flight.out_date} and returning on {cheapest_flight.return_date}."

        print(f"Check your email. Lower price flight found to {destination['city']}!")
        notification.send_email(customer_emails, message)
    
















