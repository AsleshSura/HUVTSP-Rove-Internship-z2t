import os
from amadeus import Client, ResponseError
import csv


amadeus = Client(
    client_id='NAHa5Gwxsia2CSfJKod3yjdDYpCXJwMC',
    client_secret='LXwncGgeKIIiJ9mt'
)

routes = [
    ("JFK", "HEL", "2025-07-01"),
    ("JFK", "CDG", "2025-07-01"),
    ("JFK", "AMS", "2025-07-01")
]

base_dir = os.path.dirname(os.path.abspath(__file__))
data_dir = os.path.join(base_dir, "data")
output_path = os.path.join(data_dir, "routes.csv")

os.makedirs(data_dir, exist_ok=True)

with open(output_path, "w", newline="", encoding="utf-8") as file:
    writer = csv.writer(file)
    writer.writerow([
        "Route ID", "Origin", "Destination", "Segments", "Airlines",
        "Departure Time", "Arrival Time", "Total Duration", "Price", "Number of Stops"
    ])

    route_counter = 1

    for origin, destination, departure_date in routes:
        try:
            response = amadeus.shopping.flight_offers_search.get(
                originLocationCode=origin,
                destinationLocationCode=destination,
                departureDate=departure_date,
                adults=1,
                max=50
            )

            for flight in response.data:
                price = flight["price"]["total"]
                for itinerary in flight["itineraries"]:
                    segments = itinerary["segments"]
                    segment_airports = []
                    segment_airlines = []
                    for segment in segments:
                        segment_airports.append(segment["departure"]["iataCode"])
                        segment_airlines.append(segment["carrierCode"])
                    segment_airports.append(segments[-1]["arrival"]["iataCode"])

                    writer.writerow([
                        f"Route-{route_counter}",
                        origin,
                        destination,
                        " → ".join(segment_airports),
                        " → ".join(segment_airlines),
                        segments[0]["departure"]["at"],
                        segments[-1]["arrival"]["at"],
                        itinerary["duration"],
                        price,
                        len(segments) - 1
                    ])
                    route_counter += 1

        except ResponseError as error:
            print(f"API Error {origin} to {destination}: {error}")
