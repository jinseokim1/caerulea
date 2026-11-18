'''Caerulea main.py-functions for winrate kda and champion filtering, as well
as functional main menu CUI.'''
def calculate_winrate(history): #The first function-will calculate winrate.
    wins = 0
    loss = 0
    if len(history) == 0:
        return 0
    else:
        for match in history:
            if match["Win"] == True:
                wins += 1
            else:
                loss += 1
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
        if isinstance(kda_champ, str):
            print(f"Your KDA (Kill Death Assists Ratio) on {champion} is {kda_champ}.")
        else:
            print(f"Your KDA (Kill Death Assists Ratio) on {champion} is {kda_champ:.2f}.")
#Sample test

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
        record = record == "true"
        history["match_id"] = matchid
        history["Champion name"] = champ_name
        history["Role"] = role
        history["Kills"] = kills
        history["Deaths"] = deaths
        history["Assists"] = assists
        history["Win"] = record #Updates dictionary
        matches.append(history)
        return matches #returnsfunction
#checks the Match ID system.

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
#Create overall statistics function
def overall_report(matches):
    if len(matches) == 0:
        print("There are no matches to record. ")
    else:
        print(f"Total matches played: {len(matches)}")
        print(f"Win Rate: {calculate_winrate(matches):.2f}%")
        print(f"Overall K/D/A: {calculate_kda(matches):.2f}")
#This function calls calculate_winrate and calculate_kda and displays an overall report, if there are 0 matches it will display that there are 0 matches to record.
'''Checkpoint 5: Main menu function'''
#Remember hist = [] is the sample 

def main_menu(matches):
    choices = [1, 2, 3, 4, 5]
    while True:
        print("1. Add a match")
        print("2. View Match History")
        print("3. View Champion Report")
        print("4. View Overall Statistics")
        print("5. Exit")
        try:
            menu = int(input("Enter your choice: "))
        except ValueError:
            print("Invalid Choice.")
            continue
        if menu == 1:
            add_match(matches)
            continue
        elif menu == 2:
            view_match_history(matches)
            continue
        elif menu == 3:
            champion = input("What is the name of the champion? ")
            champion_report(matches, champion)
        elif menu == 4:
            overall_report(matches) 
        elif menu == 5:
            print("Thank you!")
            break
        elif menu not in choices:
            print("Invalid Choice.")
            continue
main_menu(hist)

'''M2 done! connected all main menu options and confirmed they work.
Caerulea now has a functional command line interface. Final integration testing done. Now
starting on M3'''
        



            

    