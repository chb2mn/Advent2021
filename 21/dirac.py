from icecream import ic
from functools import lru_cache

class Dice:
    def __init__(self):
        self.state = 0
    def roll(self):
        self.state += 1
        if self.state > 100:
            self.state = 1
        return self.state

class Board:
    def __init__(self, player_pos, villain_pos):
        self.positions = [player_pos, villain_pos]
    def move(self, player_num, dist):
        self.positions[player_num] += dist
        self.positions[player_num] = self.positions[player_num] % 10
        if self.positions[player_num] == 0:
            self.positions[player_num] =10
        return self.positions[player_num]

def update_state(pos, total_roll):
    pos = (total_roll + pos) % 10
    if pos == 0:
        return 10
    else:
        return pos

@lru_cache(maxsize=None)
def play_game(play_pos, comp_pos, play_score, comp_score, comp_turn):
    if play_score >= 21:
        return 1,0
    elif comp_score >= 21:
        return 0,1
    wins = 0
    losses = 0
    results = []
    for i in range(3,10):
        if not comp_turn:
            results.append(play_game(update_state(play_pos, i), comp_pos, play_score+update_state(play_pos,i), comp_score, not comp_turn))
        else:
            results.append(play_game(play_pos, update_state(comp_pos, i), play_score, comp_score+update_state(comp_pos,i), not comp_turn))
    wins += results[0][0] + results[-1][0]
    losses += results[0][1] + results[-1][1]
    wins += 3*results[1][0] + 3*results[-2][0]
    losses += 3*results[1][1] + 3*results[-2][1]
    wins += 6*results[2][0] + 6*results[-3][0]
    losses += 6*results[2][1] + 6*results[-3][1]
    wins += 7*results[3][0] 
    losses += 7*results[3][1] 

    return wins, losses

player_pos = 2
comp_pos = 5
test_player_pos = 4
test_comp_pos = 8

turn = 0
part = 2
if part ==1:
    board = Board(player_pos, comp_pos)
    dice = Dice()
    while all(x < 1000for x in scores):
        roll = 0
        for i in range(3):
            rolli = dice.roll()
            roll += rolli
        score = board.move(turn%2, roll)
        scores[turn%2] += score
        print(f"Turn {turn+1}: player {turn%2} rolled {roll} and arrived at space {score} for a total of {scores[turn%2]}")
        turn+=1

    ic(turn*3)
    ic(turn*3*min(scores))

else:
    wins, losses = play_game(player_pos, comp_pos, 0,0,False)
    ic(wins)
    ic(losses)
