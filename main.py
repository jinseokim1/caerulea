print("League of Legends performance analyser")
match_history = [] #This stores all total matches
game_stat1 = {
        "match_id": 1, 
        "Champion name": "Kayn",
        "Role": "Jungle",
        "Kills": 12,
        "Deaths": 2,
        "Assists": 8,
        "Win": True        
    
}
game_stat2 = {
            "match_id": 2, 
            "Champion name": "Master Yi",
            "Role": "Jungle",
            "Kills": 5,
            "Deaths": 6,
            "Assists": 7,
            "Win": True    
}
game_stat3 = {
            "match_id": 3,
            "Champion name": "Kalista",
            "Role": "Attack Damage Carry (ADC)",
            "Kills": 9,
            "Deaths": 1,
            "Assists": 6,
            "Win": True 
}
#Create three game_stat dicts (sample) for each match

#Store game stat data
match_history.append(game_stat1)
match_history.append(game_stat2)
match_history.append(game_stat3)

    
#append all three games
'''Checkpoint: print the number of matches played,
the champion played in the third match,
the number of deaths in the first match,
and whether or not the second game was a win.'''
total_matches = len(match_history) #Calculate the total amount of matches played
print(f"The champion played in Game III was {match_history[2]["Champion name"]}.") #Find the champion played in game 3
print(f"You died {match_history[0]["Deaths"]} times in Game I.") #Find the amount of deaths in match 1
print(f"You won Game II: {match_history[1]["Win"]}") #Truthy/Falsy win in game 2


