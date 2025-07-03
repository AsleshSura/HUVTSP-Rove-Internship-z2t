#do i need to import anything??


#NOTE: We were unable to find the exact number of miles earned and redeemed for gift cards. Plan to go to office hours and will update this soon.
def value_per_mile(cash_value, miles, taxes_fees): #cash_value and miles are COSTS
  if miles == 0:
    return 0
  net_monetary_value = (cash_value - taxes_fees)
  
  return round( net_monetary_value/miles, 4)  #4th place good?


 
#dictionary format:
  #KEY: Acc Hotels: Marriott International, Hilton Worldwide, InterContinental Hotels Group, Wyndham Hotels & Resorts  VALUE: another dictionary
      #KEY2: The Diff Hotel Chains in Diff MAJOR Cities, of diff countries
          #Key2: Diff suite names 
              #KEY3: Price: Marriot Grand suite Paris price --> NUMBER (miles??)
              #KEY4: Upgrades + Value: Free break fast n stuff (Strings with certain format so detectable)


#Also maybe we can add more data and put it into a json file (idk how to import n do that stuff n if there are any extra cautions w dat sooo)

#IMPORTANT: The "bonuses" are "extra" things that you would get if you pay with miles, and since you get more "features" we must factor this into the value per mile calculation

#Price estimates in dollars
#The room types are averages per suite type, so things like location in hotel or view are not seperately factored in, the room values are "averaged"

HOTELS_INFO = {
    "Marriott International": { #NOTE: Rooms can be redeemed through points only, BUT miles can be converted to points
        "Paris Marriott Champs Elysees": {
            "Deluxe King": {
                "Price": [810, 31667],
                "Bonus Through Redemption": {
                    "Total": 0
                }
            },
            "Champs-Elysees Signature Suite": {
                "Price": [1161.5, 84500],
                "Bonus Through Redemption": {
                    "Possible Upgrade": 0.05,
                    "Balcony": 0.05,
                    "View": 0.1,
                    "Breakfast": 0.03,
                    "Nonstrict Time": 0.03,
                    "Total": 0.31
                }
            },
            "Core Amenities": ["Gym", "Housekeeping", "Business Center", "Evening Turndown Service"]
        },
        "New York Marriott Marquis": {
            "Deluxe (Guest room, 2 Double)": {
                "Price": [484, 26000],
                "Bonus Through Redemption": {
                    "Breakfast": 0.03,
                    "Nonstrict Time": 0.03,
                    "Total": 0.13
                }
            },
            "Premier Large Guest room (1 King, Sofa bed, Corner room)": {
                "Price": [579, 36000],
                "Bonus Through Redemption": {
                    "Breakfast": 0.03,
                    "Nonstrict Time": 0.03,
                    "Total": 0.13
                }
            },
            "Executive Suite (M Club lounge access, 1 Bedroom Larger Suite, 1 King, Sofa bed)": {
                "Price": [1218, 86000],
                "Bonus Through Redemption": {
                    "Breakfast": 0.3,
                    "Nonstrict Time": 0.03,
                    "Lounge Access": 0.08,
                    "Possible Upgrade": 0.05,
                    "Total": 0.26
                }
            },
            "Core Amenities": ["Gym", "Business Center"]
        },
        "Wailea Beach Resort - Marriott, Maui": {
            "Garden View King (Guest room, 1 King, Sofa bed, Balcony)": {
                "Price": [658, 29334],
                "Bonus Through Redemption": {
                    "Breakfast": 0.03,
                    "Late Checkout": 0.015,
                    "Total": 0.215
                }
            },
            "Junior Suite (1 King, Balcony)": {
                "Price": [849, 44667],
                "Bonus Through Redemption": {
                    "Breakfast": 0.03,
                    "Late Checkout": 0.015,
                    "Balcony": 0.05,
                    "Possible Upgrade": 0.05,
                    "Total": 0.215
                }
            },
            "Ocean Suite (1 Bedroom Suite, 1 King, Sofa bed, Ocean view, Balcony)": {
                "Price": [1241, 76000],
                "Bonus Through Redemption": {
                    "Possible Upgrade": 0.05,
                    "Breakfast": 0.03,
                    "Balcony": 0.05,
                    "View": 0.1,
                    "Late Checkout": 0.015,
                    "Total": 0.315
                }
            },
            "Core Amenities": ["Gym", "Housekeeping", "Business Center", "Sundry/Convenience Store"]
        },
        "The Cosmopolitan of Las Vegas": {
            "City Room (Guest room, 2 Queen)": {
                "Price": [425, 24000],
                "Bonus Through Redemption": {
                    "Breakfast": 0.03,
                    "Late Checkout": 0.015,
                    "Total": 0.045
                }
            },
            "Terrace Studio (Guest room, 1 King)": {
                "Price": [475, 25667],
                "Bonus Through Redemption": {
                    "Possible Upgrade": 0.05,
                    "Breakfast": 0.03,
                    "Late Checkout": 0.015,
                    "Total": 0.095
                }
            },
            "Terrace Suite (Guest room, 1 King, Fountain view)": {
                "Price": [565, 30667],
                "Bonus Through Redemption": {
                    "Possible Upgrade": 0.05,
                    "Breakfast": 0.03,
                    "Late Checkout": 0.015,
                    "View": 0.1,
                    "Total": 0.195
                }
            },
            "Core Amenities": ["Dog Friendly w/ Fee", "Gym", "Housekeeping", "Business Center", "Sundry/Convenience Store"]
        },
        "JW Marriott Marco Island Beach Resort": {
            "Tropical View (Guest room, 2 Queen, Balcony)": {
                "Price": [515, 24834],
                "Bonus Through Redemption": {
                    "Breakfast": 0.03,
                    "Late Checkout": 0.015,
                    "Balcony": 0.05,
                    "Total": 0.095
                }
            },
            "Tropical View, Guest room, 1 King, Balcony": {
                "Price": [515, 24834],
                "Bonus Through Redemption": {
                    "Breakfast": 0.03,
                    "Late Checkout": 0.015,
                    "Balcony": 0.05,
                    "Total": 0.095
                }
            },
            "Pool & Gulf View, Guest room, 2 Queen, Balcony": {
                "Price": [539, 28500],
                "Bonus Through Redemption": {
                    "Breakfast": 0.03,
                    "Late Checkout": 0.015,
                    "Total": 0.0415
                }
            },
            "Core Amenities": ["Gym", "Business Center", "Sundry/Convenience Store"]
        },
        "Sheraton Grand Seattle": {
            "Guest Room (2 Double)": {
                "Price": [252, 16000],
                "Bonus Through Redemption": {
                    "Breakfast": 0.03,
                    "Late Checkout": 0.015,
                    "Total": 0.0415
                }
            },
            "Deluxe Guest Room (2 Double, City view, High floor)": {
                "Price": [274, 17667],
                "Bonus Through Redemption": {
                    "Breakfast": 0.03,
                    "Late Checkout": 0.015,
                    "Total": 0.0415
                }
            },
            "Premium Large Guest Room (1 King)": {
                "Price": [297, 19334],
                "Bonus Through Redemption": {
                    "Possible Upgrade": 0.05,
                    "Breakfast": 0.03,
                    "Late Checkout": 0.015,
                    "Total": 0.0915
                }
            },
            "Core Amenities": ["Dog Friendly", "Gym", "Housekeeping", "Business Center", "Sundry/Convenience Store", "Evening Turndown Service"]
        }
    },
    "Hilton Worldwide": {
      
    },
    "Hiltotn Worldwide": {},
    "Hilrton Worldwide": {},
    "Hilfton Worldwide": {},
    "Hiltoyn Worldwide": {},
}

