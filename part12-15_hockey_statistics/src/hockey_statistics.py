import json


def print_player(player):
    points = player["goals"] + player["assists"]

    print(f"{player['name']:<21}{player['team']:<4}{player['goals']:>3} + {player['assists']:>2} = {points:>3}")


file_name = input("file name: ")

with open(file_name) as file:
    data = json.load(file)

print(f"read the data of {len(data)} players")

while True:
    print()
    print("commands:")
    print("0 quit")
    print("1 search for player")
    print("2 teams")
    print("3 countries")
    print("4 players in team")
    print("5 players from country")
    print("6 most points")
    print("7 most goals")

    command = input("command: ")

    if command == "0":
        break

    elif command == "1":
        name = input("name: ")

        for player in data:
            if player["name"] == name:
                print_player(player)

    elif command == "2":
        teams = sorted(set(player["team"] for player in data))

        for team in teams:
            print(team)

    elif command == "3":
        countries = sorted(set(player["nationality"] for player in data))

        for country in countries:
            print(country)

    elif command == "4":
        team = input("team: ")

        players = []

        for player in data:
            if player["team"] == team:
                players.append(player)

        players.sort(
            key=lambda player: player["goals"] + player["assists"],
            reverse=True
        )

        for player in players:
            print_player(player)

    elif command == "5":
        country = input("country: ")

        players = []

        for player in data:
            if player["nationality"] == country:
                players.append(player)

        players.sort(
            key=lambda player: player["goals"] + player["assists"],
            reverse=True
        )

        for player in players:
            print_player(player)

    elif command == "6":
        how_many = int(input("how many: "))

        players = sorted(
            data,
            key=lambda player: (
                player["goals"] + player["assists"],
                player["goals"]
            ),
            reverse=True
        )

        for player in players[:how_many]:
            print_player(player)

    elif command == "7":
        how_many = int(input("how many: "))

        players = sorted(
            data,
            key=lambda player: (
                -player["goals"],
                player["games"]
            )
        )

        for player in players[:how_many]:
            print_player(player)