import tkinter as tk
from random import randint
from objects import *
import csv
from functions import *

#open csv file and record the file in the places dict
places = []
with open("board2.csv") as fichier_csv:
   dict_csv= list(csv.DictReader(fichier_csv, delimiter=';'))
   for ligne in dict_csv:
      places.append(dict(ligne))
image_money = pygame.image.load("money_image.png")
image_money = pygame.transform.scale(image_money, (30,30))

#start pygame and creat a window
pygame.init()
window_pg = pygame.display.set_mode((1200,700))

#color of all the cards of the game
cards_color = []
for i in range(len(places)):
    cards_color.append(places[i]["Color"])

DrawGame(window_pg, cards_color)

de_click = pygame.Rect((150,350), (320,100))
next_click = pygame.Rect((350, 200), (210,50))
pygame.draw.rect(window_pg, (255,255,255), de_click)
pygame.draw.rect(window_pg, (255,255,255), next_click)


player2= Player("player2", window_pg, 36, places, (0,255,0))
player1 = Player("player1",window_pg, 36, places, (0,0,255))


w_player = 1
de1=0
de2=0
arial_font = pygame.font.SysFont("arial", 35, True, True)
txt_jouer = arial_font.render("Lancer les dés !", True, (0,0,0))
txt_buy = arial_font.render("Buy?", True, (0,0,0))
txt_possessed = arial_font.render("Possessed !", True, (255,255,255))
txt_next_player = arial_font.render("Next player?", False, (0,0,0))

"""for i in range(len(places)):
    if places[i]["Class"] == "Terain" or places[i]["Class"] == "Train" or places[i]["Class"] == "Works":
        player1.cards.append(places[i]["Name"])
"""

launched = True
while launched:
    window_pg.fill("#000000", pygame.Rect((850, 50), (300, 50)))
    window_pg.fill("#000000", pygame.Rect((1090, 10), (100, 50)))
    window_pg.fill("#000000", pygame.Rect((200, 200), (150, 50)))

    if w_player == 1:
        player1.gold_txt = player1.arial_font.render(str(player1.gold), True, "#bf8200")
        window_pg.blit(player1.gold_txt, (1090, 10))
        window_pg.blit(player1.place_txt, (850, 50))
        window_pg.blit(player1.name_txt, (200,200))
        player1.BlitCards()
        if player1.buy == True and places[player1.position]["Name"] not in player1.cards and (player1.places[player1.position]["Class"] == "Terain" or player1.places[player1.position]["Class"] == "Train" or player1.places[player1.position]["Class"] == "Works") and places[player1.position]["Name"] not in player2.cards:
            window_pg.blit(txt_buy, player1.buy_rect)
        else:
            window_pg.fill("#000000", pygame.Rect((800, 100), (250, 50)))
        if places[player1.position]["Name"] in player1.cards:
            window_pg.blit(txt_possessed, player1.buy_rect)

    elif w_player == 2:
        player2.gold_txt = player2.arial_font.render(str(player2.gold), True, "#bf8200")
        window_pg.blit(player2.gold_txt, (1090, 10))
        window_pg.blit(player2.place_txt, (850, 50))
        window_pg.blit(player2.name_txt, (200, 200))
        player2.BlitCards()

        if player2.buy == True and places[player2.position]["Name"] not in player2.cards and (
                player2.places[player2.position]["Class"] == "Terain" or player2.places[player2.position][
            "Class"] == "Train" or player2.places[player2.position]["Class"] == "Works") and places[player2.position]["Name"] not in player1.cards:
            window_pg.blit(txt_buy, player2.buy_rect)
        else:
            window_pg.fill("#000000", pygame.Rect((800, 100), (250, 50)))
        if places[player2.position]["Name"] in player2.cards:
            window_pg.blit(txt_possessed, player2.buy_rect)

    window_pg.blit(txt_next_player, (350,200))
    window_pg.blit(image_money, (1170, 10))
    window_pg.blit(txt_jouer, (150, 380))




    pygame.display.flip()
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            launched=False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if de_click.collidepoint(event.pos):
                de1 = randint(1, 6)
                de2 = randint(1, 6)

                if w_player==1:
                    player1.move(de1 + de2, cards_color)
                elif w_player == 2:
                    player2.move(de1 + de2, cards_color)

                if w_player==1 and places[player1.position]["Name"] in player2.cards:
                    if places[player1.position]["Class"]=="Works":
                        Pay(player1, player2, 4*(de1+de2))
                    else:
                        Pay(player1, player2, int(places[player1.position]["House 0"]))

                elif w_player==2 and places[player2.position]["Name"] in player1.cards:
                    if places[player2.position]["Class"]=="Works":
                        Pay(player2, player1, 4 * (de1 + de2))
                    else:
                        Pay(player2, player1, int(places[player2.position]["House 0"]))

            if w_player==1 and player1.buy_rect.collidepoint(event.pos) and player1.buy == True and places[player1.position]["Name"] not in player1.cards and places[player1.position]["Name"] not in player2.cards:
                player1.gold -= int(places[player1.position]["Cost"])
                player1.cards.append(places[player1.position]["Name"])
                print("1: ", player1.cards)
                player1.buy = False


            if w_player==2 and player2.buy_rect.collidepoint(event.pos) and player2.buy == True and places[player2.position]["Name"] not in player2.cards and places[player2.position]["Name"] not in player1.cards:
                player2.gold -= int(player2.places[player2.position]["Cost"])
                player2.cards.append(places[player2.position]["Name"])
                print("2: ", player2.cards)
                player2.buy = False


            if next_click.collidepoint(event.pos):
                if w_player==1:
                    w_player=2
                elif w_player==2:
                    w_player=1
