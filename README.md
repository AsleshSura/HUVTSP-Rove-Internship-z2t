# Rove User Airline Miles Optimization Backend
Group Members: [Hardik Aslesh Sura](https://github.com/AsleshSura/), Devisree Putta, Adrian Ciubotaru, Angelina Stewart, Jayden Nguyen, Bret Chen, Sabrina Cui

## Project Overview
This repository contains Python scripts and web applications developed during the Rove Internship. The project is a comprehensive travel optimization tool designed to help users find artificial layovers to make travel experiences cheaper and maximize the value of their airline miles. The main focus is on flight data retrieval, parsing, and visualization using the Amadeus API, combined with static hotel data to improve the overall user experience.

### Key Features
- **Artificial Layover Detection**: Identifies strategic layovers that can significantly reduce travel costs
- **Airline Miles Optimization**: Helps users get the most value from their frequent flyer programs
- **Hotel Integration**: Includes static hotel data to enhance the travel planning experience
- **Real-time Flight Data**: Live flight information and pricing through Amadeus API integration

## Main Components

### Amadeus API Scripts
- **Amadeus/Amadeus API Request.py**: Connects to the Amadeus API to fetch flight offers for specific routes and dates, saving the raw response to `response.txt`.
- **Amadeus/Response Parsing.py**: Parses the raw API response and extracts key flight details (price, airline, departure date/time) into a CSV file for further analysis.
- **New/Amadeus Compoud.py**: Automates flight data collection over a range of dates, storing results in a CSV file for batch analysis.

### Web Applications
- **Week3/app.py**: Flask web app for visualizing flight data and redemption charts. Allows users to interactively search and view flight information using a user-friendly interface.
- **Week3_live_version/api2.py**: Provides live flight data retrieval functions using the Amadeus API, supporting dynamic queries for origin, destination, and date.

## Data Files
- **data.csv / Data.csv**: CSV files containing parsed flight data for analysis.
- **data.json**: Contains airline redemption chart data used in the web app.
- **response.txt**: Raw API response data for debugging and parsing.

## How to Use
1. **Install Dependencies**: Make sure to install required Python packages (e.g., `amadeus`, `flask`).
2. **API Keys**: Update the Amadeus API credentials in the scripts if needed.
3. **Run Scripts**:
   - To fetch and parse flight data, run the scripts in the `Amadeus` and `New` folders.
   - To launch the web app, run `Week3/app.py` using Flask.
4. **Analyze Data**: Use the generated CSV files for further analysis or visualization.

## Folder Structure
- `Amadeus/`: API request and parsing scripts.
- `New/`: Batch data collection scripts.
- `Week3/`: Web app and supporting files.
- `Week3_live_version/`: Live API integration scripts.

## License
This project is for educational and internship purposes.
