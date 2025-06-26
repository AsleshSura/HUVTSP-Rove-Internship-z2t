import os
import csv
from datetime import datetime
from response import save_session


base_dir = os.path.dirname(os.path.abspath(__file__))
data_path = os.path.join(base_dir, "data", "routes.csv")

def load_routes():
    routes = []
    with open(data_path, "r", encoding="utf-8") as file:
        reader = csv.DictReader(file)
        for row in reader:
            route = {
                "id": row["Route ID"],
                "origin": row["Origin"],
                "destination": row["Destination"],
                "segments": row["Segments"].split(" → "),
                "airlines": row["Airlines"].split(" → "),
                "departure": row["Departure Time"],
                "arrival": row["Arrival Time"],
                "duration": row["Total Duration"],
                "price": float(row["Price"]),
                "stops": int(row["Number of Stops"])
            }
            routes.append(route)
    return routes

def filter_routes(routes, origin, destination):
    return [r for r in routes if r["origin"] == origin and r["destination"] == destination]

def separate_direct_and_layovers(routes):
    direct = [r for r in routes if r["stops"] == 0]
    layovers = [r for r in routes if r["stops"] > 0]
    return direct, layovers

def rank_by_price(routes):
    return sorted(routes, key=lambda r: r["price"])

def calculate_optimal_redemption(routes):
    return sorted(routes, key=lambda r: (r["price"], r["stops"], r["duration"]))[0]

def main():
    all_routes = load_routes()

    destinations = sorted(set((r["origin"], r["destination"]) for r in all_routes))

    while True:
        print("\nAvailable Routes:")
        for i, (origin, dest) in enumerate(destinations):
            print(f"{i+1}. {origin} → {dest}")
        print("Type 'exit' to quit.")

        choice = input("Choose a route by number: ").strip()
        if choice.lower() == "exit":
            print("Exiting routing tool.")
            break

        if not choice.isdigit() or int(choice) < 1 or int(choice) > len(destinations):
            print("Invalid choice. Please enter a valid number.")
            continue

        index = int(choice) - 1
        origin, destination = destinations[index]

        selected_routes = filter_routes(all_routes, origin, destination)
        direct, layovers = separate_direct_and_layovers(selected_routes)

        print(f"\n{origin} → {destination}: {len(direct)} direct flights, {len(layovers)} with layovers")

        all_ranked = rank_by_price(selected_routes)
        print("\nTop 5 Cheapest Options:")
        for r in all_ranked[:5]:
            print(f"{r['id']} | ${r['price']} | Stops: {r['stops']} | {r['segments']}")

        optimal = calculate_optimal_redemption(selected_routes)
        print(f"\nOptimal Redemption:")
        print(f"{optimal['id']} | ${optimal['price']} | Stops: {optimal['stops']} | Segments: {optimal['segments']}")
        save_session_summary(origin, destination, direct, layovers, all_ranked, optimal)
        





if __name__ == "__main__":
    main()
