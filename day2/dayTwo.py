class GameAnalyzer():
    
    legal = {
        "red": 12,
        "green": 13,
        "blue": 14,
    }

    def __init__(self, filepath) -> None:
        self.read_input(filepath)

    def read_input(self, filepath: str) -> None:
        with open(filepath, "r") as file:
            lines = file.readlines()
        self.games = {}
        for line in lines:
            splitLine = line.split(":")
            replacedString = splitLine[1].replace(";", ",")
            gameID = int(splitLine[0].split(" ")[1])
            self.games[gameID] = []
            for hand in replacedString.split(","):
                hand = hand.strip().split()
                self.games[gameID].append((int(hand[0]), hand[1]))
    
    def checkLegalMove(self, game):
        for amount, color in game:
            if amount > self.legal[color]:
                return False
        return True
            
    def checkAll(self):
        self.sumOfIDs = 0
        for gameID in self.games:
            print(f"{self.games[gameID]}", end=" ")
            if self.checkLegalMove(self.games[gameID]):
                self.sumOfIDs += gameID
                print("-> TRUE")
            else:
                print("-> FALSE")
        return self.sumOfIDs


if __name__ == "__main__":
    # Usage example
    file_path: str = "day2/dayTwoInput.txt"
    reader = GameAnalyzer(file_path)
    sumOfIDs = reader.checkAll()
    print(f"Sum of IDs: {sumOfIDs}")