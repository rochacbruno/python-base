import random
import pygame
import pygame.locals as pg
from typing import Tuple

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (60, 220, 0)
YELLOW = (255, 240, 60)
GRAY = (50, 50, 50)

size = width, height = (800, 800)
road_w = int(width / 1.6)
roadmark_w = int(width / 200)
right_track = width / 2 + road_w / 4
left_track = width / 2 - road_w / 4
speed = 1

pygame.init()
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Catch a beer")
screen.fill(GREEN)
pygame.display.update()

player = pygame.image.load("player.png")
player = pygame.transform.scale(player, (150, 150))
player_loc = player.get_rect()
player_loc.center = right_track, height * 0.8

font = pygame.font.SysFont("Comic Sans MS", 40)
font2 = pygame.font.SysFont("Comic Sans MS", 90)


def load_a_random_beer() -> Tuple:
    i = random.randint(1, 5)
    beer = pygame.image.load(f"beers/{i}.png")
    beer = pygame.transform.scale(beer, (100, 100))
    beer_loc = beer.get_rect()
    if random.randint(0, 1) == 0:
        beer_loc.center = right_track, height * 0.2
    else:
        beer_loc.center = left_track, height * 0.2
    return beer, beer_loc


beer, beer_loc = load_a_random_beer()

points = 0
turns = 0
running = True
pause = True
while running:

    turns += 1

    if turns == 2500:
        speed += 0.5
        turns = 0
        print("Level UP", speed)

    # colision
    if player_loc[1] == beer_loc[1] and player_loc[0] == beer_loc[0] - 25:
        # print(f"{player_loc=}")
        # print(f"{beer_loc=}")
        points += 1
        beer, beer_loc = load_a_random_beer()

    beer_loc[1] += speed

    # events
    for event in pygame.event.get():
        if event.type == pg.QUIT:
            running = False
        if event.type == pg.KEYDOWN:
            if event.key in (pg.K_a, pg.K_LEFT):
                player_loc = player_loc.move((-int(road_w / 2), 0))
            if event.key in (pg.K_d, pg.K_RIGHT):
                player_loc = player_loc.move((int(road_w / 2), 0))

    # draw road
    pygame.draw.rect(screen, GRAY, (width / 2 - road_w / 2, 0, road_w, height))
    # draw centre line
    pygame.draw.rect(
        screen,
        YELLOW,
        (width / 2 - roadmark_w / 2, 0, roadmark_w, height),
    )
    # draw left road marking
    pygame.draw.rect(
        screen,
        WHITE,
        (width / 2 - road_w / 2 + roadmark_w * 2, 0, roadmark_w, height),
    )
    # draw right road marking
    pygame.draw.rect(
        screen,
        WHITE,
        (width / 2 + road_w / 2 - roadmark_w * 3, 0, roadmark_w, height),
    )

    banner = font.render(f"Catch a Beer! {points}", 1, WHITE, BLACK)
    screen.blit(banner, (width / 4, 0))

    # place images on the screen
    screen.blit(player, player_loc)
    screen.blit(beer, beer_loc)

    pygame.display.update()

    # Started?
    while pause:
        msg = font.render("Press any key to start", True, YELLOW, BLACK)
        screen.blit(msg, (width / 4, 100))
        pygame.display.update()
        for event in pygame.event.get():
            if event.type == pg.KEYDOWN:
                pause = False

    # Game over?
    if beer_loc[1] > height:
        msg = font2.render("GAME OVER", True, YELLOW, BLACK)
        screen.blit(msg, (width / 4, 100))
        pygame.display.update()
        wait_key = True
        while wait_key:
            for event in pygame.event.get():
                if event.type == pg.KEYDOWN:
                    wait_key = running = False
        pygame.quit()

pygame.quit()
