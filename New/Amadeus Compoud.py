from amadeus import Client, ResponseError
import json
import csv
from datetime import datetime, timedelta

raw = "response.txt"
output = "data.csv"
init = "2025-06-30"
date = datetime.strptime(init, "%Y-%m-%d")

amadeus = Client(
    client_id = "JrpuY7vpCPQTFfGEUN306H9Y2B0R5clN",
    client_secret = "YlMXtRILoAN8ne2G"
)

with open(output, "w", newline = "", encoding = "utf-8") as table:
    writer = csv.writer(table)
    writer.writerow(['Price', 'Airline', 'Departure Date', 'Departure Time'])

    for i in range(31):
        date += timedelta(days = 1)
        try:
            response = amadeus.shopping.flight_offers_search.get(
            originLocationCode = "JFK",
            destinationLocationCode = "HEL",
            adults = 1,
            departureDate = date.strftime("%Y-%m-%d"))

            for flight in response.data:
                price = flight['price']['total']
                itineraries = flight['itineraries']
                for itinerary in itineraries:
                    segments = itinerary['segments']
                    for segment in segments:
                        airline = segment['carrierCode']
                        departure_time = segment['departure']['at']
                        departure_date = departure_time.split('T')[0]

                        writer.writerow([price, airline, departure_date, departure_time])

        except ResponseError as error:
            print(error)
    
    print("Debug")