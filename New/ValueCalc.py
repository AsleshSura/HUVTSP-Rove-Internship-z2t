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
    "Hilton Hawaiian Village Waikiki Beach Resort (Honolulu, Hawaii, USA)": {
        "Tapa Collection Resort View 1 King Bed": {
            "Price": [537, 13300],
            "Bonus Through Redemption": {
                "Total": 0.13
            }
        },
        "Resort View 2 Double Beds": {
            "Price": [538, 7500],
            "Bonus Through Redemption": {
                "Total": 0.13
            }
        },
        "Rainbow Kai Lagoon View 2q Hearing Acc": {
            "Price": [734, 18700],
            "Bonus Through Redemption": {
                "Total": 0.15
            }
        },
        "Core Amenities": ["Accessible entrances", "Accessible rooms", "Accessible dining", "Accessible pool", "Braille signage", "Service animals welcome"]
    },

    "New York Hilton Midtown (Manhattan, USA)": {
        "1 King Mobility/hearing Accessible Ri-shower": {
            "Price": [419, 8000],
            "Bonus Through Redemption": {
                "Total": 0.13
            }
        },
        "2 Queen Beds Full View Floor-ceiling Window": {
            "Price": [444, 17100],
            "Bonus Through Redemption": {
                "Total": 0.15
            }
        },
        "2 Queen Beds Top Floor with City View": {
            "Price": [474, 18300],
            "Bonus Through Redemption": {
                "Total": 0.18
            }
        },
        "Core Amenities": ["Accessible entrances", "Accessible rooms", "Accessible fitness center", "Braille signage", "Assistive listening", "Service animals welcome"]
    },

    "Homewood Suites by Hilton Chicago Downtown South Loop": {
        "1 King Mobilty/hearing Access Ri Shwr Studio Ns": {
            "Price": [385, 7000],
            "Bonus Through Redemption": {
                "Total": 0.13
            }
        },
        "1 King Hearing Accessible Corner Studio": {
            "Price": [410, 18100],
            "Bonus Through Redemption": {
                "Total": 0.15
            }
        },
        "1 King Bed Studio Corner Suite": {
            "Price": [435, 19200],
            "Bonus Through Redemption": {
                "Total": 0.18
            }
        },
        "Core Amenities": ["Accessible entrances", "Accessible rooms", "Accessible pool", "Braille signage", "Service animals welcome"]
    },

    "Conrad Maldives Rangali Island": {
        "Beach Villa": {
            "Price": [737, 14000],
            "Bonus Through Redemption": {
                "Total": 0.18
            }
        },
        "Deluxe Water Villa with Pool": {
            "Price": [1136, 28400],
            "Bonus Through Redemption": {
                "Total": 0.25
            }
        },
        "3 Bedroom Beach Suite with Pool": {
            "Price": [3245, 81200],
            "Bonus Through Redemption": {
                "Total": 0.35
            }
        },
        "Core Amenities": ["Accessible fitness center", "Audible alarms", "Accessible bathrooms"]
    },

    "Hilton Aruba Caribbean Resort & Casino": {
        "Project View Bonaire/curacao Tower 2 Doubles": {
            "Price": [538, 10000],
            "Bonus Through Redemption": {
                "Total": 0.13
            }
        },
        "Partial Ocean View Aruba Tower 2 Queen Beds": {
            "Price": [634, 28500],
            "Bonus Through Redemption": {
                "Total": 0.15
            }
        },
        "Core Amenities": ["Accessible entrances", "Accessible rooms", "Accessible pool", "Braille signage", "Service animals welcome"]
    }
}
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

