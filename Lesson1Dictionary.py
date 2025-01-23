#For a dictionary, the braces: {}
# Definition of the dictionnary
card_id = {"first name": "Paul",
           "last name" : "Lefebvre",
           "emission"  : 1978}
print(card_id)
# Overwriting a field of the dictionnary
card_id["first name"] = "Guillaume"
print(card_id)

# Adding a new key to the dictionnary of a new key
card_id["expiration"] = 1993
print(card_id)
# How long was the card valid for?
validity_duration = card_id["expiration"] - card_id["emission"]
print("This ID card was valid for", validity_duration, "years.")