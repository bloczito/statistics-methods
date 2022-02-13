import random


class Player:
    
    def __init__(self, name, p, c) -> None:
        self.name = name
        self.p = p
        self.c = c
        self.W = 0
        self.R = 0
        self.ct = [self.c]
        self.wt = [0]
        self.PP = p
        self.CC = c


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

# p - prawdopodobienstwo wygrania RUNDY gracza NAZWA
# c - Player's starting capital
# LW - liczba wygranych GIER przez gracza NAZWA
# PW - prawdopodobienstwo wygrania GRY przez gracza NAZWA
# ct - Capital Trajectory
# wt - Wins Trajectory
#Gracze = { "NAZWA": { "p":1/n, "c": c, "LW": LW, "PW": PW, "ct": list(), "wt": list() } }


# Odtąd zaczyna się nieskończona część dla więcej niż dwóch graczy
def you_can_play(players) -> bool:
    """ Checks if the next round can be played.

    If there are at least 2 players with capital 
    greater then 0, True is returned. Otherwise False is returned 
    """

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

def simulate(players,N):
    for i in range(1, N+1):
        while you_can_play(players):
            play_a_round(players)
        end_game(players)
        reset_players(players)
    calculate_Rs(players,N)

#Tutaj się kończy częśc dla więcej niż dwóch graczy


def symuluj(a=50,b=50,p=1/2,N=100):
    z = a+b
    q = 1 - p
    wygrane_a = 0
    wygrane_b = 0
    liczby_rund = list()
    for i in range(0,N):
        _a=a
        _b=b
        liczba_rund = 0
        while _a != 0 and _b != 0:
            kto_wygra = random.random()
            if kto_wygra < p:
                _a = _a+1
                _b = _b-1
            else:
                _a = _a-1
                _b = _b+1
            liczba_rund += 1
        liczby_rund.append(liczba_rund)

        if _a == 0:
            wygrane_b = wygrane_b + 1
        else:
            wygrane_a = wygrane_a + 1



    ra_s = 1 - (wygrane_a/N)
    return ra_s, liczby_rund


def symuluj_kapitaly(a,N,p,P):
    if a < N: N = a

    i = 0
    _a = a
    aty = list()
    for j in range(1,P):
        i = 0
        _a = a
        while i < N:
            kto_wygra = random.random()
            if kto_wygra < p:
                _a = _a+1
            else:
                _a = _a-1
            i = i + 1

        aty.append(_a)

    return aty


def symuluj_trajektorie(a,b,p):
    wygrane_a = 0
    _a=a
    _b=b
    liczba_rund = 0
    trajektoria_kapitalu = list()
    trajektoria_wygranych = list()
    while _a != 0 and _b != 0:
        kto_wygra = random.random()
        if kto_wygra < p:
            _a = _a+1
            _b = _b-1
            wygrane_a = wygrane_a + 1
        else:
            _a = _a-1
            _b = _b+1
        trajektoria_wygranych.append(wygrane_a)
        trajektoria_kapitalu.append(_a)

        liczba_rund += 1
        if _a == 0: wygrany = "B"
        else: wygrany = "A"

    return liczba_rund, trajektoria_wygranych, trajektoria_kapitalu, wygrany