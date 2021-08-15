import pygame

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
