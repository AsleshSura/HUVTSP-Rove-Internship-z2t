#do i need to import anything??
#will change when i get more info as to what were acc doing lmao, asked Taryn already as to wut EXACTLY value-per-mile MEEANS loll + what she wants for the calc


#NOTE: FInish Friday Morning??!
def value_per_mile(cash_value, miles, taxes_fees): #cash_value and miles are COSTS
  #change if definiton/understanding is wrong
  if miles == 0:
    return 0
  net_monetary_value = cash_value - taxes_fees
  
  return round( net_monetary_value/miles, 4)  #4th place good?


#Steps: (tho i lowk dfk) --> Add more info after talkin to Taryn
# create diff val calcs for flights n hotels n somehow some function for the girft cards
# make sure these functions fit in well to the later stuff?? (like reading the data what we gotta read n how n stuff)
#Any way to sample test if needed??
  
#dictionary:
  #KEY: Acc Hotels: Marriott International, Hilton Worldwide, InterContinental Hotels Group, Wyndham Hotels & Resorts  VALUE: another dictionary
      #KEY2: The Diff Hotel Chains in Diff MAJOR Cities, of diff countries
          #Key2: Diff suite names 
              #KEY3: Price: Marriot Grand suite Paris price --> NUMBER (miles??)
              #KEY4: Upgrades + Value: Free break fast n stuff (Strings with certain format so detectable)

# --> Algorithm: IF there are those extra value stuff based on the string: WHAT the upgrade is, a certain percentage increase on the value per mile 

#Also maybe we can add more data and put it into a json file (idk how to import n do that stuff n if there are any extra cautions w dat sooo)
aPrice = 0
aMile = 0
#For amenities: Either include estimated extra value or string ofspecific stuff to then be read in, and the value increased based on the og price
#Price estimates in dollars
#The room types are averages per suite type, so things like location in hotel or view are not seperately factored in, the room values are "averaged"
HOTELS_INFO:
{
    "Marriott International": 
   {
     "Paris Marriott Champs Elysees":    
        {                         # $$    miles
          "Deluxe King": {"Price": [810, 31667], "bonus_through_redemption": ""}, 
          "RoomType2": {"Price": aNum, "Amenities": "",},
          "RoomType3": {"Price": aNum, "Amenities": "",},
          "Core Amenities": [],
        },
     "New York Marriott Marquis": {},
     "Wailea Beach Resort - Marriott, Maui": {},
     "The Cosmopolitan of Las Vegas": {},
     "JW Marriott Marco Island Beach Resort": {},
     "Sheraton Grand Seattle": {},
    },
  
    "Hilton Worldwide": {} 
}
