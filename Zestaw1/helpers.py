from random import random
from typing import List, Union


class Player:

    def __init__(self, name, win_p, capital):
        self.name = name
        self.win_p = win_p
        self.capital = capital
        self.wins = 0
        self.ruin_p = 0
        self.capital_trajectory = [capital]
        self.wins_trajectory = [0]
        self.start_win_p = win_p
        self.start_capital = capital

    def win(self, add_capital) -> None:
        self.capital += add_capital
        self.capital_trajectory.append(self.capital)
        self.wins_trajectory.append(self.wins_trajectory[-1] + 1)

    def lose(self) -> int:
        if self.capital == 0:
            self.capital_trajectory.append(0)
            self.wins_trajectory.append(self.wins_trajectory[-1])
            return 0
        else:
            self.capital -= 1
            self.capital_trajectory.append(self.capital)
            self.wins_trajectory.append(self.wins_trajectory[-1])
            return 1

    def reset(self):
        self.win_p = self.start_win_p
        self.capital = self.start_capital
        self.capital_trajectory = [self.start_capital]
        self.wins_trajectory = [0]


def can_play(players: List[Player]) -> bool:
    capable_players = 0
    for player in players:
        if player.capital > 0:
            capable_players += 1

    if capable_players < 2:
        return False
    else:
        return True


def update_capitals(players: List[Player], winner: Player) -> None:
    units_to_add = 0

    for player in players:
        if player != winner:
            units_to_add += player.lose()

    winner.win(units_to_add)


def update_probabilities(players: List[Player]) -> None:
    ps = 0
    capable_players = 0
    for player in players:
        if player.capital == 0:
            ps += player.win_p
            player.win_p = 0
        else:
            capable_players += 1

    for player in players:
        if player.capital > 0:
            player.win_p += (ps / capable_players)


def update_game(players: List[Player], winner: Player) -> None:
    update_capitals(players, winner)
    update_probabilities(players)


def get_winner(players: List[Player]) -> Player:
    who_wins = random()
    current_interval = 0
    for player in players:
        current_interval += player.win_p
        if who_wins <= current_interval:
            return player


def play_round(players):
    winner = get_winner(players)
    update_game(players, winner)


def end_game(players):
    for player in players:
        if player.capital > 0:
            player.wins += 1


def calculate_ruins(players, games_count):
    for player in players:
        player.ruin_p = 1 - (player.wins / games_count)


def reset_players(players):
    for player in players:
        player.reset()


def simulate_games(players: List[Player], n, limit=-1):
    rounds_list = []
    for _ in range(n):
        rounds_played = 0
        while can_play(players) or rounds_played == limit:
            play_round(players)
            rounds_played += 1
        end_game(players)
        rounds_list.append(rounds_played)
        # if n != 1 or n != 1000:
        #     reset_players(players)
    calculate_ruins(players, n)

    return rounds_list


def get_theoretical_result(a, b, pa, pb):
    if pa != 0.5:
        z = a + b
        counter = (pb / pa) ** a - (pb/pa) ** z
        denominator = 1 - (pb / pa) ** z
        return counter / denominator
    else:
        return 1 - a / (a + b)


def calculate_mean(values: Union[List[int], List[float]]):
    return sum(values) / len(values)


def calculate_variance(x_axis: Union[List[int], List[float]], avg_val: Union[int, float]):
    return sum((x - avg_val) ** 2 for x in x_axis) / len(x_axis)