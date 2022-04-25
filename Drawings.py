import pygame
import Pebbles

white = (255, 255, 255)


def draw(x1, x2, x3, choice, index, mouse, click, highlights, choices, indexes, screen):
    if x1 > mouse[0] > x2 and 785 > mouse[1] > 725:
        pygame.draw.rect(screen, white, pygame.Rect(x3, 720, 70, 70), 3)
        if x1 > mouse[0] > x2 and 785 > mouse[1] > 725 and click[0] == 1:
            choices.clear()
            indexes.clear()
            highlights.clear()
            highlights.append((x3, 720))
            choices.append(choice)
            indexes.append(index)


def drawDeposit(deposit, x_coords, all_sprites):
    x = x_coords
    z = 0
    if len(deposit) < 4:
        for i in range(0, len(deposit)):
            path = 'Grafika/Pebbles/' + deposit[z].name + '.png'
            name = Pebbles.Pebble(x, 480, path)
            all_sprites.add(name)
            x = x + 65
            z = z + 1
    if 4 <= len(deposit) < 7:
        for i in range(0, 3):
            path = 'Grafika/Pebbles/' + deposit[z].name + '.png'
            name = Pebbles.Pebble(x, 480, path)
            all_sprites.add(name)
            x = x + 65
            z = z + 1
        x = x_coords
        for i in range(3, len(deposit)):
            path = 'Grafika/Pebbles/' + deposit[z].name + '.png'
            name = Pebbles.Pebble(x, 540, path)
            all_sprites.add(name)
            x = x + 65
            z = z + 1
    if 7 <= len(deposit) < 10:
        for i in range(0, 3):
            path = 'Grafika/Pebbles/' + deposit[z].name + '.png'
            name = Pebbles.Pebble(x, 480, path)
            all_sprites.add(name)
            x = x + 65
            z = z + 1
        x = x_coords
        for i in range(3, 6):
            path = 'Grafika/Pebbles/' + deposit[z].name + '.png'
            name = Pebbles.Pebble(x, 540, path)
            all_sprites.add(name)
            x = x + 65
            z = z + 1
        x = x_coords
        for i in range(6, len(deposit)):
            path = 'Grafika/Pebbles/' + deposit[z].name + '.png'
            name = Pebbles.Pebble(x, 600, path)
            all_sprites.add(name)
            x = x + 65
            z = z + 1
    if 10 <= len(deposit) < 13:
        for i in range(0, 3):
            path = 'Grafika/Pebbles/' + deposit[z].name + '.png'
            name = Pebbles.Pebble(x, 480, path)
            all_sprites.add(name)
            x = x + 65
            z = z + 1
        x = x_coords
        for i in range(3, 6):
            path = 'Grafika/Pebbles/' + deposit[z].name + '.png'
            name = Pebbles.Pebble(x, 540, path)
            all_sprites.add(name)
            x = x + 65
            z = z + 1
        x = x_coords
        for i in range(6, 9):
            path = 'Grafika/Pebbles/' + deposit[z].name + '.png'
            name = Pebbles.Pebble(x, 600, path)
            all_sprites.add(name)
            x = x + 65
            z = z + 1
        x = x_coords
        for i in range(9, len(deposit)):
            path = 'Grafika/Pebbles/' + deposit[z].name + '.png'
            name = Pebbles.Pebble(x, 660, path)
            all_sprites.add(name)
            x = x + 65
            z = z + 1

def drawOpponentDeposit(deposit, x_coords, all_sprites):
    x = x_coords
    z = 0
    if len(deposit) < 5:
        for i in range(0, len(deposit)):
            path = 'Grafika/Small Pebbles/' + deposit[z].name + '.png'
            name = Pebbles.Pebble(x, 100, path)
            all_sprites.add(name)
            x = x + 45
            z = z + 1
    if 5 <= len(deposit) < 9:
        for i in range(0, 4):
            path = 'Grafika/Small Pebbles/' + deposit[z].name + '.png'
            name = Pebbles.Pebble(x, 100, path)
            all_sprites.add(name)
            x = x + 45
            z = z + 1
        x = x_coords
        for i in range(4, len(deposit)):
            path = 'Grafika/Small Pebbles/' + deposit[z].name + '.png'
            name = Pebbles.Pebble(x, 135, path)
            all_sprites.add(name)
            x = x + 45
            z = z + 1
    if 9 <= len(deposit) < 13:
        for i in range(0, 4):
            path = 'Grafika/Small Pebbles/' + deposit[z].name + '.png'
            name = Pebbles.Pebble(x, 100, path)
            all_sprites.add(name)
            x = x + 45
            z = z + 1
        x = x_coords
        for i in range(4, 8):
            path = 'Grafika/Small Pebbles/' + deposit[z].name + '.png'
            name = Pebbles.Pebble(x, 135, path)
            all_sprites.add(name)
            x = x + 45
            z = z + 1
        x = x_coords
        for i in range(8, len(deposit)):
            path = 'Grafika/Small Pebbles/' + deposit[z].name + '.png'
            name = Pebbles.Pebble(x, 170, path)
            all_sprites.add(name)
            x = x + 45
            z = z + 1

