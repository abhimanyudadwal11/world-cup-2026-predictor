from match import Match
import random

class Tournament:
    def __init__(self,teams):
        self.teams=teams
        self.champion=None

    def play(self):
        teams=self.teams.copy()
        random.shuffle(teams)
        while(len(teams)>1):
            winners=[]
            for i in range(0,len(teams),2):
                match=Match(teams[i],teams[i+1])
                match.play()
                winners.append(match.winner)
            teams=winners
        self.champion=teams[0]

    def display_result(self):
        if self.champion is None: print("Tournament has not yet begun.")
        else: print(f"Champions: {self.champion.name}")