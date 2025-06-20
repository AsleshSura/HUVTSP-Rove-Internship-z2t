from amadeus import Client, ResponseError
import json

raw = "response.txt"

amadeus = Client(
    client_id = "JrpuY7vpCPQTFfGEUN306H9Y2B0R5clN",
    client_secret = "YlMXtRILoAN8ne2G"
)

try:
    response = amadeus.shopping.flight_offers_search.get(
        originLocationCode = "JFK",
        destinationLocationCode = "HEL",
        adults = 1,
        departureDate='2025-07-27')
    print(response.data)
except ResponseError as error:
    print(error)

with open(raw, "w", encoding = "utf-8") as dump:
    json.dump(response.data, dump, indent = 4)