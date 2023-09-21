class Player:
    def play(self):
        print("The player is playing cricket.")

class Batsman(Player):
    def play(self):
        print("The batsman is batting.")

class Bowler(Player):
    def play(self):
        print("The bowler is bowling.")

batsman = Batsman()
batsman.play() # The batsman is batting.

bowler = Bowler()
bowler.play() # The bowler is bowling.
