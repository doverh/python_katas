# Dover Hellfeldt - Jan 2018
# Inspired by https://codeclubprojects.org/en-GB/python/team-chooser/
# This app is a team chooser. Can choose a team of any size  by name or numbers  
# To implement:
# API Service that allows anyone call it sending the parameters on request 
# list of player names, or just total number of players, and numeber of players by team
# UI - TBD
# Add exception when number of players / times is not exactly

import random

#Function to genereta list of players

def teamGenerator(category, total_players):
    if category == "name":
        names = []
        for i in range(1, total_players + 1):
            #insert a name
            name.append(input("Inform a name for player "+(i)))
        return names
    else:
        names = []
        for i in range(1, total_players + 1):
            names.append(i)
        return names

#Divide number of players by the number of teams

def split_teams(teams, num_teams):
    num_players = int(len(teams) / num_teams)
    for i in range(1, num_teams + 1):
        team = random.sample(teams, num_players)
        print(f"Team [{i}]: {team}")
        #remove those already in a team
        teams=[item for item in teams if item not in team]
        
#call method    
split_teams(teamGenerator("number",21),5)
split_teams(teamGenerator("name",4),2)  



