import pygame
import random
import Deckofcards, Pebbles, Drawings, Board
from pygame.locals import *
import pygame.gfxdraw

pygame.init()

SCREEN_WIDTH = 1280
SCREEN_HEIGHT = 800

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

# Colors
white = (255, 255, 255)
dark_white = (200, 200, 200, 128)
black = (0, 0, 0)
red = (255, 0, 0)
green = (0, 150, 0)

# Turn
turn = 1
move_done = False

# Cards
d = Deckofcards.Deck()
deck = d.create_deck()

p1_hand = []
p2_hand = []
full_hand = True
discard_round = 0

for x in range(8):
    random.shuffle(deck)
    p1_hand.append(deck.pop())
    p2_hand.append(deck.pop())


def takeName(elem):
    return elem.name


p1_hand.sort(key=takeName)
p2_hand.sort(key=takeName)

bg = pygame.image.load("Grafika/Board.png")
mm = pygame.image.load("Grafika/Main_Menu.png")
rl = pygame.image.load("Grafika/Rules.png")

myfont = pygame.font.SysFont('Kurri.ttf', 30)


def text_objects(text, font):
    textSurface = font.render(text, True, black)
    return textSurface, textSurface.get_rect()


def drawDiscard(discard, x):
    path = 'Grafika/Pebbles/' + discard[0].name + '.png'
    name = Pebbles.Pebble(x, 300, path)
    all_sprites.add(name)


def drawHighlights(highlights):
    for pos in highlights:
        x = pos[0]
        y = pos[1]
        pygame.draw.rect(screen, green, pygame.Rect(x, y, 70, 70), 3)


def drawChoices(choices):
    for pos in choices:
        if pos == 'Y':
            if turn == 1:
                if not deposit_yellow_p1 or p1_hand[indexes[0]].value >= deposit_yellow_p1[-1].value:
                    pygame.draw.rect(screen, green, pygame.Rect(36, 428, 220, 280), 3)
                pygame.draw.rect(screen, green, pygame.Rect(40, 197, 212, 210), 3)
            if turn == 2:
                if not deposit_yellow_p2 or p2_hand[indexes[0]].value >= deposit_yellow_p2[-1].value:
                    pygame.draw.rect(screen, green, pygame.Rect(36, 428, 220, 280), 3)
                pygame.draw.rect(screen, green, pygame.Rect(40, 197, 212, 210), 3)
        elif pos == 'B':
            if turn == 1:
                if not deposit_blue_p1 or p1_hand[indexes[0]].value >= deposit_blue_p1[-1].value:
                    pygame.draw.rect(screen, green, pygame.Rect(286, 428, 220, 280), 3)
                pygame.draw.rect(screen, green, pygame.Rect(290, 197, 212, 210), 3)
            if turn == 2:
                if not deposit_blue_p2 or p2_hand[indexes[0]].value >= deposit_blue_p2[-1].value:
                    pygame.draw.rect(screen, green, pygame.Rect(286, 428, 220, 280), 3)
                pygame.draw.rect(screen, green, pygame.Rect(290, 197, 212, 210), 3)
        elif pos == 'W':
            if turn == 1:
                if not deposit_white_p1 or p1_hand[indexes[0]].value >= deposit_white_p1[-1].value:
                    pygame.draw.rect(screen, green, pygame.Rect(536, 428, 220, 280), 3)
                pygame.draw.rect(screen, green, pygame.Rect(540, 197, 212, 210), 3)
            if turn == 2:
                if not deposit_white_p2 or p2_hand[indexes[0]].value >= deposit_white_p2[-1].value:
                    pygame.draw.rect(screen, green, pygame.Rect(536, 428, 220, 280), 3)
                pygame.draw.rect(screen, green, pygame.Rect(540, 197, 212, 210), 3)
        elif pos == 'G':
            if turn == 1:
                if not deposit_green_p1 or p1_hand[indexes[0]].value >= deposit_green_p1[-1].value:
                    pygame.draw.rect(screen, green, pygame.Rect(786, 428, 220, 280), 3)
                pygame.draw.rect(screen, green, pygame.Rect(790, 197, 212, 210), 3)
            if turn == 2:
                if not deposit_green_p2 or p2_hand[indexes[0]].value >= deposit_green_p2[-1].value:
                    pygame.draw.rect(screen, green, pygame.Rect(786, 428, 220, 280), 3)
                pygame.draw.rect(screen, green, pygame.Rect(790, 197, 212, 210), 3)
        elif pos == 'R':
            if turn == 1:
                if not deposit_red_p1 or p1_hand[indexes[0]].value >= deposit_red_p1[-1].value:
                    pygame.draw.rect(screen, green, pygame.Rect(1024, 428, 220, 280), 3)
                pygame.draw.rect(screen, green, pygame.Rect(1028, 197, 212, 210), 3)
            if turn == 2:
                if not deposit_red_p2 or p2_hand[indexes[0]].value >= deposit_red_p2[-1].value:
                    pygame.draw.rect(screen, green, pygame.Rect(1024, 428, 220, 280), 3)
                pygame.draw.rect(screen, green, pygame.Rect(1028, 197, 212, 210), 3)


highlights = []
choices = []
indexes = []

p1_score, p2_score = 0, 0
p1_yellow_score, p1_blue_score, p1_white_score, p1_green_score, p1_red_score = 0, 0, 0, 0, 0
p2_yellow_score, p2_blue_score, p2_white_score, p2_green_score, p2_red_score = 0, 0, 0, 0, 0
yellow_dollars_p1, blue_dollars_p1, white_dollars_p1, green_dollars_p1, red_dollars_p1 = 1, 1, 1, 1, 1
yellow_dollars_p2, blue_dollars_p2, white_dollars_p2, green_dollars_p2, red_dollars_p2 = 1, 1, 1, 1, 1

discard_yellow = []
discard_blue = []
discard_white = []
discard_green = []
discard_red = []

deposit_yellow_p1 = []
deposit_blue_p1 = []
deposit_white_p1 = []
deposit_green_p1 = []
deposit_red_p1 = []

deposit_yellow_p2 = []
deposit_blue_p2 = []
deposit_white_p2 = []
deposit_green_p2 = []
deposit_red_p2 = []

