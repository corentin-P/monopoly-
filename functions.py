import pygame

pygame.init()

arial_font = pygame.font.SysFont("arial", 35, True, True)
txt_possessed = arial_font.render("Possessed !", True, (255,255,255))
txt_buy = arial_font.render("Buy?", True, (0,0,0))

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

def HouseCards(places, owned):
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



    if brown[0 and 1] in owned or light_blue[0 and 1 and 2] in owned or pink[0 and 1 and 2] in owned or orange[0 and 1 and 2] in owned or red[0 and 1 and 2] in owned or yellow[0 and 1 and 2] in owned or green[0 and 1 and 2] in owned or dark_blue[0 and 1] in owned:
        return True
    else :
        return False



def PlayerAttributes(player, other_player, window_pg, places):
    player.gold_txt = player.arial_font.render(str(player.gold), True, "#bf8200")
    window_pg.blit(player.gold_txt, (1090, 10))
    window_pg.blit(player.place_txt, (850, 50))
    window_pg.blit(player.name_txt, (200, 200))
    player.BlitCards()
    if player.buy == True and places[player.position]["Name"] not in player.cards and (
            player.places[player.position]["Class"] == "Terain" or player.places[player.position][
        "Class"] == "Train" or player.places[player.position]["Class"] == "Works") and places[player.position][
        "Name"] not in other_player.cards:
        window_pg.blit(txt_buy, player.buy_rect)
    else:
        window_pg.fill("#000000", pygame.Rect((800, 100), (250, 50)))
    if places[player.position]["Name"] in player.cards:
        window_pg.blit(txt_possessed, player.buy_rect)

    #if HouseCards(places, player.cards)==True:
     #   window_pg.blit

