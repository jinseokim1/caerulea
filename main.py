'''Caerulea main.py-functions for winrate kda and champion filtering, as well
as functional main menu CUI.'''
#JSON/CSV functionality
import json
import csv
from json_util import save_matches, load_matches
from json_util import export_matches_csv



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
    choices = [1, 2, 3, 4, 5, 6, 7, 8]
    while True:
        print("1. Add a match")
        print("2. View Match History")
        print("3. View Champion Report")
        print("4. View Overall Statistics")
        print("5. View Statistical Report")
        print("6. Exit")
        print("7. Export Match History to CSV")
        print("8. Remove a match")
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
            statistical_report(matches)
        elif menu == 6:
            validate = input("Are you sure? Y for confirmation. ").strip().lower()
            if validate == "y":
                save_matches(matches, "matches.json")
                break
            if validate != "y":
                continue
        elif menu == 7:
            export_matches_csv(matches, "matches.csv")
            print("Match history exported successfully.")
        elif menu == 8:
            try:
                remove = int(input("Enter the match ID to delete: "))
                deleted = delete_match(matches, remove)
                if deleted == True:
                    print("Match removed successfully.")
                if deleted == False:
                    print("Match could not be found.")
            except ValueError:
                print("Invalid match ID.")
                continue

        elif menu not in choices:
            print("Invalid Choice.")
            continue


'''M2 done! connected all main menu options and confirmed they work.
Caerulea now has a functional command line interface. Final integration testing done. Now
starting on M3'''
#Now make function based on average kills deaths assists
def calculate_averages(matches):
    total_kills = 0
    total_deaths = 0
    total_assists = 0
    if len(matches) == 0:
            return(0,0,0)
    else:
        for match in matches:
            total_kills = match["Kills"] + total_kills
            total_deaths = match["Deaths"] + total_deaths
            total_assists = match["Assists"] + total_assists
        avg_kills = total_kills / len(matches)
        avg_deaths = total_deaths / len(matches)
        avg_assists = total_assists / len(matches)
        total_avg = (avg_kills, avg_deaths, avg_assists)
        return total_avg #Return total_avg as a tuple
#Function based on average takedowns/kill involvement
def calculate_avg_takedowns(matches):
    total_takedowns = 0
    if len(matches) == 0:
        return 0
    for match in matches:
        total_takedowns = match["Kills"] + match["Assists"] + total_takedowns
    total_takedowns_avg = total_takedowns / len(matches)
    total_takedowns_avg = float(f"{total_takedowns_avg}")
    return total_takedowns_avg
#Function based on performance extremes-retrieve the best and worst games.
def find_performance_extremes(matches):
    if len(matches) == 0:
            return (None, None, None, None, None, None)
    else:
        most_kills = matches[0]
        least_kills = matches[0]
        most_deaths = matches[0]
        least_deaths = matches[0]
        most_assists = matches[0]
        least_assists = matches[0]
        for match in matches:
            if match["Kills"] > most_kills["Kills"]:
                most_kills = match
            if match["Kills"] < least_kills["Kills"]:
                least_kills = match
            if match["Deaths"] > most_deaths["Deaths"]:
                most_deaths = match
            if match["Deaths"] < least_deaths["Deaths"]:
                least_deaths = match
            if match["Assists"] > most_assists["Assists"]:
                most_assists = match
            if match["Assists"] < least_assists["Assists"]:
                least_assists = match
        return(most_kills, least_kills, most_deaths, least_deaths, most_assists, least_assists)
'''Checkpoint I-III finished. 3 statistic calculation functions done-
calculate average kills, deaths, assists, calculate average takedowns, and find performance extremes.
Will continue with the last 2 parts of M3-Recent Match Performance and Statistical Summary Report.'''

#Next function: this will let users analyze their last N games.
def recent_performance(matches, n):
    if n <= 0 or len(matches) == 0:
        return {
        "matches": 0,
        "winrate": 0,
        "avg_kills": 0,
        "avg_deaths": 0,
        "avg_assists": 0,
        "kda": 0
    }
    recent_matches = matches[-n:]
    amt_matches = len(recent_matches)
    amt_kills, amt_deaths, amt_assists = calculate_averages(recent_matches) 
    amt_winrate = calculate_winrate(recent_matches) 
    amt_kda = calculate_kda(recent_matches)
    summary = {
        "matches": amt_matches,
        "winrate": amt_winrate,
        "avg_kills": amt_kills,
        "avg_deaths": amt_deaths,
        "avg_assists": amt_assists,
        "kda": amt_kda
    }
    return summary
from sample_data import sample_matches 
#Sample data from a sample.py 100 games to test this

#Checkpoint V: statistical summary report. create function that puts it all together.
def statistical_report(matches):
        if len(matches) == 0:
            nothing = print("There are no matches to record.")
            return nothing
        print(f"Total matches played: {len(matches)}")
        print(f"Overall Win Rate: {calculate_winrate(matches):.2f}%")
        (a, b, c) = calculate_averages(matches)
        print(f"Average Kills: {a:.2f} Kills Per Game.")
        print(f"Average Deaths: {b:.2f} Deaths Per Game.")
        print(f"Average Assists: {c:.2f} Assists Per Game.")
        j = calculate_kda(matches) 
        if j == "Perfect": #build failsafe for input
            print(f"Overall KDA: {j}")
        else:
            print(f"Overall KDA: {j:.2f}")
        (d, e, f, g, h, i) = find_performance_extremes(matches) #use variables here and line 304 as well as 299 to store values and only call function once. Learning/implenting code effiency.
        print(f"Most Kills in a game: {d["Kills"]}-{d["Champion name"]} (Match {d["match_id"]})")
        print(f"Least Kills in a game: {e["Kills"]}-{e["Champion name"]} (Match {e["match_id"]})")
        print(f"Most Deaths in a game: {f["Deaths"]}-{f["Champion name"]} (Match {f["match_id"]})")
        print(f"Least Deaths in a game: {g["Deaths"]}-{g["Champion name"]} (Match {g["match_id"]})")
        print(f"Most Assists in a game: {h["Assists"]}-{h["Champion name"]} (Match {h["match_id"]})")
        print(f"Least Assists in a game: {i["Assists"]}-{i["Champion name"]} (Match {i["match_id"]})")
'''M3 Complete-basic statistical analysis complete, should test code and commit'''
'''Create function to delete matches'''
def delete_match(matches, match_id):
    for match in matches:
        if match["match_id"] == match_id:
            matches.remove(match)
            return True
    return False
    

matches = load_matches("matches.json")
if matches is not None:
    main_menu(matches)


   
    

        

        







            

    