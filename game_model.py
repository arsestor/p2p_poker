from random import randbytes, randint, choice

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

# ♠ ♣ ♥ ♦

a = Player()
b = Player()
ch_p = check_players(a, b)
if ch_p[0] == True:
    print(ch_p[1])
else:
    print('Игроки не прошли проверку')