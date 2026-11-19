import json
def save_matches(matches, filename):
    with open(filename, "w") as file:
        json.dump(matches, file, indent=4)

def load_matches(filename):
    try:
        with open(filename, "r") as file:
            data = json.load(file)
        return data
    except FileNotFoundError:
        print("File not found.")
        return []
    except json.JSONDecodeError:
        print("Data is not in correct format.")
        return None
import csv
def export_matches_csv(matches, filename):
    with open(filename, "w", newline="") as file:
        writer = csv.DictWriter(file, fieldnames=["match_id", "Champion name", "Role", "Kills", "Deaths", "Assists", "Win" ])
        writer.writeheader()
        writer.writerows(matches)
