import tkinter as tk
from tkinter import ttk
from objects import *

def Valid(current, build_app):
    fill = "                                                           "

    family = [['Brown - 1 ', 'Brown - 2'], ['Light-Blue-1', 'Light-Blue-2', 'Light-Blue-3'],
     ['Pink - 1', 'Pink - 2', 'Pink - 3'], ['Orange - 1', 'Orange - 2', 'Orange - 3'], ['Red - 1', 'Red -2', 'Red -3'],
     ['Yellow - 1', 'Yellow - 2', 'Yellow - 3'], ['Green - 1', 'Green - 2', 'Green - 3'],
     ['Dark - Blue - 1', 'Dark - Blue - 2']]
    card1 = tk.Label(build_app, text=fill)
    card1.grid(row=2, column=1)
    card1 = tk.Label(build_app, text=family[current][0], font=('Arial', 11, 'underline', 'bold'))
    card1.grid(row=2, column=1)

    currently1 = tk.Label(build_app, text = "\nThere is currently" +"\n")
    currently1.grid(row = 3, column = 1)
    build1 = tk.Label(build_app, text = "Build\n")
    build1.grid(row = 4, column = 1)



    card2 = tk.Label(build_app, text = fill)
    card2.grid(row=5, column=1)
    card2 = tk.Label(build_app, text=family[current][1], font=('Arial', 11, 'underline', 'bold'))
    card2.grid(row=5, column=1)

    currently2 = tk.Label(build_app, text = "\nThere is currently" +"\n")
    currently2.grid(row = 6, column = 1)

    build2 = tk.Label(build_app, text="Build\n")
    build2.grid(row=7, column=1)

    card3 = tk.Label(build_app, text=fill)
    card3.grid(row=8, column=1)

    currently3 = tk.Label(build_app, text = '\n'+fill)
    currently3.grid(row = 9, column = 1)

    build3 = tk.Label(build_app, text=fill)
    build3.grid(row=10, column=1)
    if len(family[current]) > 2 :
        card3 = tk.Label(build_app, text=family[current][2], font=('Arial', 11, 'underline', 'bold'))
        card3.grid(row=8, column=1)

        currently2 = tk.Label(build_app, text="\nThere is currently" +"\n")
        currently2.grid(row=9, column=1)

        build3 = tk.Label(build_app, text="Build\n")
        build3.grid(row=10, column=1)


def BuildApp():
    house_get = tk.IntVar
    hotel_get = tk.IntVar
    build_app = tk.Tk()
    build_app.title("Build House and Hotels?")
    build_app.geometry("200x200")
    current_var = tk.StringVar()

    # Box to select the families on which we build
    build_box = ttk.Combobox(build_app, values=[['Brown - 1 ', 'Brown - 2'], ['Light-Blue-1', 'Light-Blue-2', 'Light-Blue-3'], ['Pink - 1', 'Pink - 2', 'Pink - 3'], ['Orange - 1', 'Orange - 2', 'Orange - 3'], ['Red - 1', 'Red -2', 'Red -3'], ['Yellow - 1', 'Yellow - 2', 'Yellow - 3'], ['Green - 1', 'Green - 2', 'Green - 3'], ['Dark - Blue - 1', 'Dark - Blue - 2']], textvariable = current_var)
    build_box['state'] = 'readonly'
    build_box.current(0)



    valid_button = tk.Button(build_app, text="Valid", command= lambda : Valid(build_box.current(), build_app))

    #print(hotel_get.get(hotel_get))
    build_box.grid(row = 0, column = 1)

    valid_button.grid(row = 0, column = 2)

    build_app.mainloop()

BuildApp()