HYATT_HOTELS_INFO = {
    "Hyatt Regency Maui": {
        "Room, 1 King Bed with Sofa bed": {
            "Price": [830.31, 56000],
            "Redemption Value (¢/Mile)": 1.48,
            "Miles Earned": 8330,
            "Max Occupancy": 2,
            "Amenities": [
                "Coffee/tea maker", "Safety deposit box", "TV", "Telephone", "Air conditioning"
            ]
        },
        "Room, 1 King Bed with Sofa bed (Breakfast Included)": {
            "Price": [947.85, 64000],
            "Redemption Value (¢/Mile)": 1.48,
            "Miles Earned": 9510,
            "Max Occupancy": 2,
            "Amenities": [
                "Coffee/tea maker", "Safety deposit box", "TV", "Telephone", "Air conditioning"
            ]
        },
        "Room, 1 King Bed, Accessible (Shower)": {
            "Price": [830.31, 56000],
            "Redemption Value (¢/Mile)": 1.48,
            "Miles Earned": 8330,
            "Max Occupancy": 2,
            "Amenities": [
                "Coffee/tea maker", "Safety deposit box", "TV", "Telephone", "Air conditioning"
            ]
        },
        "Room, 1 King Bed, Accessible (Shower, Breakfast Included)": {
            "Price": [947.85, 64000],
            "Redemption Value (¢/Mile)": 1.48,
            "Miles Earned": 9510,
            "Max Occupancy": 2,
            "Amenities": [
                "Coffee/tea maker", "Safety deposit box", "TV", "Telephone", "Air conditioning"
            ]
        },
        "Room, 1 King Bed with Sofa bed, Partial Ocean View": {
            "Price": [866.47, 58000],
            "Redemption Value (¢/Mile)": 1.49,
            "Miles Earned": 8693,
            "Max Occupancy": 2,
            "Amenities": [
                "Coffee/tea maker", "Safety deposit box", "TV", "Telephone", "Air conditioning"
            ]
        },
        "Room, 1 King Bed with Sofa bed, Partial Ocean View (Breakfast Included)": {
            "Price": [984.36, 66000],
            "Redemption Value (¢/Mile)": 1.49,
            "Miles Earned": 9876,
            "Max Occupancy": 2,
            "Amenities": [
                "Coffee/tea maker", "Safety deposit box", "TV", "Telephone", "Air conditioning"
            ]
        },
        "Room, 1 King Bed with Sofa bed, Ocean View": {
            "Price": [878.52, 59000],
            "Redemption Value (¢/Mile)": 1.49,
            "Miles Earned": 8813,
            "Max Occupancy": 2,
            "Amenities": [
                "Coffee/tea maker", "Safety deposit box", "TV", "Telephone", "Air conditioning"
            ]
        },
        "Room, 1 King Bed with Sofa bed, Ocean View (Breakfast Included)": {
            "Price": [996.55, 67000],
            "Redemption Value (¢/Mile)": 1.49,
            "Miles Earned": 9999,
            "Max Occupancy": 2,
            "Amenities": [
                "Coffee/tea maker", "Safety deposit box", "TV", "Telephone", "Air conditioning"
            ]
        },
        "1 King Bed, Mountain View": {
            "Price": [795.63, 64000],
            "Redemption Value (¢/Mile)": 1.47,
            "Miles Earned": 9468,
            "Max Occupancy": 2,
            "Amenities": [
                "Coffee/tea maker", "Safety deposit box", "TV", "Telephone", "Air conditioning"
            ]
        },
        "1 King Bed, Mountain View (Breakfast Included)": {
            "Price": [898.08, 72000],
            "Redemption Value (¢/Mile)": 1.48,
            "Miles Earned": 10686,
            "Max Occupancy": 2,
            "Amenities": [
                "Coffee/tea maker", "Safety deposit box", "TV", "Telephone", "Air conditioning"
            ]
        },
        "ROOM, QUEEN/QUEEN, MOUNTAIN VIEW": {
            "Price": [947.48, 64000],
            "Redemption Value (¢/Mile)": 1.48,
            "Miles Earned": 9506,
            "Max Occupancy": 2,
            "Amenities": [
                "Coffee/tea maker", "Safety deposit box", "TV", "Telephone", "Air conditioning"
            ]
        },
        "ROOM, QUEEN/QUEEN, OCEAN VIEW": {
            "Price": [987.00, 67000],
            "Redemption Value (¢/Mile)": 1.47,
            "Miles Earned": 9903,
            "Max Occupancy": 2,
            "Amenities": [
                "Coffee/tea maker", "Safety deposit box", "TV", "Telephone", "Air conditioning"
            ]
        },
        "ROOM, QUEEN/QUEEN, PARTIAL OCEAN VIEW": {
            "Price": [991.02, 67000],
            "Redemption Value (¢/Mile)": 1.48,
            "Miles Earned": 9943,
            "Max Occupancy": 2,
            "Amenities": [
                "Coffee/tea maker", "Safety deposit box", "TV", "Telephone", "Air conditioning"
            ]
        },
        "Room, 1 King Bed with Sofa bed, Ocean View, Corner": {
            "Price": [1008.70, 68000],
            "Redemption Value (¢/Mile)": 1.48,
            "Miles Earned": 10120,
            "Max Occupancy": 2,
            "Amenities": [
                "Coffee/tea maker", "Safety deposit box", "TV", "Telephone", "Air conditioning"
            ]
        },
        "Room, 1 King Bed with Sofa bed, Ocean View, Corner (Breakfast Included)": {
            "Price": [1118.20, 75000],
            "Redemption Value (¢/Mile)": 1.49,
            "Miles Earned": 11219,
            "Max Occupancy": 2,
            "Amenities": [
                "Coffee/tea maker", "Safety deposit box", "TV", "Telephone", "Air conditioning"
            ]
        },
        "1 King Bed, Ocean front": {
            "Price": [863.93, 69000],
            "Redemption Value (¢/Mile)": 1.49,
            "Miles Earned": 10280,
            "Max Occupancy": 2,
            "Amenities": [
                "Coffee/tea maker", "Safety deposit box", "TV", "Telephone", "Air conditioning"
            ]
        },
        "1 King Bed, Ocean front (Breakfast Included)": {
            "Price": [966.35, 77000],
            "Redemption Value (¢/Mile)": 1.49,
            "Miles Earned": 11498,
            "Max Occupancy": 2,
            "Amenities": [
                "Coffee/tea maker", "Safety deposit box", "TV", "Telephone", "Air conditioning"
            ]
        },
        "Club Room, 1 King Bed with Sofa bed, Partial Ocean View (Club Access)": {
            "Price": [1144.99, 77000],
            "Redemption Value (¢/Mile)": 1.49,
            "Miles Earned": 11488,
            "Max Occupancy": 2,
            "Amenities": [
                "Coffee/tea maker", "Safety deposit box", "TV", "Telephone", "Air conditioning"
            ]
        },
        "Club Room, 1 King Bed with Sofa bed, Partial Ocean View (Club Access, Breakfast Included)": {
            "Price": [1254.50, 84000],
            "Redemption Value (¢/Mile)": 1.49,
            "Miles Earned": 12588,
            "Max Occupancy": 2,
            "Amenities": [
                "Coffee/tea maker", "Safety deposit box", "TV", "Telephone", "Air conditioning"
            ]
        },
        "Club Room, 1 King Bed with Sofa bed, Oceanfront (Club Access)": {
            "Price": [1193.67, 80000],
            "Redemption Value (¢/Mile)": 1.49,
            "Miles Earned": 11976,
            "Max Occupancy": 2,
            "Amenities": [
                "Coffee/tea maker", "Safety deposit box", "TV", "Telephone", "Air conditioning"
            ]
        },
        "Club Room, 1 King Bed with Sofa bed, Oceanfront (Club Access, Breakfast Included)": {
            "Price": [1303.18, 88000],
            "Redemption Value (¢/Mile)": 1.48,
            "Miles Earned": 13075,
            "Max Occupancy": 2,
            "Amenities": [
                "Coffee/tea maker", "Safety deposit box", "TV", "Telephone", "Air conditioning"
            ]
        },
        "Suite, Oceanfront": {
            "Price": [2804.68, 188000],
            "Redemption Value (¢/Mile)": 1.49,
            "Miles Earned": 28140,
            "Max Occupancy": 2,
            "Amenities": [
                "Coffee/tea maker", "Safety deposit box", "TV", "Telephone", "Air conditioning"
            ]
        },
        "Suite, Oceanfront (Breakfast Included)": {
            "Price": [2914.18, 195000],
            "Redemption Value (¢/Mile)": 1.49,
            "Miles Earned": 29239,
            "Max Occupancy": 2,
            "Amenities": [
                "Coffee/tea maker", "Safety deposit box", "TV", "Telephone", "Air conditioning"
            ]
        },
        "Deluxe Ocean Suite": {
            "Price": [2726.09, 217000],
            "Redemption Value (¢/Mile)": 1.49,
            "Miles Earned": 32440,
            "Max Occupancy": 2,
            "Amenities": [
                "Coffee/tea maker", "Safety deposit box", "TV", "Telephone", "Air conditioning"
            ]
        },
        "Deluxe Ocean Suite (Breakfast Included)": {
            "Price": [2828.53, 225000],
            "Redemption Value (¢/Mile)": 1.49,
            "Miles Earned": 33659,
            "Max Occupancy": 2,
            "Amenities": [
                "Coffee/tea maker", "Safety deposit box", "TV", "Telephone", "Air conditioning"
            ]
        },
        "Core Amenities": [
            "Coffee/tea maker", "Safety deposit box", "TV", "Telephone", "Air conditioning"
        ]
    },
    "Hyatt Regency Bali": {
        "1 King Bed Premium": {
            "Price": [356.32, 24000],
            "Redemption Value (¢/Mile)": 1.48,
            "Miles Earned": 3576,
            "Max Occupancy": 2,
            "Amenities": [
                "Coffee/tea maker", "Minibar", "Safety deposit box", "TV", "Telephone"
            ]
        },
        "Core Amenities": [
            "Coffee/tea maker", "Minibar", "Safety deposit box", "TV", "Telephone"
        ]
    },
    "Park Hyatt New York": {
        "1 King Bed": {
            "Price": [1108.14, 75000],
            "Redemption Value (¢/Mile)": 1.48,
            "Miles Earned": 11118,
            "Max Occupancy": 2,
            "Amenities": [
                "Coffee/tea maker", "Minibar", "Safety deposit box", "TV", "Telephone"
            ]
        },
        "1 King Bed (Breakfast Included)": {
            "Price": [1246.03, 84000],
            "Redemption Value (¢/Mile)": 1.48,
            "Miles Earned": 12501,
            "Max Occupancy": 2,
            "Amenities": [
                "Coffee/tea maker", "Minibar", "Safety deposit box", "TV", "Telephone"
            ]
        },
        "1 King Bed With Ada Shower": {
            "Price": [1108.14, 75000],
            "Redemption Value (¢/Mile)": 1.48,
            "Miles Earned": 11118,
            "Max Occupancy": 2,
            "Amenities": [
                "Coffee/tea maker", "Minibar", "Safety deposit box", "TV", "Telephone"
            ]
        },
        "1 King Bed With Ada Shower (Breakfast Included)": {
            "Price": [1246.03, 84000],
            "Redemption Value (¢/Mile)": 1.48,
            "Miles Earned": 12501,
            "Max Occupancy": 2,
            "Amenities": [
                "Coffee/tea maker", "Minibar", "Safety deposit box", "TV", "Telephone"
            ]
        },
        "2 Double Beds With City View": {
            "Price": [1438.01, 97000],
            "Redemption Value (¢/Mile)": 1.48,
            "Miles Earned": 14428,
            "Max Occupancy": 2,
            "Amenities": [
                "Coffee/tea maker", "Minibar", "Safety deposit box", "TV", "Telephone"
            ]
        },
        "2 Double Beds With City View (Breakfast Included)": {
            "Price": [1575.90, 106000],
            "Redemption Value (¢/Mile)": 1.49,
            "Miles Earned": 15811,
            "Max Occupancy": 2,
            "Amenities": [
                "Coffee/tea maker", "Minibar", "Safety deposit box", "TV", "Telephone"
            ]
        },
        "1 King Bed With City View": {
            "Price": [1438.01, 97000],
            "Redemption Value (¢/Mile)": 1.48,
            "Miles Earned": 14428,
            "Max Occupancy": 2,
            "Amenities": [
                "Coffee/tea maker", "Minibar", "Safety deposit box", "TV", "Telephone"
            ]
        },
        "1 King Bed With City View (Breakfast Included)": {
            "Price": [1575.90, 106000],
            "Redemption Value (¢/Mile)": 1.49,
            "Miles Earned": 15811,
            "Max Occupancy": 2,
            "Amenities": [
                "Coffee/tea maker", "Minibar", "Safety deposit box", "TV", "Telephone"
            ]
        },
        "2 Double Beds Studio Suite": {
            "Price": [1491.05, 100000],
            "Redemption Value (¢/Mile)": 1.49,
            "Miles Earned": 14960,
            "Max Occupancy": 2,
            "Amenities": [
                "Coffee/tea maker", "Minibar", "Safety deposit box", "TV", "Telephone"
            ]
        },
        "2 Double Beds Studio Suite (Breakfast Included)": {
            "Price": [1628.94, 109000],
            "Redemption Value (¢/Mile)": 1.49,
            "Miles Earned": 16343,
            "Max Occupancy": 2,
            "Amenities": [
                "Coffee/tea maker", "Minibar", "Safety deposit box", "TV", "Telephone"
            ]
        },
        "1 Bedroom City View Suite": {
            "Price": [1654.40, 111000],
            "Redemption Value (¢/Mile)": 1.49,
            "Miles Earned": 16599,
            "Max Occupancy": 2,
            "Amenities": [
                "Coffee/tea maker", "Minibar", "Safety deposit box", "TV", "Telephone"
            ]
        },
        "1 Bedroom City View Suite (Breakfast Included)": {
            "Price": [1792.29, 120000],
            "Redemption Value (¢/Mile)": 1.49,
            "Miles Earned": 17983,
            "Max Occupancy": 2,
            "Amenities": [
                "Coffee/tea maker", "Minibar", "Safety deposit box", "TV", "Telephone"
            ]
        },
        "1 Bedroom Sleep Suite By Bryte": {
            "Price": [1737.14, 117000],
            "Redemption Value (¢/Mile)": 1.48,
            "Miles Earned": 17430,
            "Max Occupancy": 2,
            "Amenities": [
                "Coffee/tea maker", "Minibar", "Safety deposit box", "TV", "Telephone"
            ]
        },
        "1 Bedroom Sleep Suite By Bryte (Breakfast Included)": {
            "Price": [1875.03, 126000],
            "Redemption Value (¢/Mile)": 1.49,
            "Miles Earned": 18813,
            "Max Occupancy": 2,
            "Amenities": [
                "Coffee/tea maker", "Minibar", "Safety deposit box", "TV", "Telephone"
            ]
        },
        "Suite 1 Bedroom City View 1 King Bed": {
            "Price": [1938.97, 130000],
            "Redemption Value (¢/Mile)": 1.49,
            "Miles Earned": 19454,
            "Max Occupancy": 2,
            "Amenities": [
                "Coffee/tea maker", "Minibar", "Safety deposit box", "TV", "Telephone"
            ]
        },
        "1 Bedroom Terrace Suite": {
            "Price": [2609.04, 175000],
            "Redemption Value (¢/Mile)": 1.49,
            "Miles Earned": 26177,
            "Max Occupancy": 2,
            "Amenities": [
                "Coffee/tea maker", "Minibar", "Safety deposit box", "TV", "Telephone"
            ]
        },
        "1 Bedroom Terrace Suite (Breakfast Included)": {
            "Price": [2746.92, 184000],
            "Redemption Value (¢/Mile)": 1.49,
            "Miles Earned": 27560,
            "Max Occupancy": 2,
            "Amenities": [
                "Coffee/tea maker", "Minibar", "Safety deposit box", "TV", "Telephone"
            ]
        },
        "Suite 1 Bedroom Terrace 1 King Bed": {
            "Price": [3059.20, 205000],
            "Redemption Value (¢/Mile)": 1.49,
            "Miles Earned": 30694,
            "Max Occupancy": 2,
            "Amenities": [
                "Coffee/tea maker", "Minibar", "TV", "Telephone", "Air conditioning"
            ]
        },
        "Core Amenities": [
            "Coffee/tea maker", "Minibar", "Safety deposit box", "TV", "Telephone"
        ]
    },
    "Park Hyatt Milano": {
        "Deluxe Room (Park)": {
            "Price": [1537.47, 111000],
            "Redemption Value (¢/Mile)": 1.48,
            "Miles Earned": 16514,
            "Max Occupancy": 2,
            "Amenities": [
                "Coffee/tea maker", "Minibar", "Safety deposit box", "TV", "Air conditioning"
            ]
        },
        "Park Junior Suite": {
            "Price": [2408.23, 162000],
            "Redemption Value (¢/Mile)": 1.49,
            "Miles Earned": 24163,
            "Max Occupancy": 2,
            "Amenities": [
                "Coffee/tea maker", "Minibar", "Safety deposit box", "TV", "Air conditioning"
            ]
        },
        "Park Junior Suite (Breakfast Included)": {
            "Price": [2527.63, 170000],
            "Redemption Value (¢/Mile)": 1.49,
            "Miles Earned": 25360,
            "Max Occupancy": 2,
            "Amenities": [
                "Coffee/tea maker", "Minibar", "Safety deposit box", "TV", "Air conditioning"
            ]
        },
        "Prestige Suite": {
            "Price": [3607.00, 242000],
            "Redemption Value (¢/Mile)": 1.49,
            "Miles Earned": 36190,
            "Max Occupancy": 2,
            "Amenities": [
                "Coffee/tea maker", "Minibar", "Safety deposit box", "TV", "Air conditioning"
            ]
        },
        "Prestige Suite (Breakfast Included)": {
            "Price": [3726.40, 250000],
            "Redemption Value (¢/Mile)": 1.49,
            "Miles Earned": 37388,
            "Max Occupancy": 2,
            "Amenities": [
                "Coffee/tea maker", "Minibar", "Safety deposit box", "TV", "Air conditioning"
            ]
        },
        "Terrace Suite": {
            "Price": [3845.80, 258000],
            "Redemption Value (¢/Mile)": 1.49,
            "Miles Earned": 38586,
            "Max Occupancy": 2,
            "Amenities": [
                "Coffee/tea maker", "Minibar", "Safety deposit box", "TV", "Air conditioning"
            ]
        },
        "Terrace Suite (Breakfast Included)": {
            "Price": [3965.20, 266000],
            "Redemption Value (¢/Mile)": 1.49,
            "Miles Earned": 39784,
            "Max Occupancy": 2,
            "Amenities": [
                "Coffee/tea maker", "Minibar", "Safety deposit box", "TV", "Air conditioning"
            ]
        },
        "Core Amenities": [
            "Coffee/tea maker", "Minibar", "Safety deposit box", "TV", "Air conditioning"
        ]
    },
    "Hyatt Regency London Blackfriars": {
        "Regency Suite High Street View": {
            "Price": [1189.82, 80000],
            "Redemption Value (¢/Mile)": 1.49,
            "Miles Earned": 11940,
            "Max Occupancy": 2,
            "Amenities": [
                "Coffee/tea maker", "Minibar", "Safety deposit box", "Telephone", "Air conditioning"
            ]
        },
        "Executive Suite": {
            "Price": [1293.26, 87000],
            "Redemption Value (¢/Mile)": 1.49,
            "Miles Earned": 12976,
            "Max Occupancy": 2,
            "Amenities": [
                "Coffee/tea maker", "Minibar", "Safety deposit box", "Telephone", "Air conditioning"
            ]
        },
        "Executive Suite (Room Only, Higher Rate)": {
            "Price": [1432.73, 96000],
            "Redemption Value (¢/Mile)": 1.49,
            "Miles Earned": 14376,
            "Max Occupancy": 2,
            "Amenities": [
                "Coffee/tea maker", "Minibar", "Safety deposit box", "Telephone", "Air conditioning"
            ]
        },
        "SUITE EXECUTIVE CITY VIEW": {
            "Price": [1392.25, 94000],
            "Redemption Value (¢/Mile)": 1.48,
            "Miles Earned": 13969,
            "Max Occupancy": 2,
            "Amenities": [
                "Coffee/tea maker", "Minibar", "Safety deposit box", "Telephone", "Air conditioning"
            ]
        },
        "Core Amenities": [
            "Coffee/tea maker", "Minibar", "Safety deposit box", "Telephone", "Air conditioning"
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

