# Front end:
# Emulate the visual experience of a pokemon trading card battle
# Pick up and place cards, move cards, knock out cards, level up cards, show damage, and show special conditions (manual or automatic)

# Back end:
# Emulate the functional characteristics of a pokemon trading card battle
# Drawing cards, searching for cards, returning cards to the deck, shuffling the deck

# Imports
import tkinter as tk
from PIL import Image, ImageTk
import json

# Basic definitions

# Resize an image from https://stackoverflow.com/a/69307786
def resizeImage(img, newWidth, newHeight):
    oldWidth = img.width()
    oldHeight = img.height()
    newPhotoImage = tk.PhotoImage(width=newWidth, height=newHeight)
    for x in range(newWidth):
        for y in range(newHeight):
            xOld = int(x*oldWidth/newWidth)
            yOld = int(y*oldHeight/newHeight)
            rgb = '#%02x%02x%02x' % img.get(xOld, yOld)
            newPhotoImage.put(rgb, (x, y))
    return newPhotoImage

# Store all attack attributes in an attack object class
class attack:
    def __init__(self, name: str, cost: list,  damage: list, effects: str):
        self.name = name
        self.cost = cost
        self.damage = damage
        self.effects = effects
    def __str__(self):
        return f"{self.name} {self.cost} {self.damage} {self.effects}"

# Store all ability attributes in an ability object class
class ability:
    def __init__(self, name: str, effects: str):
        self.name = name
        self.effects = effects
    def __str__(self):
        return f"{self.name} {self.effects}"

# Store all card attributes in a card object
class card:
    def __init__(self, name: str, image, set: str=None, coll:int =None, reg: str=None):
        self.name = name
        self.set = set
        self.coll = coll
        self.reg = reg
        self.image = image
    def __str__(self):
        return f"{self.name} {self.hp}"
    def __repr__(self):
        return self.__str__()

# Window drawing
window = tk.Tk()
window.title("Image in Tkinter")
greet = tk.Label(text="Hello")
greet.grid(row=0, column=0, padx=10, pady=5)

# Set window size
window.maxsize(1600, 900)

# Create canvas for images
canvas = tk.Canvas(window, width=600, height=600)
canvas.grid(row=0, column=1, padx=10, pady=5)

# Window functions
def enlargeOnClick(item):
    enlargedItem = tk.PhotoImage(file=item)
    enlargedCanvas = tk.Canvas(window, width=600, height=600, bg="light grey")
    enlargedCanvas.create_image(50, 50, anchor="nw", image=enlargedItem)
    enlargedCanvas.grid(row=0, column=0, rowspan=5, columnspan=5)

# Card management
deck = [] # Will contain exactly 60 cards





# pika_atk1 = {"name": "Barrel", "cost": ["colorless", "electric"], "damage": 10, "effects": None}
# Define the first attack
pika_atk1 = attack("Barrel", ["colorless", "lightning"], 10, None)

# Load image
pika_img = tk.PhotoImage(file="Images/pikachu_with_grey_felt_hat.png")
# Resize image
pika_img = resizeImage(pika_img, 300, 300)
# Place image on canvas
canvas.create_image(50, 50, anchor="nw", image=pika_img)
canvas.create_text(0, 0, anchor="nw", text="original was very large\nNow it is 300x300")

pika = card("pika", pika_img, "CEL", 2, "G")

# Array containing a bunch of card images
bench = [pika_img, pika_img, pika_img]

# Frame that contains the bench
bench_frame = tk.Frame(window, width=800, height=300, bg="grey")
bench_frame.grid(row=1, column=0, columnspan=5, sticky="w", padx=10, pady=5)

count = 0
for item in bench:
    tk.Label(bench_frame, image=item, relief="raised").grid(row=0, column=count, padx=10, pady=5)
    count += 1

# img_label = tk.Label(window, image=pika_img)

btnActiveImg = tk.PhotoImage(file="Images/pikachu_with_grey_felt_hat.png")
btnActiveLabel = tk.Label(image=btnActiveImg)
btnActive = tk.Button(window, image=pika_img, command= lambda: enlargeOnClick("Images/pikachu_with_grey_felt_hat.png"), padx=10, pady=5)
btnActive.grid(row=0, column=1)





# Game logic

# Load a deck from JSON file
# filename = "alakazam.json"
# loadedFile = json.loads(filename)

# for item in loadedFile:
#     itemName = item["name"]
#     itemSet = item["set"]
#     itemColl = item["coll"]
#     itemReg = item["reg"]
#     itemFilename = itemName + " " + itemSet + " " + str(itemColl) + ".jpg"
#     itemImage = tk.PhotoImage(file=itemFilename)
#     deck.append(card(itemName))

# print(deck)


# End program with window's main loop
window.mainloop()