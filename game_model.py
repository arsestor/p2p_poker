from random import randbytes, randint

class Player():
    def __init__(self):
        self.player_num = hash(randbytes(32))

    def accept_num(self, other_num):
        return self.player_num * other_num
    
    def send_num(self):
        return self.player_num

a = Player()
b = Player()
if b.accept_num(a.send_num()) == a.accept_num(b.send_num()):
    print(True)

# def get_player_hash():
#     return hash(randbytes(32))

# def check(x, y):
#     if hash(x*hash(y)) == hash(hash(x)*y):
#         return True
#     else:
#         return False

# print(check(get_player_hash(), get_player_hash()))