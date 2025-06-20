import csv
import json

raw = "response.txt"
output = "data.csv"

with open(raw, "r", encoding = "utf-8") as raw_data:
    read_data = raw_data.read()
data = json.loads(read_data)

with open(output, "w", newline = "", encoding = "utf-8") as table:
    writer = csv.writer(table)
    writer.writerow(['Price', 'Airline', 'Departure Date', 'Departure Time'])

    for flight in data:
        price = flight['price']['total']
        itineraries = flight['itineraries']
        for itinerary in itineraries:
            segments = itinerary['segments']
            for segment in segments:
                airline = segment['carrierCode']
                departure_time = segment['departure']['at']
                departure_date = departure_time.split('T')[0]

                writer.writerow([price, airline, departure_date, departure_time])