import json

# Generate a decklist as a JSON object, then save it to file

# Store card details in a class
class card:
    def __init__(self, name, set=None, coll=None, reg=None):
        self.name = name
        self.set = set
        self.coll = coll
        self.reg = reg
    def __str__(self):
        return f"\n{self.name}"
    def __repr__(self):
        return self.__str__()
    # def showAll(self):
    #     return " ".join([f"{self.name} {self.set} {self.coll} {self.reg}" for card in self.])

def obj_dict(obj):
    return obj.__dict__

deck = [
    card("Abra", "MEW", 63, "G"),
    card("Abra", "MEW", 63, "G"),
    card("Abra", "MEW", 63, "G"),
    card("Abra", "MEW", 63, "G"),
    card("Kadabra", "MEW", 64, "G"),
    card("Alakazam ex", "MEW", 65, "G"),
    card("Alakazam ex", "SVP", 50, "G"),
    card("Alakazam ex", "SVP", 50, "G"),
    card("Mimikyu", "PAL", 97, "G"),
    card("Mimikyu", "PAL", 97, "G"),
    card("Klefki", "SVI", 96, "G"),
    card("Klefki", "SVI", 96, "G"),
    card("Radiant Alakazam", "SIT", 59, "F"),
    card("Manaphy", "BRS", 41, "F"),
    card("Jirachi", "PAR", 126, "G"),
    card("Zacian V", "CEL", 16, "E"),
    card("Counter Catcher"),
    card("Rare Candy"),
    card("Rare Candy"),
    card("Rare Candy"),
    card("Rare Candy"),
    card("Lost Vacuum"),
    card("Fog Crystal"),
    card("Fog Crystal"),
    card("Fog Crystal"),
    card("Fog Crystal"),
    card("Super Rod"),
    card("Super Rod"),
    card("Switch"),
    card("Switch"),
    card("Ultra Ball"),
    card("Ultra Ball"),
    card("Nest Ball"),
    card("Nest Ball"),
    card("Path to the Peak"),
    card("Path to the Peak"),
    card("Path to the Peak"),
    card("Pot Helmet"),
    card("Defiance Band"),
    card("Geeta"),
    card("Geeta"),
    card("Boss's Orders"),
    card("Boss's Orders"),
    card("Arven"),
    card("Arven"),
    card("Judge"),
    card("Judge"),
    card("Iono"),
    card("Iono"),
    card("Tulip")
]
for i in range(10):
    deck.append(card("Basic Psychic Energy"))

print("Deck size:", len(deck))
# print(deck)

# Now that the deck is populated, save it.
filename = "alakazam.json"
try:
    with open(filename, 'w+') as file:
        json.dump(deck, file, indent=2, ensure_ascii=False, default=obj_dict)
except:
    print("Error saving file.")