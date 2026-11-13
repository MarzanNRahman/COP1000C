class Players:
    def __init__(self, playerName, playerPosition):
        self.playerName = playerName
        self.playerPosition = playerPosition


class NFLTeam:
    def __init__(self, teamName, playerList):
        self.teamName = teamName
        self.playerList = playerList

    def displayTeam(self):
        print(f"Team: {self.teamName}")
        print("Players:")

        for player in self.playerList:
            print(f"{player.playerName} - {player.playerPosition}")


def main():
    # Create the four players.
    player1 = Players("Joe Montana", "QB")
    player2 = Players("Barry Sanders", "RB")
    player3 = Players("Jerry Rice", "WR")
    player4 = Players("Graham Gano", "K")

    # Add the players to a list.
    playerList = [player1, player2, player3, player4]

    # Create one team with the team name and player list.
    team = NFLTeam("Smashmouth Football", playerList)

    # Print the team name and all of its players.
    team.displayTeam()


if __name__ == "__main__":
    main()