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

