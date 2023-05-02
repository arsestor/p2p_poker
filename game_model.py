from random import randint, choice, shuffle


class Player():
    def __init__(self):
        self.player_num = random.choice(range(1, 101))

    def accept_num(self, other_num):
        return self.player_num * other_num


class Deck():
    def __init__(self):
        self.cards = ['2♠', '2♣', '2♥', '2♦', '3♠', '3♣', '3♥', '3♦',
                      '4♠', '4♣', '4♥', '4♦', '5♠', '5♣', '5♥', '5♦',
                      '6♠', '6♣', '6♥', '6♦', '7♠', '7♣', '7♥', '7♦',
                      '8♠', '8♣', '8♥', '8♦', '9♠', '9♣', '9♥', '9♦',
                      '10♠', '10♣', '10♥', '10♦', 'J♠', 'J♣', 'J♥', 'J♦',
                      'Q♠', 'Q♣', 'Q♥', 'Q♦', 'K♠', 'K♣', 'K♥', 'K♦',
                      'A♠', 'A♣', 'A♥', 'A♦']
        self.range = 10000
        self.step = self.range // 52
    
    def shuffle(self):
        shuffle(self.cards)
    
    def get_card(self, num: int) -> str:
        card = self.cards[num//self.step]
        self.cards.remove(card)
        self.range -= self.step
        return card


class Game():
    def __init__(self, players: list):
        self.players = {i:players[i] for i in range(len(players))}
    
    def check_players(self):
        result = []
        for player1 in range(len(self.players)):
            for player2 in self.players:
                if player1 != player2:
                    result.append(self.players[player1].accept_num(self.players[player2].player_num))
        result = sorted(result)
        for i in range(len(result[1::2])):
            if result[i*2] != result[i*2+1]:
                return False
        return True


a = Player()
b = Player()
c = Player()

game = Game([a, b, c])
if game.check_players() == True:
    print(True)