RITZ_CARLTON_INFO = {
    "Dallas Irving Ritz Carlton": {
        "Deluxe Room, 1 King Bed, Balcony, Tower (Mobility Accessible, Roll-in Shower)": {
            "Price": [509.66, 35000],
            "Redemption Value (¢/Mile)": 1.46,
            "Miles Earned": 5113,
            "Max Occupancy": 2,
            "Amenities": [
                "Coffee/tea maker", "Safety deposit box", "TV", "Telephone", "Air conditioning",
            ]
        },
        "Villa, 1 King Bed, Patio, Poolside (View)": {
            "Price": [653.87, 49000],
            "Redemption Value (¢/Mile)": 1.47,
            "Miles Earned": 7250,
            "Max Occupancy": 2,
            "Amenities": [
                "Coffee/tea maker", "Safety deposit box", "TV", "Telephone", "Air conditioning",
            ]
        },
        "Executive Suite, 1 King Bed, Non Smoking, Golf View (Balcony)": {
            "Price": [692.39, 52000],
            "Redemption Value (¢/Mile)": 1.47,
            "Miles Earned": 7678,
            "Max Occupancy": 2,
            "Amenities": [
                "Coffee/tea maker", "Safety deposit box", "TV", "Telephone", "Air conditioning",
            ]
        },
        "Core Amenities": [
            "Coffee/tea maker", "Safety deposit box", "TV", "Telephone", "Air conditioning"
        ]
    },
    "London Ritz Carlton": {
        "Executive Suite, 1 Bedroom": {
            "Price": [7261.87, 512000],
            "Redemption Value (¢/Mile)": 1.42,
            "Miles Earned": 47530,
            "Max Occupancy": 2,
            "Amenities": [
                "Shower", "Safety deposit box", "Telephone", "Air conditioning", "Hair dryer",
            ]
        },
        "Executive Suite, 1 Bedroom (Breakfast Included)": {
            "Price": [7391.55, 521000],
            "Redemption Value (¢/Mile)": 1.42,
            "Miles Earned": 48378,
            "Max Occupancy": 2,
            "Amenities": [
                "Shower", "Safety deposit box", "Telephone", "Air conditioning", "Hair dryer",
            ]
        },
        "Core Amenities": [
            "Shower", "Safety deposit box", "Telephone", "Air conditioning", "Hair dryer"
        ]
    },
    "New York Ritz Carlton": {
        "Superior Room, 1 King Bed, Non Smoking": {
            "Price": [887.41, 60000],
            "Redemption Value (¢/Mile)": 1.48,
            "Miles Earned": 8903,
            "Max Occupancy": 2,
            "Amenities": [
                "Minibar", "Shower", "Safety deposit box", "TV", "Telephone",
            ]
        },
        "Room, 1 King Bed, Non Smoking, Park View": {
            "Price": [1109.29, 75000],
            "Redemption Value (¢/Mile)": 1.48,
            "Miles Earned": 11129,
            "Max Occupancy": 2,
            "Amenities": [
                "Minibar", "Shower", "Safety deposit box", "TV", "Telephone",
            ]
        },
        "Deluxe 1 King Bed, Interior View": {
            "Price": [1531.88, 103000],
            "Redemption Value (¢/Mile)": 1.49,
            "Miles Earned": 15370,
            "Max Occupancy": 2,
            "Amenities": [
                "Minibar", "Shower", "Safety deposit box", "TV", "Telephone",
            ]
        },
        "Avenue View, 1 King Bed, Mobility Accessible, Tub": {
            "Price": [1609.12, 108000],
            "Redemption Value (¢/Mile)": 1.49,
            "Miles Earned": 16144,
            "Max Occupancy": 2,
            "Amenities": [
                "Minibar", "Safety deposit box", "TV", "Telephone", "Air conditioning",
            ]
        },
        "1 King Bed, Avenue View": {
            "Price": [1636.77, 110000],
            "Redemption Value (¢/Mile)": 1.49,
            "Miles Earned": 16422,
            "Max Occupancy": 2,
            "Amenities": [
                "Minibar", "Shower", "Safety deposit box", "TV", "Telephone",
            ]
        },
        "Deluxe 2 Double Beds, Interior View": {
            "Price": [1702.35, 114000],
            "Redemption Value (¢/Mile)": 1.49,
            "Miles Earned": 17079,
            "Max Occupancy": 2,
            "Amenities": [
                "Minibar", "Shower", "Safety deposit box", "TV", "Telephone",
            ]
        },
        "Grand Room, 1 King Bed, Non Smoking, Park View": {
            "Price": [1714.47, 115000],
            "Redemption Value (¢/Mile)": 1.49,
            "Miles Earned": 17202,
            "Max Occupancy": 2,
            "Amenities": [
                "Minibar", "Shower", "Safety deposit box", "TV", "Telephone",
            ]
        },
        "Suite, 1 Bedroom, Non Smoking, Park View": {
            "Price": [2785.80, 187000],
            "Redemption Value (¢/Mile)": 1.49,
            "Miles Earned": 27950,
            "Max Occupancy": 2,
            "Amenities": [
                "Minibar", "Shower", "Safety deposit box", "TV", "Telephone",
            ]
        },
        "Suite, Avenue View": {
            "Price": [2889.07, 194000],
            "Redemption Value (¢/Mile)": 1.49,
            "Miles Earned": 28987,
            "Max Occupancy": 2,
            "Amenities": [
                "Minibar", "Shower", "Safety deposit box", "TV", "Telephone",
            ]
        },
        "Grand Suite, 1 Bedroom, Non Smoking, Park View": {
            "Price": [3471.66, 233000],
            "Redemption Value (¢/Mile)": 1.49,
            "Miles Earned": 34833,
            "Max Occupancy": 2,
            "Amenities": [
                "Minibar", "Shower", "Safety deposit box", "TV", "Telephone",
            ]
        },
        "Premier Suite, 1 Bedroom, Non Smoking, Park View": {
            "Price": [4238.22, 284000],
            "Redemption Value (¢/Mile)": 1.49,
            "Miles Earned": 42523,
            "Max Occupancy": 2,
            "Amenities": [
                "Minibar", "Shower", "Safety deposit box", "TV", "Telephone",
            ]
        },
        "Core Amenities": [
            "Minibar", "Shower", "Safety deposit box", "TV", "Telephone"
        ]
    },
    "Bali Ritz Carlton": {
        "Suite, 1 Bedroom, Non Smoking, Resort View (Balcony)": {
            "Price": [1868.86, 126000],
            "Redemption Value (¢/Mile)": 1.48,
            "Miles Earned": 18750,
            "Max Occupancy": 2,
            "Amenities": [
                "Coffee/tea maker", "Minibar", "Shower", "Safety deposit box", "TV",
            ]
        },
        "Suite 1 Bedroom Non Smoking Resort View (Balcony) 1 King Bed": {
            "Price": [2006.80, 135000],
            "Redemption Value (¢/Mile)": 1.49,
            "Miles Earned": 20135,
            "Max Occupancy": 2,
            "Amenities": [
                "Coffee/tea maker", "Minibar", "Shower", "Safety deposit box", "TV",
            ]
        },
        "Ubud Pool Villa 1 Bedroom Villa 1 King Ubud View Private Pool": {
            "Price": [2909.33, 195000],
            "Redemption Value (¢/Mile)": 1.49,
            "Miles Earned": 29190,
            "Max Occupancy": 2,
            "Amenities": [
                "Coffee/tea maker", "Minibar", "Shower", "Safety deposit box", "TV",
            ]
        },
        "Riverfront Pool Villa 1 Bedroom Villa 1 King Ayung River view Private pool": {
            "Price": [3182.08, 213000],
            "Redemption Value (¢/Mile)": 1.49,
            "Miles Earned": 31927,
            "Max Occupancy": 2,
            "Amenities": [
                "Coffee/tea maker", "Minibar", "Shower", "Safety deposit box", "TV",
            ]
        },
        "Reserve Pool Villa 2 Bedroom Villa Bedroom 1: 1 King Bedroom 2: 2 Queen Ayung River View": {
            "Price": [7273.33, 487000],
            "Redemption Value (¢/Mile)": 1.49,
            "Miles Earned": 72976,
            "Max Occupancy": 2,
            "Amenities": [
                "Coffee/tea maker", "Minibar", "Shower", "Safety deposit box", "TV",
            ]
        },
        "Core Amenities": [
            "Coffee/tea maker", "Minibar", "Shower", "Safety deposit box", "TV"
        ]
    },
    "Maui Ritz-Carlton": {
        "Deluxe Room, 1 King Bed, Lanai, Resort View": {
            "Price": [734.83, 50000],
            "Redemption Value (¢/Mile)": 1.47,
            "Miles Earned": 7372,
            "Max Occupancy": 2,
            "Amenities": [
                "Shower", "Safety deposit box", "TV", "Telephone", "Air conditioning",
            ]
        },
        "1 Bedroom Suite, 1 King Bed and Sofa Bed, Garden View": {
            "Price": [1205.74, 81000],
            "Redemption Value (¢/Mile)": 1.49,
            "Miles Earned": 12097,
            "Max Occupancy": 2,
            "Amenities": [
                "Shower", "Safety deposit box", "TV", "Telephone", "Air conditioning",
            ]
        },
        "1 Bedroom Suite, 1 King Bed and Sofa Bed, Ocean View": {
            "Price": [1279.71, 86000],
            "Redemption Value (¢/Mile)": 1.49,
            "Miles Earned": 12840,
            "Max Occupancy": 2,
            "Amenities": [
                "Shower", "Safety deposit box", "TV", "Telephone", "Air conditioning",
            ]
        },
        "Suite, 2 Bedrooms, Non Smoking, Garden View": {
            "Price": [2195.10, 147000],
            "Redemption Value (¢/Mile)": 1.49,
            "Miles Earned": 22024,
            "Max Occupancy": 2,
            "Amenities": [
                "Shower", "Safety deposit box", "TV", "Telephone", "Air conditioning",
            ]
        },
        "Core Amenities": [
            "Shower", "Safety deposit box", "TV", "Telephone", "Air conditioning"
        ]
    }
}


#Keys and Value categories
#Bonuses: Possible Upgrade = 0.05   Late Checkout = 0.015   Balcony = 0.05    View = 0.1    Breakfast = 0.03    Nonstrict Time =  0.03 (Early check in / Late Checkout)   Lounge Access: 0.08  
#Hotel Wide Amenities: Gym    Housekeeping   Business Center   Evening Turndown Service     Sundry/Convenience Store    Dog Friendly w/ Fee

#CALCULATOR
#Calculate value per mile for the hotel specifically\y
def hotel_vpm_calc(taxes_fees, chain, hotel_name, room_name):
  bonus_value = HOTELS_INFO[chain][hotel_name][room_name]["Bonus Through Redemption"]["Total"]
  cash_value = HOTELS_INFO[chain][hotel_name][room_name]["Price"][0]
  miles = HOTELS_INFO[chain][hotel_name][room_name]["Price"][1]

#fees and taxes???  
  cash_value = cash_value*(1+bonus_value)
  return value_per_mile(cash_value, miles, taxes_fees)

