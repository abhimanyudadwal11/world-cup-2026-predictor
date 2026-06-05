class Team:
    def __init__(self,name,rating):
        self.name=name
        self.rating=rating
    def display(self):
        print(f"Team: {self.name}");
        print(f"Rating: {self.rating}")
        return