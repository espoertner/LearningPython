#As New Media aquired Gannett I thought it'd be fun to suggest a new name.
#New Media is more commonly known as GateHouse and Gannett as USA Today.
#This program randomly generates a name from synonyms of "Gate", "House", "USA", and "Today"
import random
gate = ["Gate", "Portal", "Door", "Entrance", "Doorway", "Exit", "Fence", "Port", "Opening", "Conduit", "Turnstile", "Egress", "Passage"]
house = ["House", "Shelter", "Apartment", "Home", "Building", "Condo", "Dwelling", "Masion", "Residence", "Shack", "Abode", "Crib", "Shanty"]
usa = ["USA", "America", "New World", "US of A", "the States", "Nation", "Republic", "Country", "Homeland", "Land of Liberty", "Land of the Free", "Land of Opportunity"]
today = ["Today", "Currently", "Current", "Fresh", "Instantly", "Presently", "Nowadays", "Up-to-date", "at this Moment", "Now", "the Latest", "With It", "Just Out", "Here and Now"]
#I want the program to select first from either the gate or usa list
#If it selects from gate than second half will come from today
#If it selects from usa than second half will come from house
start = random.randint(0, 1)
if start == 0:
    print(random.choice(gate) + " " + random.choice(today))
else:
    print (random.choice(usa) + " " + random.choice(house))
#Yes, I know the company is still keeping the name Gannett.