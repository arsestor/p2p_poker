from random import randint, choice, shuffle

def check_players(a, b):
    if b.accept_num(a.player_num) == a.accept_num(b.player_num):
        return [True, a.accept_num(b.player_num)]
    else:
        return [False, a.accept_num(b.player_num), b.accept_num(a.player_num)]

class Player():
    def __init__(self):
        self.player_num = choice(range(1, 101))

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
        print(result)
        

a = Player()
b = Player()
c = Player()
if ch_p[0] == True:
    game = Game([a, b, c])
    game.check_players()
else:
    print('Игроки не прошли проверку')