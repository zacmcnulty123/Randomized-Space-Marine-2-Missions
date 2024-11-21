
#Import the required libaries
import os, sys, random
import tkinter as tk
from tkinter import ttk, scrolledtext

#####################################################################
#Create the window, give it a size, title, min and max size. 
window = tk.Tk()
window.title("Randomized Space Marine 2 Mission Selector")
window.geometry('700x375')
window.minsize(200, 200)
window.maxsize(1000, 1000)

#Create the grid. https://www.pythontutorial.net/tkinter/tkinter-grid/
window.columnconfigure(0, weight=1)
window.columnconfigure(1, weight=1)

#Add a header at the top center and add it to the window. Make it bold and stretch over two columns
greeting = ttk.Label(text="Randomized Space Marine 2 Mission Selector", font=("Helvetica", 20, "bold"), compound='left')
greeting.grid(column=0, row=0, columnspan=2, padx=5, pady=5)

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
#This section creates the button at the bottom which lets your re-roll your setup
button = tk.Button(window, text="Click for another mission")    #Create a new button with the info for the current object
button['font'] = 12
button.grid(column=0, row=7, columnspan=2, padx=5, pady=5) #Put the label on a grid 

#####################################################################
#####################################################################
#####################################################################
#This section will create the functions that will be used with the bellow UI elements




#This section creates the check boxes in the right column. It first creates variables for the status of the box, then it creates the box, finally it adds it ot the grid. 
mission_Check_state = tk.IntVar()
difficulty_Check_state = tk.IntVar()
class_Check_state = tk.IntVar()
primary_Check_state = tk.IntVar()
secondary_Check_state= tk.IntVar()
melee_Check_state = tk.IntVar()

check_Box_Mission = tk.Checkbutton(window, text="mission", variable=mission_Check_state, onvalue=1, offvalue=0)
check_Box_Difficulty = tk.Checkbutton(window, text="difficulty", variable=difficulty_Check_state, onvalue=1, offvalue=0)
check_Box_Class = tk.Checkbutton(window, text="class", variable=class_Check_state, onvalue=1, offvalue=0)
check_Box_Primary = tk.Checkbutton(window, text="primary", variable=primary_Check_state, onvalue=1, offvalue=0)
check_Box_Secondary = tk.Checkbutton(window, text="secondary", variable=secondary_Check_state, onvalue=1, offvalue=0)
check_Box_Melee = tk.Checkbutton(window, text="melee", variable=melee_Check_state, onvalue=1, offvalue=0)

check_Box_Mission.grid(column=2, row=1, columnspan=1, padx=5, pady=5) 
check_Box_Difficulty.grid(column=2, row=2, columnspan=1, padx=5, pady=5)
check_Box_Class.grid(column=2, row=3, columnspan=1, padx=5, pady=5) 
check_Box_Primary.grid(column=2, row=4, columnspan=1, padx=5, pady=5)
check_Box_Secondary.grid(column=2, row=5, columnspan=1, padx=5, pady=5)
check_Box_Melee.grid(column=2, row=6, columnspan=1, padx=5, pady=5)


#####################################################################
#This section defines functions that are tinker related. The first one is triggered when escape is pressed



def close_window(event):
    window.destroy()



    #Run the trigger that fills out the data
    #fillOutRandom()
    #randomquote()

#####################################################################
#This section is for functions that deal with the random data. There is one function for each row. The first gets a random mission

def getRandomMission():
    missionArry = ["Inferno", "Decapitation", "Vox Liberatis", "Reliquary", "Fall of Arteus", "Ballistic Engine", "Termination"]
    mission = random.choice(missionArry)
    return mission

#Get a random difficulty. Each difficutly is weighted slightly so that Substantial and Ruthless come up a bit more often
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


#####################################################################
#####################################################################
#This will re-roll everything when the re-roll button is pressed
def button_press(event):

    print("Button Pessed")

    if mission_Check_state.get() == 0:
        newMission = getRandomMission()
        print("Rerolling Mission " + newMission)

    if difficulty_Check_state.get() == 0:
        newDifficutly = getRandomDifficutly()
        print("Rerolling Difficulty " + newDifficutly)

    if class_Check_state.get() == 0:
        newClass = getRandomClass()
        print("Rerolling Class " + newClass)

    if primary_Check_state.get() == 0:
        newPrimary = getRandomWeapon1()
        print("Rerolling Primary " + newPrimary)

    if secondary_Check_state.get() == 0:
        newSecondary = getRandomWeapon2()
        print("Rerolling Secondary " + newSecondary)

    if melee_Check_state.get() == 0:
        newMelee = getRandomMelee()
        print("Rerolling Melee " + newMelee)








#####################################################################
#Set it so that the escape key closes the window. Next tie  Then start a loop that pauses the shell until the menu is closed
window.bind('<Escape>', close_window)
button.bind("<Button-1>", button_press)
window.mainloop()