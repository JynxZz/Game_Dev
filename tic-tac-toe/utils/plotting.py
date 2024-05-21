import matplotlib.pyplot as plt
from IPython import display


class TicTacToePlotter:
    def __init__(self):
        self.wins = 0
        self.losses = 0
        self.ties = 0
        self.games = 0

    def upload_results(self, result):
        if result == "Win":
            self.wins += 1
        elif result == "Loss":
            self.losses += 1
        else:
            self.ties += 1
        self.games += 1

    def plot_results(self):
        display.clear_output(wait=True)
        plt.figure(figsize=(10, 5))
        plt.bar(["Wins", "Losses", "Ties"], [self.wins, self.losses, self.ties])
        plt.title(f"Results after {self.games} games")
        plt.show(block=False)
        plt.pause(0.1)
