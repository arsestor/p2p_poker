from random import randbytes, randint

def check_players(a, b):
    if b.accept_num(a.send_num()) == a.accept_num(b.send_num()):
        return True
    else:
        return False

class Player():
    def __init__(self):
        self.player_num = hash(randbytes(32))

    def accept_num(self, other_num):
        return self.player_num * other_num
    
    def send_num(self):
        return self.player_num
    


a = Player()
b = Player()