from api2 import get_flight_data
from response2 import save_session_summary

def parse_flights(api_data):
    routes = []
    for i, flight in enumerate(api_data):
        price = float(flight["price"]["total"])
        for itinerary in flight["itineraries"]:
            segments = itinerary["segments"]
            segment_airports = []
            segment_airlines = []
            for segment in segments:
                segment_airports.append(segment["departure"]["iataCode"])
                segment_airlines.append(segment["carrierCode"])
            segment_airports.append(segments[-1]["arrival"]["iataCode"])

            route = {
                "id": f"Route-{i+1}",
                "origin": segments[0]["departure"]["iataCode"],
                "destination": segments[-1]["arrival"]["iataCode"],
                "segments": segment_airports,
                "airlines": segment_airlines,
                "departure": segments[0]["departure"]["at"],
                "arrival": segments[-1]["arrival"]["at"],
                "duration": itinerary["duration"],
                "price": price,
                "stops": len(segments) - 1
            }
            routes.append(route)
    return routes

def separate_direct_and_layovers(routes):
    direct = [r for r in routes if r["stops"] == 0]
    layovers = [r for r in routes if r["stops"] > 0]
    return direct, layovers

def rank_by_price(routes):
    return sorted(routes, key=lambda r: r["price"])

def calculate_optimal_redemption(routes):
    return sorted(routes, key=lambda r: (r["price"], r["stops"], r["duration"]))[0]

def main():
    print("Enter your route details.")
    origin = input("Origin airport code (e.g. JFK): ").upper()
    destination = input("Destination airport code (e.g. HEL): ").upper()
    departure_date = input("Departure date (YYYY-MM-DD): ")

    api_data = get_flight_data(origin, destination, departure_date)
    if not api_data:
        print("No flights found.")
        return

    routes = parse_flights(api_data)
    direct, layovers = separate_direct_and_layovers(routes)
    all_ranked = rank_by_price(routes)
    optimal = calculate_optimal_redemption(routes)

    print(f"\n{origin} → {destination}: {len(direct)} direct flights, {len(layovers)} with layovers\n")
    print("Top 5 Cheapest Options:")
    for r in all_ranked[:5]:
        print(f"{r['id']} | ${r['price']} | Stops: {r['stops']} | {r['segments']}")

    print(f"\nOptimal Redemption:")
    print(f"{optimal['id']} | ${optimal['price']} | Stops: {optimal['stops']} | Segments: {optimal['segments']}")

    save_session_summary(origin, destination, direct, layovers, all_ranked, optimal)

if __name__ == "__main__":
    main()
