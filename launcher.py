import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from main import *

def Valid():
    nbr_players = nbr_players_box.get()
    nbr_gold = nbr_gold_box.get()
    MonopolyGame()


launcher = tk.Tk()

launcher.title("Monopoly Launcher")
launcher.geometry("800x600")

label_welcome= tk.Label(launcher, text="Welcome to the Monopoly Launcher!\n")
label_players= tk.Label(launcher, text="How many players do you want?")
label_gold= tk.Label(launcher, text="How many dollars do you want?")
label_park = tk.Label(launcher, text = "\nIf a player go on the park, does he get money?")
label_go = tk.Label(launcher, text= "\nIf a player go on the Go case, how many gold does he receive?")
nbr_players_box = ttk.Combobox(launcher,values=["2","3","4"])
nbr_players_box['state'] = 'readonly'
nbr_players_box.current(0)
nbr_gold_box = ttk.Combobox(launcher, values = ["1000", "1250", "1500", "1750", "2000"])
nbr_gold_box.current(2)
park_box = ttk.Combobox(launcher, values = ["YES", "NO"])
park_box['state'] = 'readonly'
park_box.current(0)
go_box = ttk.Combobox(launcher, values = [200, 300])
go_box['state']='readonly'
go_box.current(0)
valid_button = tk.Button(launcher, text = "Valid", command = Valid)





label_players.grid(row=2, column = 1)
nbr_players_box.grid(row=3, column = 1)
label_gold.grid(row=2, column = 3)
nbr_gold_box.grid(row = 3, column = 3)
label_park.grid(row = 4, column = 1)
park_box.grid(row= 5, column = 1)
label_go.grid(row = 4, column = 3)
go_box.grid(row = 5, column =3)
valid_button.grid(row = 10, column = 3)
#nombre de joueurs
#argent de départ
#parcs gratuit qui redonne de l'argent ou pas
#300 dollars au lieu de 200 si tombé sur la case départ
#



#print on the screen
label_welcome.grid(row=1, column=2)

#mainloop
launcher.mainloop()