# Main Menu
intro = True
hotseat = False
rules = False
si = False

while intro:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            intro = False

    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()

    screen.fill((0, 0, 0))
    screen.blit(mm, (0, 0))

    largeText = pygame.font.Font('Kurri.ttf', 20)
    Button_1, Button_1_rect = text_objects("Gorące Krzesło", largeText)
    Button_1_rect.center = (770, 158)
    Button_2, Button_2_rect = text_objects("SI", largeText)
    Button_2_rect.center = (770, 233)
    Button_3, Button_3_rect = text_objects("Zasady", largeText)
    Button_3_rect.center = (770, 308)
    Button_4, Button_4_rect = text_objects("Wyjście", largeText)
    Button_4_rect.center = (770, 383)
    screen.blit(Button_1, Button_1_rect)
    screen.blit(Button_2, Button_2_rect)
    screen.blit(Button_3, Button_3_rect)
    screen.blit(Button_4, Button_4_rect)

    if 690 <= mouse[0] <= 850 and 138 <= mouse[1] <= 178:
        pygame.gfxdraw.box(screen, [690, 138, 160, 40], dark_white)
        if click[0] == 1:
            intro = False
            hotseat = True

    if 690 <= mouse[0] <= 850 and 213 <= mouse[1] <= 253:
        pygame.gfxdraw.box(screen, [690, 213, 160, 40], dark_white)
        if click[0] == 1:
            intro = False
            si = True

    if 690 <= mouse[0] <= 850 and 288 <= mouse[1] <= 328:
        pygame.gfxdraw.box(screen, [690, 288, 160, 40], dark_white)
        if click[0] == 1:
            rules = True

    if 690 <= mouse[0] <= 850 and 363 <= mouse[1] <= 403:
        pygame.gfxdraw.box(screen, [690, 363, 160, 40], dark_white)
        if click[0] == 1:
            intro = False
            hotseat = False

    pygame.display.flip()

    while rules:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                rules = False

        mouse = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()

        screen.fill((0, 0, 0))
        screen.blit(rl, (0, 0))

        largeText = pygame.font.Font('Kurri.ttf', 20)
        Button_1, Button_1_rect = text_objects("Powrót", largeText)
        Button_1_rect.center = (1060, 700)

        if 980 <= mouse[0] <= 1130 and 680 <= mouse[1] <= 720:
            pygame.gfxdraw.box(screen, [980, 680, 160, 40], dark_white)
            if click[0] == 1:
                rules = False

        screen.blit(Button_1, Button_1_rect)

        pygame.display.flip()


