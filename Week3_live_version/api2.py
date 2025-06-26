from amadeus import Client, ResponseError

amadeus = Client(
    client_id='NAHa5Gwxsia2CSfJKod3yjdDYpCXJwMC',
    client_secret='LXwncGgeKIIiJ9mt'
)

def get_flight_data(origin, destination, departure_date):
    try:
        response = amadeus.shopping.flight_offers_search.get(
            originLocationCode=origin,
            destinationLocationCode=destination,
            departureDate=departure_date,
            adults=1,
            max=50
        )

        flights = []
        for idx, flight in enumerate(response.data, 1):
            price = float(flight["price"]["total"])
            base = float(flight["price"]["base"])
            taxes = price - base
            for itinerary in flight["itineraries"]:
                segments = itinerary["segments"]
                route = {
                    "id": f"LiveRoute-{idx}",
                    "origin": origin,
                    "destination": destination,
                    "segments": [s["departure"]["iataCode"] for s in segments] + [segments[-1]["arrival"]["iataCode"]],
                    "airlines": [s["carrierCode"] for s in segments],
                    "departure": segments[0]["departure"]["at"],
                    "arrival": segments[-1]["arrival"]["at"],
                    "duration": itinerary["duration"],
                    "price": price,
                    "base": base,
                    "taxes": taxes,
                    "stops": len(segments) - 1
                }
                flights.append(route)
        return flights

    except ResponseError as error:
        print(f"API Error: {error}")
        return []
