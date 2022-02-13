import random


class Player:
    
    def __init__(self, name, p, c) -> None:
        self.name = name
        self.p = p # probability of winning one ROUND
        self.c = c # player's capital
        self.W = 0 # number of player's GAME wins
        self.R = 0 # probability of player's ruin
        self.ct = [self.c] # Trajectory of player's capital
        self.wt = [0] #trajectory of player's wins
        self.PP = p # player's starting probability of winning one ROUND
        self.CC = c # player's starting capital


    def reset(self):
        self.p = self.PP
        self.c = self.CC
        self.ct = [self.c]
        self.wt = [0]


    def win(self, units):
        self.c += units
        ( self.ct ).append( self.c )
        ( self.wt ).append( ( self.wt )[-1] +1 )

    def loose(self):
        if self.c == 0:
            (self.ct).append(0)
            (self.wt).append( (self.wt)[-1] )
            return 0
        else:
            self.c -= 1
            ( self.ct ).append( self.c )
            (self.wt).append( (self.wt)[-1] )
            return 1

    def __str__(self) -> str:
        return f"Name: {self.name}, p: {self.p}, c: {self.c} W: {self.W}, R: {self.R}"


def you_can_play(players) -> bool:

    capable_players = 0
    for player in players:
        if player.c > 0: capable_players += 1

    if capable_players < 2: return False
    else: return True


def update_capitals( players, winner ):
    how_many_units_to_add = 0

    for player in players:
        if player != winner:
            how_many_units_to_add += player.loose()
        
    winner.win(how_many_units_to_add)


def update_probabilities( players ) -> None:
    ps = 0
    capable_players = 0
    for player in players:
        if player.c == 0:
            ps += player.p
            player.p = 0
        else:
            capable_players += 1

    for player in players:
        if player.c > 0:
            player.p += (ps / capable_players )


def update_game_state( players, winner ):
    update_capitals(players, winner)
    update_probabilities(players)
    

def get_a_winner(players):
    who_wins = random.random()
    current_interval = 0
    for player in players:
        current_interval += player.p
        if who_wins <= current_interval:
            return player


def play_a_round(players):
    winner = get_a_winner(players)
    update_game_state(players, winner)


def end_game(players):
    for player in players:
        if player.c > 0:
            player.W += 1


def calculate_Rs(players, games_count):
    for player in players:
        player.R = 1 - ( ( player.W ) / ( games_count ) )


def reset_players(players):
    for player in players:
        player.reset()


def simulate(players,N, S = -1 ):
    rounds_list = list()
    for i in range(1, N+1):
        rounds_played = 0
        while you_can_play(players) or rounds_played == S:
            play_a_round(players)
            rounds_played += 1
        end_game(players)
        rounds_list.append(rounds_played)
        if N != 1: reset_players(players)
    calculate_Rs(players,N)

    return rounds_list

#Tutaj się kończy częśc dla więcej niż dwóch graczy