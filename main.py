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
            "Win": False 
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
def calculate_winrate(history): #The first function-will calculate winrate.
    wins = 0
    loss = 0
    if len(history) == 0:
        return 0
    else:
        for match in history:
            if match["Win"] == True:
                wins = wins + 1
            else:
                loss = loss + 1
        winrate = wins / (wins + loss)
        winratepct = winrate * 100  
        return winratepct
def calculate_kda(history): #The second function-will calculate Kills/Deaths/Assists, or KDA ((Kills+Assists)/Deaths)
    Kills = 0
    Deaths = 0
    Assists = 0
    if len(history) == 0:
        return 0
    else:
        for match in history:
            Kills = Kills + match["Kills"]
            Deaths = Deaths + match["Deaths"]
            Assists = Assists + match["Assists"]
        if Deaths == 0:
            kda = "Perfect"
        else:
            kda = (Kills + Assists) / Deaths
        return kda
def filter_by_champion(history, champion): #This third function will remove all other games besides those by a specific Champ name
    matching_games = [] 
    for match in history:
        if champion.lower() == match["Champion name"].lower():
            matching_games.append(match)
    return matching_games
def champion_report(history, champion): #This fourth function will blend the first 3 to create a report by champion. Perhaps in the future I will add statistical reporting for things such as Role/Class/Subclass type.
    matching_games_list = filter_by_champion(history, champion)
    if len(matching_games_list) == 0:
        print("You have no games on this champion.")
    else:
        win_rate_pct_champ = calculate_winrate(matching_games_list)
        kda_champ = calculate_kda(matching_games_list) 
        print(f"Your win rate on {champion} is {win_rate_pct_champ:.2f}%.")
        print(f"Your KDA (Kill Death Assists Ratio) on {champion} is {kda_champ}.")
champion_report(match_history, "Kayn") #Sample test

'''M2'''
hist = []
valid_roles = {"top": "Top",
               "mid": "Mid",
               "jungle": "Jungle",
               "adc": "ADC",
               "support": "Support"
}
win_loss = ["true", "false"]
def add_match(matches): #First function of Milestone 2, adding match history. Use try/except and while Loop to handle exceptions.
        history = {}
        while True:
                champ_name = input("Champion: ").strip().title()
                if champ_name == "":
                    print("Enter a valid Champion Name.")
                    continue
                break
        while True:
                role = input("What role did you play? ").strip().lower()
                if role not in valid_roles:
                    print("Invalid role.")
                    continue
                role = valid_roles[role]
                break  
        while True:
            try:
                kills = int(input("How many kills did you record? "))
            except ValueError:
                print("Please enter a valid number.")
                continue
            if kills < 0:
                print("Kills can not be negative.")
                continue
            break
        while True:
            try:
                deaths = int(input("How many times did you die? "))
            except ValueError:
                print("Please enter a valid number.")
                continue
            if deaths < 0:
                print("Deaths can not be negative.")
                continue
            break
        while True:
            try:
                assists = int(input("How many assists did you record? "))
            except ValueError:
                print("Please enter a valid number.")
                continue
            if assists < 0:
                print("Assists can not be negative.")
                continue
            break
        while True:
            try:
                record = input("Did you win the game? True/False ").strip().lower()
            except ValueError:
                print("Please enter True or False.")
                continue
            if record not in win_loss:
                print("Please enter True or False.")
                continue
            break
        #Use try/except and if statements for input validation.
        #Now create match_id system
        if len(matches) == 0:
            matchid = 1
        else:
            ids = [match["match_id"] for match in matches] #("Creates list of matches")
            matchid = max(ids) + 1
        record = record == "True"
        history["match_id"] = matchid
        history["Champion name"] = champ_name
        history["Role"] = role
        history["Kills"] = kills
        history["Deaths"] = deaths
        history["Assists"] = assists
        history["Win"] = record #Updates dictionary
        matches.append(history)
        return matches #returnsfunction

add_match(hist)
print(hist) #checks the Match ID system.

'''Checkpoint 4'''
def view_match_history(matches):
    if len(matches) == 0:
        print("No matches have been recorded.")
    else:
        print("===Match History===")
        for match in matches:
            print(f"match ID: #{match["match_id"]}")
            print(f"Champion: {match["Champion name"]}")
            print(f"Role: {match["Role"]}")
            print(f"KDA: {match["Kills"]}/{match["Deaths"]}/{match["Assists"]}")
            if match["Win"]:
                result = "Win"
                print(f"Result: {result}")
            else:
                result = "Loss"
                print(f"Result: {result}")
view_match_history(hist)
            


            

    