while hotseat:

    all_sprites = pygame.sprite.Group()

    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()

    # Did the user click the window close button?
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            hotseat = False
        if event.type == KEYDOWN:
            if event.key == K_ESCAPE:
                choices.clear()
                indexes.clear()
                highlights.clear()

    # Fill the background with white
    screen.fill((0, 0, 0))

    # Draw a background image
    screen.blit(bg, (0, 0))

    # Obliczanie i wyświetlanie ile zostało kart do końca
    cards_left = len(deck)
    cards_left_text = 'Pozostało kart: ' + str(cards_left)
    turnsurface = myfont.render(cards_left_text, True, white)

    whose_turn = 'Tura Gracza ' + str(turn)
    whoseturnsurface = myfont.render(whose_turn, True, white)

    # Turn Text
    screen.blit(turnsurface, (320, 20))
    screen.blit(whoseturnsurface, (120, 20))

    if turn == 1:
        # Drawing Cards
        i = 345
        for x in p1_hand:
            path = 'Grafika/Pebbles/' + x.name + '.png'
            name = Pebbles.Pebble(i, 755, path)
            all_sprites.add(name)
            i = i + 85

        if deposit_yellow_p1:
            Drawings.drawDeposit(deposit_yellow_p1, 80, all_sprites)
        if deposit_blue_p1:
            Drawings.drawDeposit(deposit_blue_p1, 330, all_sprites)
        if deposit_white_p1:
            Drawings.drawDeposit(deposit_white_p1, 580, all_sprites)
        if deposit_green_p1:
            Drawings.drawDeposit(deposit_green_p1, 830, all_sprites)
        if deposit_red_p1:
            Drawings.drawDeposit(deposit_red_p1, 1070, all_sprites)

        if deposit_yellow_p2:
            Drawings.drawOpponentDeposit(deposit_yellow_p2, 80, all_sprites)
        if deposit_blue_p2:
            Drawings.drawOpponentDeposit(deposit_blue_p2, 330, all_sprites)
        if deposit_white_p2:
            Drawings.drawOpponentDeposit(deposit_white_p2, 580, all_sprites)
        if deposit_green_p2:
            Drawings.drawOpponentDeposit(deposit_green_p2, 830, all_sprites)
        if deposit_red_p2:
            Drawings.drawOpponentDeposit(deposit_red_p2, 1070, all_sprites)

        if full_hand == False:
            if 250 > mouse[0] > 45 and 400 > mouse[1] > 200 and discard_yellow and discard_round != 'Y':
                pygame.draw.rect(screen, white, pygame.Rect(40, 197, 212, 210), 3)
                if click[0] == 1:
                    tmp = discard_yellow.pop(0)
                    p1_hand.append(tmp)
                    p1_hand.sort(key=takeName)
                    full_hand = True
            elif 500 > mouse[0] > 295 and 400 > mouse[1] > 200 and discard_blue and discard_round != 'B':
                pygame.draw.rect(screen, white, pygame.Rect(290, 197, 212, 210), 3)
                if click[0] == 1:
                    tmp = discard_blue.pop(0)
                    p1_hand.append(tmp)
                    p1_hand.sort(key=takeName)
                    full_hand = True
            elif 750 > mouse[0] > 545 and 400 > mouse[1] > 200 and discard_white and discard_round != 'W':
                pygame.draw.rect(screen, white, pygame.Rect(540, 197, 212, 210), 3)
                if click[0] == 1:
                    tmp = discard_white.pop(0)
                    p1_hand.append(tmp)
                    p1_hand.sort(key=takeName)
                    full_hand = True
            elif 1000 > mouse[0] > 795 and 400 > mouse[1] > 200 and discard_green and discard_round != 'G':
                pygame.draw.rect(screen, white, pygame.Rect(790, 197, 212, 210), 3)
                if click[0] == 1:
                    tmp = discard_green.pop(0)
                    p1_hand.append(tmp)
                    p1_hand.sort(key=takeName)
                    full_hand = True
            elif 1250 > mouse[0] > 1045 and 400 > mouse[1] > 200 and discard_red and discard_round != 'R':
                pygame.draw.rect(screen, white, pygame.Rect(1028, 197, 212, 210), 3)
                if click[0] == 1:
                    tmp = discard_red.pop(0)
                    p1_hand.append(tmp)
                    p1_hand.sort(key=takeName)
                    full_hand = True

        if move_done == False:
            # Highlighting player's cards
            Drawings.draw(375, 315, 310, p1_hand[0].color, 0, mouse, click, highlights, choices, indexes, screen)
            Drawings.draw(460, 400, 395, p1_hand[1].color, 1, mouse, click, highlights, choices, indexes, screen)
            Drawings.draw(545, 485, 480, p1_hand[2].color, 2, mouse, click, highlights, choices, indexes, screen)
            Drawings.draw(630, 570, 565, p1_hand[3].color, 3, mouse, click, highlights, choices, indexes, screen)
            Drawings.draw(715, 655, 650, p1_hand[4].color, 4, mouse, click, highlights, choices, indexes, screen)
            Drawings.draw(800, 740, 735, p1_hand[5].color, 5, mouse, click, highlights, choices, indexes, screen)
            Drawings.draw(885, 825, 820, p1_hand[6].color, 6, mouse, click, highlights, choices, indexes, screen)
            Drawings.draw(975, 915, 905, p1_hand[7].color, 7, mouse, click, highlights, choices, indexes, screen)

            # Move pebble
            if choices:
                if choices[0] == 'Y':
                    if 250 > mouse[0] > 45 and 400 > mouse[1] > 200 and click[0] == 1:
                        discard_yellow.insert(0, p1_hand.pop(indexes[0]))
                        choices.clear()
                        indexes.clear()
                        highlights.clear()
                        move_done = True
                        full_hand = False
                        discard_round = 'Y'

                elif choices[0] == 'B':
                    if 500 > mouse[0] > 295 and 400 > mouse[1] > 200 and click[0] == 1:
                        discard_blue.insert(0, p1_hand.pop(indexes[0]))
                        choices.clear()
                        indexes.clear()
                        highlights.clear()
                        move_done = True
                        full_hand = False
                        discard_round = 'B'

                elif choices[0] == 'W':
                    if 750 > mouse[0] > 545 and 400 > mouse[1] > 200 and click[0] == 1:
                        discard_white.insert(0, p1_hand.pop(indexes[0]))
                        choices.clear()
                        indexes.clear()
                        highlights.clear()
                        move_done = True
                        full_hand = False
                        discard_round = 'W'

                elif choices[0] == 'G':
                    if 1000 > mouse[0] > 795 and 400 > mouse[1] > 200 and click[0] == 1:
                        discard_green.insert(0, p1_hand.pop(indexes[0]))
                        choices.clear()
                        indexes.clear()
                        highlights.clear()
                        move_done = True
                        full_hand = False
                        discard_round = 'G'

                elif choices[0] == 'R':
                    if 1250 > mouse[0] > 1045 and 400 > mouse[1] > 200 and click[0] == 1:
                        discard_red.insert(0, p1_hand.pop(indexes[0]))
                        choices.clear()
                        indexes.clear()
                        highlights.clear()
                        move_done = True
                        full_hand = False
                        discard_round = 'R'

            # Drawing deposit
            if choices:
                if choices[0] == 'Y':
                    if not deposit_yellow_p1 or p1_hand[indexes[0]].value >= deposit_yellow_p1[-1].value:
                        if 250 > mouse[0] > 45 and 700 > mouse[1] > 435 and click[0] == 1:
                            if not deposit_yellow_p1:
                                p1_yellow_score = -20
                            if p1_hand[indexes[0]].value == 0:
                                yellow_dollars_p1 = yellow_dollars_p1 + 1
                            p1_yellow_score = p1_yellow_score + p1_hand[indexes[0]].value
                            deposit_yellow_p1.append(p1_hand.pop(indexes[0]))
                            choices.clear()
                            indexes.clear()
                            highlights.clear()
                            move_done = True
                            full_hand = False

                elif choices[0] == 'B':
                    if not deposit_blue_p1 or p1_hand[indexes[0]].value >= deposit_blue_p1[-1].value:
                        if 500 > mouse[0] > 295 and 700 > mouse[1] > 435 and click[0] == 1:
                            if not deposit_blue_p1:
                                p1_blue_score = -20
                            if p1_hand[indexes[0]].value == 0:
                                blue_dollars_p1 = blue_dollars_p1 + 1
                            p1_blue_score = p1_blue_score + p1_hand[indexes[0]].value
                            deposit_blue_p1.append(p1_hand.pop(indexes[0]))
                            choices.clear()
                            indexes.clear()
                            highlights.clear()
                            move_done = True
                            full_hand = False

                elif choices[0] == 'W':
                    if not deposit_white_p1 or p1_hand[indexes[0]].value >= deposit_white_p1[-1].value:
                        if 750 > mouse[0] > 545 and 700 > mouse[1] > 435 and click[0] == 1:
                            if not deposit_white_p1:
                                p1_white_score = -20
                            if p1_hand[indexes[0]].value == 0:
                                white_dollars_p1 = white_dollars_p1 + 1
                            p1_white_score = p1_white_score + p1_hand[indexes[0]].value
                            deposit_white_p1.append(p1_hand.pop(indexes[0]))
                            choices.clear()
                            indexes.clear()
                            highlights.clear()
                            move_done = True
                            full_hand = False

                elif choices[0] == 'G':
                    if not deposit_green_p1 or p1_hand[indexes[0]].value >= deposit_green_p1[-1].value:
                        if 1000 > mouse[0] > 795 and 700 > mouse[1] > 435 and click[0] == 1:
                            if not deposit_green_p1:
                                p1_green_score = -20
                            if p1_hand[indexes[0]].value == 0:
                                green_dollars_p1 = green_dollars_p1 + 1
                            p1_green_score = p1_green_score + p1_hand[indexes[0]].value
                            deposit_green_p1.append(p1_hand.pop(indexes[0]))
                            choices.clear()
                            indexes.clear()
                            highlights.clear()
                            move_done = True
                            full_hand = False

                elif choices[0] == 'R':
                    if not deposit_red_p1 or p1_hand[indexes[0]].value >= deposit_red_p1[-1].value:
                        if 1250 > mouse[0] > 1045 and 700 > mouse[1] > 435 and click[0] == 1:
                            if not deposit_red_p1:
                                p1_red_score = -20
                            if p1_hand[indexes[0]].value == 0:
                                red_dollars_p1 = red_dollars_p1 + 1
                            p1_red_score = p1_red_score + p1_hand[indexes[0]].value
                            deposit_red_p1.append(p1_hand.pop(indexes[0]))
                            choices.clear()
                            indexes.clear()
                            highlights.clear()
                            move_done = True
                            full_hand = False

    if turn == 2:
        # Drawing Cards
        i = 345
        for x in p2_hand:
            path = 'Grafika/Pebbles/' + x.name + '.png'
            name = Pebbles.Pebble(i, 755, path)
            all_sprites.add(name)
            i = i+85

        if deposit_yellow_p2:
            Drawings.drawDeposit(deposit_yellow_p2, 80, all_sprites)
        if deposit_blue_p2:
            Drawings.drawDeposit(deposit_blue_p2, 330, all_sprites)
        if deposit_white_p2:
            Drawings.drawDeposit(deposit_white_p2, 580, all_sprites)
        if deposit_green_p2:
            Drawings.drawDeposit(deposit_green_p2, 830, all_sprites)
        if deposit_red_p2:
            Drawings.drawDeposit(deposit_red_p2, 1070, all_sprites)

        if deposit_yellow_p1:
            Drawings.drawOpponentDeposit(deposit_yellow_p1, 80, all_sprites)
        if deposit_blue_p1:
            Drawings.drawOpponentDeposit(deposit_blue_p1, 330, all_sprites)
        if deposit_white_p1:
            Drawings.drawOpponentDeposit(deposit_white_p1, 580, all_sprites)
        if deposit_green_p1:
            Drawings.drawOpponentDeposit(deposit_green_p1, 830, all_sprites)
        if deposit_red_p1:
            Drawings.drawOpponentDeposit(deposit_red_p1, 1070, all_sprites)

        if full_hand == False:
            if 250 > mouse[0] > 45 and 400 > mouse[1] > 200 and discard_yellow and discard_round != 'Y':
                pygame.draw.rect(screen, white, pygame.Rect(40, 197, 212, 210), 3)
                if click[0] == 1:
                    tmp = discard_yellow.pop(0)
                    p2_hand.append(tmp)
                    p2_hand.sort(key=takeName)
                    full_hand = True
            elif 500 > mouse[0] > 295 and 400 > mouse[1] > 200 and discard_blue and discard_round != 'B':
                pygame.draw.rect(screen, white, pygame.Rect(290, 197, 212, 210), 3)
                if click[0] == 1:
                    tmp = discard_blue.pop(0)
                    p2_hand.append(tmp)
                    p2_hand.sort(key=takeName)
                    full_hand = True
            elif 750 > mouse[0] > 545 and 400 > mouse[1] > 200 and discard_white and discard_round != 'W':
                pygame.draw.rect(screen, white, pygame.Rect(540, 197, 212, 210), 3)
                if click[0] == 1:
                    tmp = discard_white.pop(0)
                    p2_hand.append(tmp)
                    p2_hand.sort(key=takeName)
                    full_hand = True
            elif 1000 > mouse[0] > 795 and 400 > mouse[1] > 200 and discard_green and discard_round != 'G':
                pygame.draw.rect(screen, white, pygame.Rect(790, 197, 212, 210), 3)
                if click[0] == 1:
                    tmp = discard_green.pop(0)
                    p2_hand.append(tmp)
                    p2_hand.sort(key=takeName)
                    full_hand = True
            elif 1250 > mouse[0] > 1045 and 400 > mouse[1] > 200 and discard_red and discard_round != 'R':
                pygame.draw.rect(screen, white, pygame.Rect(1028, 197, 212, 210), 3)
                if click[0] == 1:
                    tmp = discard_red.pop(0)
                    p2_hand.append(tmp)
                    p2_hand.sort(key=takeName)
                    full_hand = True

        if move_done == False:
            # Highlighting player's cards
            Drawings.draw(375, 315, 310, p2_hand[0].color, 0, mouse, click, highlights, choices, indexes, screen)
            Drawings.draw(460, 400, 395, p2_hand[1].color, 1, mouse, click, highlights, choices, indexes, screen)
            Drawings.draw(545, 485, 480, p2_hand[2].color, 2, mouse, click, highlights, choices, indexes, screen)
            Drawings.draw(630, 570, 565, p2_hand[3].color, 3, mouse, click, highlights, choices, indexes, screen)
            Drawings.draw(715, 655, 650, p2_hand[4].color, 4, mouse, click, highlights, choices, indexes, screen)
            Drawings.draw(800, 740, 735, p2_hand[5].color, 5, mouse, click, highlights, choices, indexes, screen)
            Drawings.draw(885, 825, 820, p2_hand[6].color, 6, mouse, click, highlights, choices, indexes, screen)
            Drawings.draw(975, 915, 905, p2_hand[7].color, 7, mouse, click, highlights, choices, indexes, screen)

            # Move pebble
            if choices:
                if choices[0] == 'Y':
                    if 250 > mouse[0] > 45 and 400 > mouse[1] > 200 and click[0] == 1:
                        discard_yellow.insert(0, p2_hand.pop(indexes[0]))
                        choices.clear()
                        indexes.clear()
                        highlights.clear()
                        move_done = True
                        full_hand = False
                        discard_round = 'Y'

                elif choices[0] == 'B':
                    if 500 > mouse[0] > 295 and 400 > mouse[1] > 200 and click[0] == 1:
                        discard_blue.insert(0, p2_hand.pop(indexes[0]))
                        choices.clear()
                        indexes.clear()
                        highlights.clear()
                        move_done = True
                        full_hand = False
                        discard_round = 'B'

                elif choices[0] == 'W':
                    if 750 > mouse[0] > 545 and 400 > mouse[1] > 200 and click[0] == 1:
                        discard_white.insert(0, p2_hand.pop(indexes[0]))
                        choices.clear()
                        indexes.clear()
                        highlights.clear()
                        move_done = True
                        full_hand = False
                        discard_round = 'W'

                elif choices[0] == 'G':
                    if 1000 > mouse[0] > 795 and 400 > mouse[1] > 200 and click[0] == 1:
                        discard_green.insert(0, p2_hand.pop(indexes[0]))
                        choices.clear()
                        indexes.clear()
                        highlights.clear()
                        move_done = True
                        full_hand = False
                        discard_round = 'G'

                elif choices[0] == 'R':
                    if 1250 > mouse[0] > 1045 and 400 > mouse[1] > 200 and click[0] == 1:
                        discard_red.insert(0, p2_hand.pop(indexes[0]))
                        choices.clear()
                        indexes.clear()
                        highlights.clear()
                        move_done = True
                        full_hand = False
                        discard_round = 'R'

            # Drawing deposit
            if choices:
                if choices[0] == 'Y':
                    if not deposit_yellow_p2 or p2_hand[indexes[0]].value >= deposit_yellow_p2[-1].value:
                        if 250 > mouse[0] > 45 and 700 > mouse[1] > 435 and click[0] == 1:
                            if not deposit_yellow_p2:
                                p2_yellow_score = -20
                            if p2_hand[indexes[0]].value == 0:
                                yellow_dollars_p2 = yellow_dollars_p2 + 1
                            p2_yellow_score = p2_yellow_score + p2_hand[indexes[0]].value
                            deposit_yellow_p2.append(p2_hand.pop(indexes[0]))
                            choices.clear()
                            indexes.clear()
                            highlights.clear()
                            move_done = True
                            full_hand = False

                elif choices[0] == 'B':
                    if not deposit_blue_p2 or p2_hand[indexes[0]].value >= deposit_blue_p2[-1].value:
                        if 500 > mouse[0] > 295 and 700 > mouse[1] > 435 and click[0] == 1:
                            if not deposit_blue_p2:
                                p2_blue_score = -20
                            if p2_hand[indexes[0]].value == 0:
                                blue_dollars_p2 = blue_dollars_p2 + 1
                            p2_blue_score = p2_blue_score + p2_hand[indexes[0]].value
                            deposit_blue_p2.append(p2_hand.pop(indexes[0]))
                            choices.clear()
                            indexes.clear()
                            highlights.clear()
                            move_done = True
                            full_hand = False

                elif choices[0] == 'W':
                    if not deposit_white_p2 or p2_hand[indexes[0]].value >= deposit_white_p2[-1].value:
                        if 750 > mouse[0] > 545 and 700 > mouse[1] > 435 and click[0] == 1:
                            if not deposit_white_p2:
                                p2_white_score = -20
                            if p2_hand[indexes[0]].value == 0:
                                white_dollars_p2 = white_dollars_p2 + 1
                            p2_white_score = p2_white_score + p2_hand[indexes[0]].value
                            deposit_white_p2.append(p2_hand.pop(indexes[0]))
                            choices.clear()
                            indexes.clear()
                            highlights.clear()
                            move_done = True
                            full_hand = False

                elif choices[0] == 'G':
                    if not deposit_green_p2 or p2_hand[indexes[0]].value >= deposit_green_p2[-1].value:
                        if 1000 > mouse[0] > 795 and 700 > mouse[1] > 435 and click[0] == 1:
                            if not deposit_green_p2:
                                p2_green_score = -20
                            if p2_hand[indexes[0]].value == 0:
                                green_dollars_p2 = green_dollars_p2 + 1
                            p2_green_score = p2_green_score + p2_hand[indexes[0]].value
                            deposit_green_p2.append(p2_hand.pop(indexes[0]))
                            choices.clear()
                            indexes.clear()
                            highlights.clear()
                            move_done = True
                            full_hand = False

                elif choices[0] == 'R':
                    if not deposit_red_p2 or p2_hand[indexes[0]].value >= deposit_red_p2[-1].value:
                        if 1250 > mouse[0] > 1045 and 700 > mouse[1] > 435 and click[0] == 1:
                            if not deposit_red_p2:
                                p2_red_score = -20
                            if p2_hand[indexes[0]].value == 0:
                                red_dollars_p2 = red_dollars_p2 + 1
                            p2_red_score = p2_red_score + p2_hand[indexes[0]].value
                            deposit_red_p2.append(p2_hand.pop(indexes[0]))
                            choices.clear()
                            indexes.clear()
                            highlights.clear()
                            move_done = True
                            full_hand = False

    # Next round button
    if 1205 > mouse[0] > 1060 and 790 > mouse[1] > 720 and move_done and full_hand:
        pygame.draw.rect(screen, white, pygame.Rect(1055, 715, 160, 75), 3)
        if click[0] == 1:
            if turn == 1:
                turn = 2
                move_done = False
                discard_round = 0
            elif turn == 2:
                turn = 1
                move_done = False
                discard_round = 0

    # Exit button
    if 1275 > mouse[0] > 1235 and 46 > mouse[1] > 6 and click[0] == 1:
        hotseat = False

    # Draw card button
    if move_done and 220 > mouse[0] > 70 and 790 > mouse[1] > 720 and full_hand == False:
        pygame.draw.rect(screen, white, pygame.Rect(65, 715, 160, 75), 3)
        if click[0] == 1:
            if turn == 1:
                p1_hand.append(deck.pop())
                p1_hand.sort(key=takeName)
                full_hand = True
            elif turn == 2:
                p2_hand.append(deck.pop())
                p2_hand.sort(key=takeName)
                full_hand = True

    # Drawing
    if discard_yellow:
        drawDiscard(discard_yellow, 150)
    if discard_blue:
        drawDiscard(discard_blue, 400)
    if discard_white:
        drawDiscard(discard_white, 650)
    if discard_green:
        drawDiscard(discard_green, 900)
    if discard_red:
        drawDiscard(discard_red, 1140)

    drawChoices(choices)
    drawHighlights(highlights)
    all_sprites.update()
    all_sprites.draw(screen)

    # Flip the display
    pygame.display.flip()

    if cards_left == 0:
        scoreboard = True

        p1_yellow_score = p1_yellow_score * yellow_dollars_p1
        if len(deposit_yellow_p1) > 7:
            p1_yellow_score = p1_yellow_score + 20
        p1_blue_score = p1_blue_score * blue_dollars_p1
        if len(deposit_blue_p1) > 7:
            p1_blue_score = p1_blue_score + 20
        p1_white_score = p1_white_score * white_dollars_p1
        if len(deposit_white_p1) > 7:
            p1_white_score = p1_white_score + 20
        p1_green_score = p1_green_score * green_dollars_p1
        if len(deposit_green_p1) > 7:
            p1_green_score = p1_green_score + 20
        p1_red_score = p1_red_score * red_dollars_p1
        if len(deposit_red_p1) > 7:
            p1_red_score = p1_red_score + 20

        p2_yellow_score = p2_yellow_score * yellow_dollars_p2
        if len(deposit_yellow_p2) > 7:
            p2_yellow_score = p2_yellow_score + 20
        p2_blue_score = p2_blue_score * blue_dollars_p2
        if len(deposit_blue_p2) > 7:
            p2_blue_score = p2_blue_score + 20
        p2_white_score = p2_white_score * white_dollars_p2
        if len(deposit_white_p2) > 7:
            p2_white_score = p2_white_score + 20
        p2_green_score = p2_green_score * green_dollars_p2
        if len(deposit_green_p2) > 7:
            p2_green_score = p2_green_score + 20
        p2_red_score = p2_red_score * red_dollars_p2
        if len(deposit_red_p2) > 7:
            p2_red_score = p2_red_score + 20

        p1_score = p1_yellow_score + p1_blue_score + p1_white_score + p1_green_score + p1_red_score
        p2_score = p2_yellow_score + p2_blue_score + p2_white_score + p2_green_score + p2_red_score

        while scoreboard:

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    scoreboard = False
                    hotseat = False

            screen.fill(black)

            if p1_score > p2_score:
                score_text = 'Wygrywa Gracz 1! Miał ' + str(p1_score) + ' punktów. Przeciwnik miał ' + str(p2_score) + ' punktów!'
                scoresurface = myfont.render(score_text, True, white)
            elif p2_score > p1_score:
                score_text = 'Wygrywa Gracz 2! Miał ' + str(p2_score) + ' punktów. Przeciwnik miał ' + str(p1_score) + ' punktów!'
                scoresurface = myfont.render(score_text, True, white)
            elif p1_score == p2_score:
                score_text = 'Remis! ' + str(p1_score) + ' punktów miał każdy z graczy.'
                scoresurface = myfont.render(score_text, True, white)

            screen.blit(scoresurface, (280, 400))

            pygame.display.flip()

