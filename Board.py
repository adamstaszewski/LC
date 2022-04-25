class Board:

    def __init__(self, p1_hand, p2_hand, discard_yellow, discard_blue, discard_white, discard_green, discard_red, deposit_yellow_p1, deposit_blue_p1, deposit_white_p1, deposit_green_p1, deposit_red_p1, deposit_yellow_p2, deposit_blue_p2, deposit_white_p2, deposit_green_p2, deposit_red_p2, deck):
        self.p1_hand = p1_hand
        self.p2_hand = p2_hand
        self.discard_yellow = discard_yellow
        self.discard_blue = discard_blue
        self.discard_white = discard_white
        self.discard_green = discard_green
        self.discard_red = discard_red
        self.deposit_yellow_p1 = deposit_yellow_p1
        self.deposit_blue_p1 = deposit_blue_p1
        self.deposit_white_p1 = deposit_white_p1
        self.deposit_green_p1 = deposit_green_p1
        self.deposit_red_p1 = deposit_red_p1
        self.deposit_yellow_p2 = deposit_yellow_p2
        self.deposit_blue_p2 = deposit_blue_p2
        self.deposit_white_p2 = deposit_white_p2
        self.deposit_green_p2 = deposit_green_p2
        self.deposit_red_p2 = deposit_red_p2
        self.deck = deck

    def isGameOver(self):
        if len(self.deck) == 0:
            return True
        else:
            return False

    def possibleMoves(self):
        deposits = [self.deposit_yellow_p1,self.deposit_blue_p1, self.deposit_white_p1, self.deposit_green_p1, self.deposit_red_p1]
        for i in range(8):
            for item in deposits:
                if self.p2_hand[i].color == self.p2_hand[i].value:
                    return