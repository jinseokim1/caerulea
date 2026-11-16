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
print(match_history)
