from random import randbytes

def get_player_hash():
    return hash(randbytes(32))

print(get_player_hash())