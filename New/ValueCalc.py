#idk if i gotta import anything, Angelina cld u take care of this if imports r needed?? thxxx

#will change when i get more info as to what were acc doing lmao, asked Taryn already as to wut EXACTLY value-per-mile MEEANS loll + what she wants for the calc


#function is for value per mile for da FLIGHT stuff, based on monetary value per mile
def value_per_mile_flight(cash_value, miles, taxes_fees): #cash_value and miles are COSTS
  #change if definiton/understanding is wrong

  if miles == 0:
    return 0

  net_monetary_value = cash_value - taxes_fees

  return round( net_monetary_value/miles, 4)  #4th place good?


#Steps: (tho i lowk dfk) --> Add more info after talkin to Taryn
# create diff val calcs for flights n hotels n somehow some function for the girft cards
# make sure these functions fit in well to the later stuff?? (like reading the data what we gotta read n how n stuff)
#Any way to sample test if needed??
  
