#This script will generate a GUI that will display a given mission, dificutly, and loadout for an operations mission in Warhammer 40K Space Marine 2
#Created by: Disk5464
#Last Modified: 11/12/24
#Version 1.0: Inital Commit
#Version 1.1: Removed Minimal dificulty, if your using this tool your not playing on Minimal. 
#             Added weights to the difficulty so that Substantial and Ruthless are chosen slightly more often.
#             Fixed a visual bug with the quote section not properly resetting. 
#####################################################################
#Import the required libaries
import os, sys, random
import tkinter as tk
from tkinter import ttk, scrolledtext

#####################################################################
#Get the current working directory, this will allow us to avoid hard coding paths.
script_directory = os.path.dirname(os.path.abspath(sys.argv[0])) 

#####################################################################
#Create the new GUI, give it a title, and an icon at the top
window = tk.Tk()
window.title("Randomized Space Marine 2 Mission Selector")
window.geometry('700x375')
window.minsize(200, 200)
window.maxsize(1000, 1000)
window.iconbitmap(script_directory + "\SM2.ico")

#Create the grid. https://www.pythontutorial.net/tkinter/tkinter-grid/
window.columnconfigure(0, weight=1)
window.columnconfigure(1, weight=1)

#Add a header at the top center and add it to the window. Make it bold and stretch over two columns
greeting = ttk.Label(text="Randomized Space Marine 2 Mission Selector", font=("Helvetica", 20, "bold"), compound='left')
greeting.grid(column=0, row=0, columnspan=2, padx=5, pady=5)

#This is an array that will hold the values that are currently in the right column. This gets populated by XX then cleared out by YY
resetRightColumnArry = []
quoteLableArry = []

#####################################################################
#Define the triggers for when different events happen. The first one is triggered when escape is pressed
def close_window(event):
    window.destroy()

#This will re-roll everything when the re-roll button is pressed
def button_press(event):
    #These for loops clear out the right column and quote row to prepare them for the new data that is about to be added.
    for e in resetRightColumnArry:
        e.config(text="")

    for f in quoteLableArry:
        f.config(text="")

    #Run the trigger that fills out the data
    fillOutRandom()
    randomquote()

#Get a random mission
def getRandomMission():
    global missionArry
    missionArry = ["Inferno", "Decapitation", "Vox Liberatis", "Reliquary", "Fall of Arteus", "Ballistic Engine", "Termination"]
    mission = random.choice(missionArry)
    return mission

#Get a random difficulty
def getRandomDifficutly():
    difficutlyArry = ["Average", "Substantial", "Ruthless", "Lethal"]
    difficutly = random.choices(difficutlyArry, weights=(10,17,15,10))
    return difficutly

#Get a random class
def getRandomClass():
    classArry = ["Tactical", "Assault", "Vanguard", "Bulwark", "Sniper", "Heavy"]
    single_class = random.choice(classArry) #I wanted to use class as the var name but that's a reserved term, so single_class it is
    return single_class

#Get a random primary weapon
def getRandomWeapon1(selectedClass):
    if(selectedClass == "Tactical"):
        primaryGunArry = ["Auto Bolt Rifle","Bolt Rifle","Heavy Bolt Rifle","Stalker Bolt Rifle","Bolt Carbine","Plasma Incinerator","Melta Rifle"] 
    elif(selectedClass =="Vanguard"):
        primaryGunArry = ["Melta Rifle","Instigator Bolt Carbine","Occulus Bolt Carbine"] 
    elif(selectedClass =="Sniper"):
        primaryGunArry = ["Stalker Bolt Rifle","Bolt Carbine","Bolt Sniper Rifle","Las Fusil"] 
    elif(selectedClass =="Heavy"):
        primaryGunArry = ["Heavy Bolter ", "Heavy Plasma Incinerator", "Multi-Melta"]
    elif(selectedClass =="Assault" or selectedClass =="Bulwark"):
        primaryGunArry = ["None"]

    gun1 = random.choice(primaryGunArry)
    return gun1

#Get a random secondary weapon
def getRandomWeapon2(selectedClass):
    if(selectedClass =="Vanguard"):
        secondaryGunArry = ["Bolt Pistol", "Plasma Pistol", "Neo-Volkite"]
    elif(selectedClass == "Tactical" or selectedClass =="Sniper"):
        secondaryGunArry = ["Bolt Pistol", "Plasma Pistol"]
    elif(selectedClass =="Bulwark"):
        secondaryGunArry = ["Bolt Pistol", "Neo-Volkite"] 
    elif(selectedClass =="Heavy"):
        secondaryGunArry = ["Bolt Pistol"] 
    elif(selectedClass =="Assault"):
        secondaryGunArry = ["Neo-Volkite"]

    gun2 = random.choice(secondaryGunArry)
    return gun2

#Get a random melee weapon
def getRandomMelee(selectedClass):
    if(selectedClass == "Assault"):
        secondaryGunArry = ["Chainsword", "Thunder Hammer", "Power Fist"] 
    elif(selectedClass =="Bulwark"):
        secondaryGunArry = ["Chainsword", "Power Fist", "Power Sword"] 
    elif(selectedClass =="Vanguard"):
        secondaryGunArry = ["Chainsword","Combat Knife"] 
    elif(selectedClass =="Sniper"):
        secondaryGunArry = ["Combat Knife"] 
    elif(selectedClass == "Tactical"):
        secondaryGunArry = ["Chainsword"] 
    elif(selectedClass =="Heavy" or selectedClass =="Bulwark"):
        secondaryGunArry = ["None"]

    gun2 = random.choice(secondaryGunArry)
    return gun2

