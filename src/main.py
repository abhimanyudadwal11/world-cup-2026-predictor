from team import Team
from match import Match
from tournament import Tournament
#creating teams[] list
teams=[]
teams=[0]*8
spain=Team("Spain", 99)
teams[0]=spain
france=Team("France", 98)
teams[1]=france
argentina=Team("Argentina", 97)
teams[2]=argentina
brazil=Team("Brazil", 96)
teams[3]=brazil
portugal=Team("Portugal", 95)
teams[4]=portugal
england=Team("England",94)
teams[5]=england
norway=Team("Norway", 93)
teams[6]=norway
netherlands=Team("Netherlands",92)
teams[7]=netherlands
#teams[] list created

world_cup=Tournament(teams)

world_cup.play()

world_cup.display_result()