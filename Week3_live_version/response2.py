import os
from datetime import datetime

def save_session_summary(origin, destination, direct, layovers, top_routes, optimal):
    base_dir = os.path.dirname(os.path.abspath(__file__))
    response_dir = os.path.join(base_dir, "response2")
    os.makedirs(response_dir, exist_ok=True)

    timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    filename = f"response_{timestamp}.txt"
    response_file = os.path.join(response_dir, filename)

    with open(response_file, "w", encoding="utf-8") as f:
        f.write(f"Route Selected: {origin} → {destination}\n")
        f.write(f"Total Direct Flights: {len(direct)}\n")
        f.write(f"Total Layover Flights: {len(layovers)}\n\n")

        f.write("Top 5 Cheapest Options:\n")
        for r in top_routes[:5]:
            f.write(f"{r['id']} | ${r['price']} | Stops: {r['stops']} | {r['segments']}\n")

        f.write("\nOptimal Redemption:\n")
        f.write(f"{optimal['id']} | ${optimal['price']} | Stops: {optimal['stops']} | Segments: {optimal['segments']}\n")

    print(f"Session saved to: {filename}")