while si:

    all_sprites = pygame.sprite.Group()

    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()

    # Did the user click the window close button?
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            si = False
        if event.type == KEYDOWN:
            if event.key == K_ESCAPE:
                choices.clear()
                indexes.clear()
                highlights.clear()

    # Fill the background with white
    screen.fill((0, 0, 0))

    # Draw a background image
    screen.blit(bg, (0, 0))

    # Obliczanie i wyświetlanie ile zostało kart do końca
    cards_left = len(deck)
    cards_left_text = 'Pozostało kart: ' + str(cards_left)
    turnsurface = myfont.render(cards_left_text, True, white)

    whose_turn = 'Tura Gracza ' + str(turn)
    whoseturnsurface = myfont.render(whose_turn, True, white)

    # Turn Text
    screen.blit(turnsurface, (320, 20))
    screen.blit(whoseturnsurface, (120, 20))

    if turn == 1:
        # Drawing Cards
        i = 345
        for x in p1_hand:
            path = 'Grafika/Pebbles/' + x.name + '.png'
            name = Pebbles.Pebble(i, 755, path)
            all_sprites.add(name)
            i = i + 85

        if deposit_yellow_p1:
            Drawings.drawDeposit(deposit_yellow_p1, 80, all_sprites)
        if deposit_blue_p1:
            Drawings.drawDeposit(deposit_blue_p1, 330, all_sprites)
        if deposit_white_p1:
            Drawings.drawDeposit(deposit_white_p1, 580, all_sprites)
        if deposit_green_p1:
            Drawings.drawDeposit(deposit_green_p1, 830, all_sprites)
        if deposit_red_p1:
            Drawings.drawDeposit(deposit_red_p1, 1070, all_sprites)

        if deposit_yellow_p2:
            Drawings.drawOpponentDeposit(deposit_yellow_p2, 80, all_sprites)
        if deposit_blue_p2:
            Drawings.drawOpponentDeposit(deposit_blue_p2, 330, all_sprites)
        if deposit_white_p2:
            Drawings.drawOpponentDeposit(deposit_white_p2, 580, all_sprites)
        if deposit_green_p2:
            Drawings.drawOpponentDeposit(deposit_green_p2, 830, all_sprites)
        if deposit_red_p2:
            Drawings.drawOpponentDeposit(deposit_red_p2, 1070, all_sprites)

        if full_hand == False:
            if 250 > mouse[0] > 45 and 400 > mouse[1] > 200 and discard_yellow and discard_round != 'Y':
                pygame.draw.rect(screen, white, pygame.Rect(40, 197, 212, 210), 3)
                if click[0] == 1:
                    tmp = discard_yellow.pop(0)
                    p1_hand.append(tmp)
                    p1_hand.sort(key=takeName)
                    full_hand = True
            elif 500 > mouse[0] > 295 and 400 > mouse[1] > 200 and discard_blue and discard_round != 'B':
                pygame.draw.rect(screen, white, pygame.Rect(290, 197, 212, 210), 3)
                if click[0] == 1:
                    tmp = discard_blue.pop(0)
                    p1_hand.append(tmp)
                    p1_hand.sort(key=takeName)
                    full_hand = True
            elif 750 > mouse[0] > 545 and 400 > mouse[1] > 200 and discard_white and discard_round != 'W':
                pygame.draw.rect(screen, white, pygame.Rect(540, 197, 212, 210), 3)
                if click[0] == 1:
                    tmp = discard_white.pop(0)
                    p1_hand.append(tmp)
                    p1_hand.sort(key=takeName)
                    full_hand = True
            elif 1000 > mouse[0] > 795 and 400 > mouse[1] > 200 and discard_green and discard_round != 'G':
                pygame.draw.rect(screen, white, pygame.Rect(790, 197, 212, 210), 3)
                if click[0] == 1:
                    tmp = discard_green.pop(0)
                    p1_hand.append(tmp)
                    p1_hand.sort(key=takeName)
                    full_hand = True
            elif 1250 > mouse[0] > 1045 and 400 > mouse[1] > 200 and discard_red and discard_round != 'R':
                pygame.draw.rect(screen, white, pygame.Rect(1028, 197, 212, 210), 3)
                if click[0] == 1:
                    tmp = discard_red.pop(0)
                    p1_hand.append(tmp)
                    p1_hand.sort(key=takeName)
                    full_hand = True

        if move_done == False:
            # Highlighting player's cards
            Drawings.draw(375, 315, 310, p1_hand[0].color, 0, mouse, click, highlights, choices, indexes, screen)
            Drawings.draw(460, 400, 395, p1_hand[1].color, 1, mouse, click, highlights, choices, indexes, screen)
            Drawings.draw(545, 485, 480, p1_hand[2].color, 2, mouse, click, highlights, choices, indexes, screen)
            Drawings.draw(630, 570, 565, p1_hand[3].color, 3, mouse, click, highlights, choices, indexes, screen)
            Drawings.draw(715, 655, 650, p1_hand[4].color, 4, mouse, click, highlights, choices, indexes, screen)
            Drawings.draw(800, 740, 735, p1_hand[5].color, 5, mouse, click, highlights, choices, indexes, screen)
            Drawings.draw(885, 825, 820, p1_hand[6].color, 6, mouse, click, highlights, choices, indexes, screen)
            Drawings.draw(975, 915, 905, p1_hand[7].color, 7, mouse, click, highlights, choices, indexes, screen)

            # Move pebble
            if choices:
                if choices[0] == 'Y':
                    if 250 > mouse[0] > 45 and 400 > mouse[1] > 200 and click[0] == 1:
                        discard_yellow.insert(0, p1_hand.pop(indexes[0]))
                        choices.clear()
                        indexes.clear()
                        highlights.clear()
                        move_done = True
                        full_hand = False
                        discard_round = 'Y'

                elif choices[0] == 'B':
                    if 500 > mouse[0] > 295 and 400 > mouse[1] > 200 and click[0] == 1:
                        discard_blue.insert(0, p1_hand.pop(indexes[0]))
                        choices.clear()
                        indexes.clear()
                        highlights.clear()
                        move_done = True
                        full_hand = False
                        discard_round = 'B'

                elif choices[0] == 'W':
                    if 750 > mouse[0] > 545 and 400 > mouse[1] > 200 and click[0] == 1:
                        discard_white.insert(0, p1_hand.pop(indexes[0]))
                        choices.clear()
                        indexes.clear()
                        highlights.clear()
                        move_done = True
                        full_hand = False
                        discard_round = 'W'

                elif choices[0] == 'G':
                    if 1000 > mouse[0] > 795 and 400 > mouse[1] > 200 and click[0] == 1:
                        discard_green.insert(0, p1_hand.pop(indexes[0]))
                        choices.clear()
                        indexes.clear()
                        highlights.clear()
                        move_done = True
                        full_hand = False
                        discard_round = 'G'

                elif choices[0] == 'R':
                    if 1250 > mouse[0] > 1045 and 400 > mouse[1] > 200 and click[0] == 1:
                        discard_red.insert(0, p1_hand.pop(indexes[0]))
                        choices.clear()
                        indexes.clear()
                        highlights.clear()
                        move_done = True
                        full_hand = False
                        discard_round = 'R'

            # Drawing deposit
            if choices:
                if choices[0] == 'Y':
                    if not deposit_yellow_p1 or p1_hand[indexes[0]].value >= deposit_yellow_p1[-1].value:
                        if 250 > mouse[0] > 45 and 700 > mouse[1] > 435 and click[0] == 1:
                            if not deposit_yellow_p1:
                                p1_yellow_score = -20
                            if p1_hand[indexes[0]].value == 0:
                                yellow_dollars_p1 = yellow_dollars_p1 + 1
                            p1_yellow_score = p1_yellow_score + p1_hand[indexes[0]].value
                            deposit_yellow_p1.append(p1_hand.pop(indexes[0]))
                            choices.clear()
                            indexes.clear()
                            highlights.clear()
                            move_done = True
                            full_hand = False

                elif choices[0] == 'B':
                    if not deposit_blue_p1 or p1_hand[indexes[0]].value >= deposit_blue_p1[-1].value:
                        if 500 > mouse[0] > 295 and 700 > mouse[1] > 435 and click[0] == 1:
                            if not deposit_blue_p1:
                                p1_blue_score = -20
                            if p1_hand[indexes[0]].value == 0:
                                blue_dollars_p1 = blue_dollars_p1 + 1
                            p1_blue_score = p1_blue_score + p1_hand[indexes[0]].value
                            deposit_blue_p1.append(p1_hand.pop(indexes[0]))
                            choices.clear()
                            indexes.clear()
                            highlights.clear()
                            move_done = True
                            full_hand = False

                elif choices[0] == 'W':
                    if not deposit_white_p1 or p1_hand[indexes[0]].value >= deposit_white_p1[-1].value:
                        if 750 > mouse[0] > 545 and 700 > mouse[1] > 435 and click[0] == 1:
                            if not deposit_white_p1:
                                p1_white_score = -20
                            if p1_hand[indexes[0]].value == 0:
                                white_dollars_p1 = white_dollars_p1 + 1
                            p1_white_score = p1_white_score + p1_hand[indexes[0]].value
                            deposit_white_p1.append(p1_hand.pop(indexes[0]))
                            choices.clear()
                            indexes.clear()
                            highlights.clear()
                            move_done = True
                            full_hand = False

                elif choices[0] == 'G':
                    if not deposit_green_p1 or p1_hand[indexes[0]].value >= deposit_green_p1[-1].value:
                        if 1000 > mouse[0] > 795 and 700 > mouse[1] > 435 and click[0] == 1:
                            if not deposit_green_p1:
                                p1_green_score = -20
                            if p1_hand[indexes[0]].value == 0:
                                green_dollars_p1 = green_dollars_p1 + 1
                            p1_green_score = p1_green_score + p1_hand[indexes[0]].value
                            deposit_green_p1.append(p1_hand.pop(indexes[0]))
                            choices.clear()
                            indexes.clear()
                            highlights.clear()
                            move_done = True
                            full_hand = False

                elif choices[0] == 'R':
                    if not deposit_red_p1 or p1_hand[indexes[0]].value >= deposit_red_p1[-1].value:
                        if 1250 > mouse[0] > 1045 and 700 > mouse[1] > 435 and click[0] == 1:
                            if not deposit_red_p1:
                                p1_red_score = -20
                            if p1_hand[indexes[0]].value == 0:
                                red_dollars_p1 = red_dollars_p1 + 1
                            p1_red_score = p1_red_score + p1_hand[indexes[0]].value
                            deposit_red_p1.append(p1_hand.pop(indexes[0]))
                            choices.clear()
                            indexes.clear()
                            highlights.clear()
                            move_done = True
                            full_hand = False

    if turn == 2:

        board = Board.Board(p1_hand, p2_hand, discard_yellow, discard_blue, discard_white, discard_green, discard_red, deposit_yellow_p1, deposit_blue_p1, deposit_white_p1, deposit_green_p1, deposit_red_p1, deposit_yellow_p2, deposit_blue_p2, deposit_white_p2, deposit_green_p2, deposit_red_p2, deck)
        if board.isGameOver():
            scoreboard = True

    # Next round button
    if 1205 > mouse[0] > 1060 and 790 > mouse[1] > 720 and move_done and full_hand:
        pygame.draw.rect(screen, white, pygame.Rect(1055, 715, 160, 75), 3)
        if click[0] == 1:
            if turn == 1:
                turn = 2
                move_done = False
                discard_round = 0
            elif turn == 2:
                turn = 1
                move_done = False
                discard_round = 0

    # Exit button
    if 1275 > mouse[0] > 1235 and 46 > mouse[1] > 6 and click[0] == 1:
        si = False

    # Draw card button
    if move_done and 220 > mouse[0] > 70 and 790 > mouse[1] > 720 and full_hand == False:
        pygame.draw.rect(screen, white, pygame.Rect(65, 715, 160, 75), 3)
        if click[0] == 1:
            if turn == 1:
                p1_hand.append(deck.pop())
                p1_hand.sort(key=takeName)
                full_hand = True
            elif turn == 2:
                p2_hand.append(deck.pop())
                p2_hand.sort(key=takeName)
                full_hand = True

    # Drawing
    if discard_yellow:
        drawDiscard(discard_yellow, 150)
    if discard_blue:
        drawDiscard(discard_blue, 400)
    if discard_white:
        drawDiscard(discard_white, 650)
    if discard_green:
        drawDiscard(discard_green, 900)
    if discard_red:
        drawDiscard(discard_red, 1140)

    drawChoices(choices)
    drawHighlights(highlights)
    all_sprites.update()
    all_sprites.draw(screen)

    # Flip the display
    pygame.display.flip()

    if cards_left == 0:
        scoreboard = True

        p1_yellow_score = p1_yellow_score * yellow_dollars_p1
        if len(deposit_yellow_p1) > 7:
            p1_yellow_score = p1_yellow_score + 20
        p1_blue_score = p1_blue_score * blue_dollars_p1
        if len(deposit_blue_p1) > 7:
            p1_blue_score = p1_blue_score + 20
        p1_white_score = p1_white_score * white_dollars_p1
        if len(deposit_white_p1) > 7:
            p1_white_score = p1_white_score + 20
        p1_green_score = p1_green_score * green_dollars_p1
        if len(deposit_green_p1) > 7:
            p1_green_score = p1_green_score + 20
        p1_red_score = p1_red_score * red_dollars_p1
        if len(deposit_red_p1) > 7:
            p1_red_score = p1_red_score + 20

        p2_yellow_score = p2_yellow_score * yellow_dollars_p2
        if len(deposit_yellow_p2) > 7:
            p2_yellow_score = p2_yellow_score + 20
        p2_blue_score = p2_blue_score * blue_dollars_p2
        if len(deposit_blue_p2) > 7:
            p2_blue_score = p2_blue_score + 20
        p2_white_score = p2_white_score * white_dollars_p2
        if len(deposit_white_p2) > 7:
            p2_white_score = p2_white_score + 20
        p2_green_score = p2_green_score * green_dollars_p2
        if len(deposit_green_p2) > 7:
            p2_green_score = p2_green_score + 20
        p2_red_score = p2_red_score * red_dollars_p2
        if len(deposit_red_p2) > 7:
            p2_red_score = p2_red_score + 20

        p1_score = p1_yellow_score + p1_blue_score + p1_white_score + p1_green_score + p1_red_score
        p2_score = p2_yellow_score + p2_blue_score + p2_white_score + p2_green_score + p2_red_score

        while scoreboard:

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    scoreboard = False
                    si = False

            screen.fill(black)

            if p1_score > p2_score:
                score_text = 'Wygrywa Gracz 1! Miał ' + str(p1_score) + ' punktów. Przeciwnik miał ' + str(p2_score) + ' punktów!'
                scoresurface = myfont.render(score_text, True, white)
            elif p2_score > p1_score:
                score_text = 'Wygrywa Gracz 2! Miał ' + str(p2_score) + ' punktów. Przeciwnik miał ' + str(p1_score) + ' punktów!'
                scoresurface = myfont.render(score_text, True, white)
            elif p1_score == p2_score:
                score_text = 'Remis! ' + str(p1_score) + ' punktów miał każdy z graczy.'
                scoresurface = myfont.render(score_text, True, white)

            screen.blit(scoresurface, (280, 400))

            pygame.display.flip()

# Done! Time to quit.
pygame.quit()