#Get a random quote from the quote array.
def randomquote():
    #An array full of quotes
    quotesArry = ["No Pity! No Remorse! No Fear! - Chaplain Grimaldus",
    "Only in death does duty end. - Imperium of Man",
    "The difference between heresy and treachery is ignorance. - Inquisition",
    "Knowledge is power, guard it well. - Inquisitor Kryptman",
    "To admit defeat is to blaspheme against the Emperor. - Imperial Guard",
    "Give me a hundred Space Marines. Or failing that, give me a thousand other troops. - Primarch Rogal Dorn",
    "Even in death, I still serve. - Space Marines",
    "Innocence proves nothing. - Inquisition",
    "There is no such thing as innocence, only degrees of guilt. - Inquisition",
    "Pain is an illusion of the senses, despair an illusion of the mind. - Legion of the Damned",
    "I am the hammer, I am the mail about His fist. I am the Spear in His hand. - Space Marines",
    "Hope is the first step on the road to disappointment. - Space Marines",
    "From the moment I understood the weakness of my flesh, it disgusted me. I craved the strength and certainty of steel. - Adeptus Mechanicus",
    "I have no fear, for I am fear incarnate. - Space Marines",
    "Walk softly, and carry a big gun. - Imperial Guard",
    "Brother I am pinned here! - Space Marines",
    "For the Emperor! - Space Marines",
    "An open mind is like a fortress with its gates unbarred and unguarded. - Blood Ravens Librarian",
    "Blessed is the mind too small for doubt. - Imperium of Man",
    "By His will alone is Terra kept safe. - Adeptus Custodes",
    "Ruthlessness is the kindness of the wise. - Lord Solar Macharius",
    "They shall be my finest warriors, these men who give of themselves to me. - The Emperor of Mankind",
    "Suffer not the unclean to live. - Inquisition",
    "What I cannot crush with words, I will crush with the tanks of the Imperial Guard! - Imperial Guard Commander",
    "Victory is but a prelude to the next battle. - Space Marines",
    "Only in death does duty end. - Imperium of Man",
    "Victory is achieved through mettle. Glory is achieved through metal. - Iron Hands Chapter"
    ]

    #Select a random quote, put it in a label
    quote= random.choice(quotesArry)
    quoteLabel = tk.Label(window, text=quote, font=(19), wraplength=650)
    quoteLabel.grid(column=0, row=8, columnspan=2, rowspan=2,  padx=5, pady=5) #Put the label on a grid 

    #Add the label to the array that is used to clear it out when the button gets pressed. 
    quoteLableArry.append(quoteLabel)

#This triggers when the user changes a drop down item
def changedEvent(callback):
    print(callback)
    callback['state'] = 'disabled'
    #callback.bind('<<ComboboxSelected>>', callback)

#Fill out the random lines. This gets triggered when the GUI spawns and any time the re-roll button is clicked (via button_press()).
def fillOutRandom():
    selectedMission = getRandomMission()
    selectedClass = getRandomClass()
    selectedDifficulty = getRandomDifficutly()
    primaryGun = getRandomWeapon1(selectedClass)
    secondaryGun = getRandomWeapon2(selectedClass)
    meleeGun = getRandomMelee(selectedClass)

    right_label_texts = {
        "mission_Label": selectedMission, 
        "difficulty_Label":selectedDifficulty,
        "class_Label": selectedClass,
        "weapon1_Label": primaryGun,
        "weapon2_Label": secondaryGun,
        "weapon3_Label": meleeGun
    }

    #For loop that loops through each dictornay value and creates label bassed of each
    for i, (key, text) in enumerate(right_label_texts.items()):  #For each item in the dict reach each key/value
        label = ttk.Combobox(window, state="readonly", values=missionArry, font=12)  #Create a read only dropdown box with all of the missions in
        label.set(text) #Set the default value to the random item
        label.bind('<<ComboboxSelected>>', changedEvent) #This triggeres changedEvent whenever the user changes a dropdown box
        label.grid(row=i+1, column=1,  padx=5, pady=5, sticky=tk.E ) #Put the label on a grid  
        resetRightColumnArry.append(label) #Add the dropdown box variable name to an array. This gets used when the button is pressed and everything is cleared out


#####################################################################
#This section will fill out the left column. The first step is to create a dictionary with key value pairs. They key is the name of the variable and the value is what the lable with be shown.
left_label_texts = {
    "mission_Label":"Your mission is:", 
    "difficulty_Label":"Your difficulty is:",
    "class_Label":"Your class is:",
    "weapon1_Label": "Your primary weapon is:",
    "weapon2_Label": "Your secondary weapon is:",
    "weapon3_Label": "Your melee weapon is:"
}

#For loop that loops through each dictornay value and creates label bassed of each
for i, (key, text) in enumerate(left_label_texts.items()):  #For each item in the dict reach each key/value
    label = ttk.Label(window, text=text, font=12)    #Create a new label with the info for the current object
    label.grid(row=i+1, column=0,  padx=5, pady=5, sticky=tk.W) #Put the label on a grid 

#####################################################################
#This section will fill out the right column and the quote when the GUI first spawns. It calls fillOutRandom() and randomquote() which are also called when the re-roll button is pressed. It's pulling double duty here, inital spawn and re-roll. 
fillOutRandom()
randomquote()

#####################################################################
#This section creates the btton which lets your re-roll your setup
button = tk.Button(window, text="Click for another mission")    #Create a new button with the info for the current object
button['font'] = 12
button.grid(column=0, row=7, columnspan=2, padx=5, pady=5) #Put the label on a grid 
button.bind("<Button-1>", button_press)

#####################################################################
#Set it so that the escape key closes the window. Then start a loop that pauses the shell until the menu is closed
window.bind('<Escape>', close_window)
window.mainloop()
