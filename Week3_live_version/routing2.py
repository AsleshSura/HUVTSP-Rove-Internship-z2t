from api2 import get_flight_data
from response2 import save_session_summary

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

    routes = api_data
    direct, layovers = separate_direct_and_layovers(routes)
    all_ranked = rank_by_price(routes)
    optimal = calculate_optimal_redemption(routes)

    print(f"\n{origin} → {destination}: {len(direct)} direct flights, {len(layovers)} with layovers\n")
    print("Top 5 Cheapest Options:")
    for r in all_ranked[:5]:
        print(f"{r['id']} | ${r['price']} (Base: ${r['base']} + Taxes/Fees: ${r['taxes']}) | Stops: {r['stops']} | {r['segments']}")

    print(f"\nOptimal Redemption:")
    print(f"{optimal['id']} | ${optimal['price']} (Base: ${optimal['base']} + Taxes/Fees: ${optimal['taxes']}) | Stops: {optimal['stops']} | Segments: {optimal['segments']}")

    save_session_summary(origin, destination, direct, layovers, all_ranked, optimal)

if __name__ == "__main__":
    main()
