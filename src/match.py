import random

class Match:
    def __init__(self,team1,team2): #object composition
        self.team1=team1
        self.team2=team2
        winner=None #Note to self: winner is a Team object
    def play(self):
        total_rating=self.team1.rating+self.team2.rating
        team1_prob=self.team1.rating/total_rating
        if(random.random()<team1_prob):
            self.winner=self.team1
        else:
            self.winner=self.team2
        return self.winner
    def display_result(self):
        print(f"{self.team1.name} ({self.team1.rating}) vs {self.team2.name} ({self.team2.rating})")
        if self.winner is None:
            print("Result: Not played yet.")
        else:
            print(f"Winner: {self.winner.name}")
        return
    