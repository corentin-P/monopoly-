import pygame
import tkinter as tk
from tkinter import ttk

pygame.init()

arial_font = pygame.font.SysFont("arial", 35, True, True)
txt_possessed = arial_font.render("Owned !", True, (255,255,255))
txt_buy = arial_font.render("Buy?", True, (0,0,0))
txt_build = arial_font.render("Build?", True, (0,0,0))


def DrawGame(window_pg, cards_color):
    for i in range(10):
        pygame.draw.rect(window_pg, "#" + cards_color[i], pygame.Rect((i * 62 + 5, 5), (62, 62)))
        pygame.draw.rect(window_pg, "#" + cards_color[i + 10], pygame.Rect((625, i * 62 + 5), (62, 62)))
        pygame.draw.rect(window_pg, "#" + cards_color[i + 20], pygame.Rect((-i * 62 + 625, 625), (62, 62)))
        pygame.draw.rect(window_pg, "#" + cards_color[i + 30], pygame.Rect((5, -i * 62 + 625), (62, 62)))
    # creat all the lines for the monopoly game
    for i in range(9):
        pygame.draw.line(window_pg, (255, 255, 255), [67 + (i * 62), 5], [67 + (i * 62), 67])
        pygame.draw.line(window_pg, (255, 255, 255), [625, 67 + (62 * i)], [687, 67 + (62 * i)])
        pygame.draw.line(window_pg, (255, 255, 255), [67 + (i * 62), 625], [67 + (i * 62), 687])
        pygame.draw.line(window_pg, (255, 255, 255), [5, 67 + (62 * i)], [67, 67 + (62 * i)])
    pygame.draw.line(window_pg, (255, 255, 255), [5, 5], [687, 5])
    pygame.draw.line(window_pg, (255, 255, 255), [5, 67], [687, 67])
    pygame.draw.line(window_pg, (255, 255, 255), [5, 5], [5, 687])
    pygame.draw.line(window_pg, (255, 255, 255), [67, 5], [67, 687])
    pygame.draw.line(window_pg, (255, 255, 255), [687, 5], [687, 687])
    pygame.draw.line(window_pg, (255, 255, 255), [625, 5], [625, 687])
    pygame.draw.line(window_pg, (255, 255, 255), [5, 687], [687, 687])
    pygame.draw.line(window_pg, (255, 255, 255), [5, 625], [687, 625])

def Pay(player1, player2, cost):
    print(cost)
    player1.gold -= cost
    player2.gold += cost

def HouseCards(places, owned, player):
    Terrain = []
    for i in range(len(places)):
        if places[i]["Class"]=="Terain":
            Terrain.append(places[i])

    brown = [Terrain[0]["Name"], Terrain[1]["Name"]]
    light_blue = [Terrain[2]["Name"], Terrain[3]["Name"], Terrain[4]["Name"]]
    pink = [Terrain[5]["Name"], Terrain[6]["Name"], Terrain[7]["Name"]]
    orange = [Terrain[8]["Name"], Terrain[9]["Name"], Terrain[10]["Name"]]
    red = [Terrain[11]["Name"], Terrain[12]["Name"], Terrain[13]["Name"]]
    yellow = [Terrain[14]["Name"], Terrain[15]["Name"], Terrain[16]["Name"]]
    green = [Terrain[17]["Name"], Terrain[18]["Name"], Terrain[19]["Name"]]
    dark_blue = [Terrain[20]["Name"], Terrain[21]["Name"]]

    #if the player had a family of cards, it will add this family to his collection
    if (brown[0] in owned and brown[1] in owned) and brown not in player.families_cards:
        player.families_cards.append(brown)
    if (light_blue[0] in owned and light_blue[1] in owned and light_blue[2] in owned) and light_blue not in player.families_cards:
        player.families_cards.append(light_blue)
    if (pink[0] in owned and pink[1] in owned and pink[2] in owned) and pink not in player.families_cards:
        player.families_cards.append(pink)
    if (orange[0] in owned and orange[1] in owned and orange[2] in owned) and orange not in player.families_cards:
        player.families_cards.append(orange)
    if (red[0] in owned and red[1] in owned and red[2] in owned) and red not in player.families_cards:
        player.families_cards.append(red)
    if (yellow[0] in owned and yellow[1] in owned and yellow[2] in owned) and yellow not in player.families_cards:
        player.families_cards.append(yellow)
    if (green[0] in owned and green[1] in owned and green[2] in owned) and green not in player.families_cards:
        player.families_cards.append(green)
    if (dark_blue[0] in owned and dark_blue[1] in owned) and dark_blue not in player.families_cards:
        player.families_cards.append(dark_blue)

    #return True if the player had a family
    if len(player.families_cards) != 0:
        return True
    else:
        return False

def PlayerAttributes(player, other_player, window_pg, places, build_rect):

    #Set the font for the text of the gold of the player
    player.gold_txt = player.arial_font.render(str(player.gold), True, "#bf8200")

    #Show the gold, the place and the name of the player
    window_pg.blit(player.gold_txt, (1090, 10))
    window_pg.blit(player.place_txt, (850, 50))
    window_pg.blit(player.name_txt, (200, 200))

    #Show all the cards of the Player
    player.BlitCards()

    #Show the buy text
    if places[player.position]["Name"] not in player.cards and (
            player.places[player.position]["Class"] == "Terain" or player.places[player.position][
        "Class"] == "Train" or player.places[player.position]["Class"] == "Works") and places[player.position][
        "Name"] not in other_player.cards and player.gold >=int(places[player.position]["Cost"]):

        window_pg.blit(txt_buy, player.buy_rect)
    else:
        window_pg.fill("#000000", pygame.Rect((770, 100), (250, 50)))
    if places[player.position]["Name"] in player.cards:
        window_pg.blit(txt_possessed, player.buy_rect)

    #Player can build houses or not
    if HouseCards(places, player.cards, player)==True:
        pygame.draw.rect(window_pg, "#FFFFFF", build_rect)
        window_pg.blit(txt_build, build_rect)
    else:
        window_pg.fill("#000000", build_rect)

def Valid():
    print("v")

def BuildApp(player):
    house_get = tk.IntVar
    hotel_get = tk.IntVar
    build_app = tk.Tk()
    build_app.title("Build House and Hotels?")
    build_app.geometry("200x200")

    house_labels = tk.Label(build_app, text = "construire des maisons?")
    hotels_labels = tk.Label(build_app, text = "construire des hotels?")

    build_box = ttk.Combobox(build_app, values=player.families_cards)
    build_box['state'] = 'readonly'
    build_box.current(0)

    house = tk.Checkbutton(build_app, variable = house_get, onvalue = 1, offvalue = 0)
    hotel = tk.Checkbutton(build_app, variable = hotel_get, onvalue = 1, offvalue = 0)

    valid_button = tk.Button(build_app, text="Valid", command=Valid)

    #print(hotel_get.get(hotel_get))
    build_box.grid(row = 0, column = 1)
    house.grid(row = 1, column = 0)
    house_labels.grid(row = 1, column = 1)
    hotel.grid(row=2, column=0)
    hotels_labels.grid(row=2, column=1)
    valid_button.grid(row = 3, column = 3)

    build_app.mainloop()

