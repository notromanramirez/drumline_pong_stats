# Roman Ramirez, rr8rk@virginia.edu
# PowerPoint Night 2023
# Pong SICKOS Committee

class Player:

    def __init__(self, name, seed_1s, seed_2s) -> None:
        self.name = name
        self.seed_1s = seed_1s
        self.seed_2s = seed_2s
    
    def __str__(self):
        return self.name
    
    def __repr__(self):
        return '(repr)' + self.name
    
class Match:

    def __init__(self, number, t1, t2, r1, r2, t3 = None, t4 = None) -> None:
        # team 1, this is a list of players of length 1 or 2
        self.t1 = list()
        self.t1.append(t1)
        if t3 is not None:
            self.t1.append(t3)
        # team 2, this is a list of player of length 1 or 2
        self.t2 = list()
        self.t2.append(t2)
        if t4 is not None:
            self.t2.append(t4)
        # how many cups did player 1 score in that match
        self.s1 = s1
        # how many cups did player 2 score in that match
        self.s2 = s2

#%% INITIALIZING PLAYERS        

players = dict()

with open("players.txt") as f:
    for i, line in enumerate(f.readlines()):
        name, seed_1s, seed_2s = line.strip().split(',')
        name = name.strip()
        seed_1s = int(seed_1s) if seed_1s != 'None' else None
        seed_2s = int(seed_2s) if seed_2s != 'None' else None
        
        players.update({name: Player(name, seed_1s, seed_2s)})

# for player in players.values():
#     print(player.name, player.seed_1s, player.seed_2s)

#%% INITIALIZING MATCHES

# singles 2022
matches_1s = dict()

with open("matches_1s.txt") as f:
    for i, line in enumerate(f.readlines()):
        match_number, t1, t2, s1, s2 = [x.strip() for x in line.split(',')]
        match_number = int(match_number)
        s1 = int(s1)
        s2 = int(s2)
        
        matches_1s.update(
            {
                match_number: Match(match_number, players[t1], players[t2], s1, s2)
                }
            )

# doubles 2022
matches_2s = dict()

with open("matches_2s.txt") as f:
    for i, line in enumerate(f.readlines()):
        match_number, t1, t3, t2, t4, s1, s2 = [x.strip() for x in line.split(',')]
        match_number = int(match_number)
        s1 = int(s1)
        s2 = int(s2)
        
        matches_2s.update(
            {
                match_number: Match(match_number, players[t1], players[t2], s1, s2, players[t3], players[t4])
                }
            )
        
        
#%% ANALYSIS: calculate number of games played