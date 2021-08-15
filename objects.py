import pygame

class Player(pygame.sprite.Sprite):
    def __init__(self, name,window_pg, position, places, color):
        super().__init__()

        self.name = name
        self.color = color
        self.gold = 1500
        self.position = 0
        self.position2 = 0
        self.places = places
        self.cards = []
        self.arial_font = pygame.font.SysFont("arial", 30, True, True)
        self.arial_font2 = pygame.font.SysFont("arial", 17, True, True)
        self.gold_txt = self.arial_font.render(str(self.gold), True, "#bf8200")
        self.place_txt = self.arial_font.render(self.places[self.position]["Name"], True, "#ffffff")
        self.name_txt = self.arial_font.render(self.name, True, "#ffffff")

        self.window_pg = window_pg
        self.lastest_position_x = position
        self.lastest_position_y = position
        self.buy_rect= pygame.Rect((800, 100), (90, 40))
        self.cards_rect = pygame.Rect((1060, 100), (130, 600))
        self.buy = True


        pygame.draw.circle(self.window_pg, self.color, (position, position), 20)

    def move(self, de, cards_color):
        self.position += de
        self.position2 += de
        self.buy= True
        pygame.draw.circle(self.window_pg, "#"+cards_color[self.position-de], (self.lastest_position_x, self.lastest_position_y), 20)
        self.window_pg.fill("#000000", pygame.Rect((800, 100), (250, 50)))
        self.window_pg.fill("#000000", self.cards_rect)


        if 10<self.position<20:
            self.position2 = self.position-10
            pygame.draw.circle(self.window_pg, self.color, (656, 62*(self.position2)+36), 20)
            self.lastest_position_x = 656
            self.lastest_position_y = 62*(self.position2)+36
            self.place_txt = self.arial_font.render(self.places[self.position]["Name"], True, "#ffffff")
        elif 20<=self.position<30:
            self.position2 = self.position-20
            pygame.draw.circle(self.window_pg, self.color, (656-(62 * (self.position2)), 656), 20)
            self.lastest_position_x = 656-(62 * (self.position2))
            self.lastest_position_y = 656
            self.place_txt = self.arial_font.render(self.places[self.position]["Name"], True, "#ffffff")
        elif 30<=self.position<40:
            self.position2 = self.position-30
            pygame.draw.circle(self.window_pg, self.color, (36, 656-(62 * (self.position2))), 20)
            self.lastest_position_x = 36
            self.lastest_position_y = 656-(62 * (self.position2))
            self.place_txt = self.arial_font.render(self.places[self.position]["Name"], True, "#ffffff")
        elif self.position>=40:
            if self.position == 40:
                self.gold+=300
            else:
                self.gold += 200
            self.position -= 40
            self.position2 = self.position
            pygame.draw.circle(self.window_pg, self.color, (62*(self.position2)+36, 36), 20)
            self.lastest_position_x = 62*(self.position2)+36
            self.lastest_position_y = 36
            self.place_txt = self.arial_font.render(self.places[self.position]["Name"], True, "#ffffff")
        else:
            pygame.draw.circle(self.window_pg, self.color, (62*(self.position2)+36, 36), 20)
            self.lastest_position_x = 62*(self.position2)+36
            self.lastest_position_y = 36
            self.place_txt = self.arial_font.render(self.places[self.position]["Name"], True, "#ffffff")

        if (self.places[self.position]["Class"]=="Terain" or self.places[self.position]["Class"]=="Train" or self.places[self.position]["Class"]=="Works") and self.places[self.position]["Name"] not in self.cards:
            pygame.draw.rect(self.window_pg, "#FFFFFF",self.buy_rect)
        if self.places[self.position]["Class"]=="Tax":
            self.gold -= int(self.places[self.position]["Cost"])

    def BlitCards(self):
        for i in range(len(self.cards)):
            self.cards_txt = self.arial_font2.render(self.cards[i], True, "#FFFFFF")
            self.window_pg.blit(self.cards_txt, pygame.Rect((1060,100+20*i),(140,20)))