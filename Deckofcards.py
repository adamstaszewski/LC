colors = ['Y', 'B', 'W', 'G', 'R']
values = ['$1', '$2', '$3', 2, 3, 4, 5, 6, 7, 8, 9, 'X']


class Card:

    def __init__(self, color, number):
        self.color = color
        self.number = number
        self.name = f'{color}{number}'
        if number == '$1' or number == '$2' or number == '$3':
            self.value = 0
        elif number == 'X':
            self.value = 10
        else:
            self.value = number


class Deck:

    def __init__(self):
        self.deck_comp = []

    def create_deck(self):
        for color in colors:
            for value in values:
                self.deck_comp.append(Card(color, value))

        return self.deck_comp
