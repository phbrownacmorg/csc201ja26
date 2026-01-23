from random import random

def simulate_point(p: float) -> bool:
    """Simulate a single volley in a volleyball match.  The serving team has 
        probability P1 of winning the rally.  Return True if the serving team
        won; otherwise, return False."""
    return random() < p

def game_over(game_pts: int, score1: int, score2: int) -> bool:
    return (score1 >= game_pts or score2 >= game_pts) and (abs(score1 - score2) >= 2)

def simulate_one_game(p1: float, p2: float, scoring: str) -> bool:
    """Simulate a volleyball game between Team 1, which has probability P1 of winning
        the point when they serve, and Team 2, which has probability P2 of winning the
        point when they serve, using the type of scoring indicated by SCORING.
        Return True if Team 1 won; otherwise, return False.  The team that serves
        to start is chosen by a coin flip."""
    game_pts = 15
    if scoring == "rally":
        game_pts = 25
    team1_serving = random() < 0.5 # Coin flip
    team1_score = 0
    team2_score = 0
    while not game_over(game_pts, team1_score, team2_score):
        if team1_serving:
            if simulate_point(p1):
                team1_score = team1_score + 1
            else:
                if scoring == 'rally':
                    team2_score = team2_score + 1
                team1_serving = False
        else: # Team 2 serving
            if simulate_point(p2):
                team2_score = team2_score + 1
            else:
                if scoring == 'rally':
                    team1_score = team1_score + 1
                team1_serving = True
    return team1_score > team2_score

def simulate_games(p1: float, p2: float, games: int, scoring: str) -> int:
    """Simulate N volleyball games between Team 1, which has probability P1 of winning
        the point when they serve, and Team 2, which has probability P2 of winning the
        point when they serve.  Return the number of games Team 1 won."""
    team1_wins = 0
    for i in range(games): # type: ignore
        if simulate_one_game(p1, p2, scoring):
            team1_wins = team1_wins + 1
    return team1_wins

def main(args: list[str]) -> int:
    print('This program simulates a volleyball game between Team 1 and Team 2.')
    scoring = input('Please enter the kind of scoring to use (rally or sideout): ')
    scoring = scoring.strip().lower() # don't make it too hard to match...
    p1 = float(input('Please enter the probability that Team 1 wins the point when they serve: '))
    p2 = float(input('Please enter the probability that Team 2 wins the point when they serve: '))
    games = int(input('Please enter the number of games to simulate: '))
    team1_wins = simulate_games(p1, p2, games, scoring)
    print(f'Team 1 won {team1_wins} out of {games}, or {(team1_wins/games)*100:.2f}%.')
    return 0

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
