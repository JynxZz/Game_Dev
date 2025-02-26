# Script to handle scoring
# Author: JynxZz
# Date : 15 Feb 2025

import os
from settings import SCORES_FILE


def load_scores():
    if not os.path.exists(SCORES_FILE):
        return {"1P": 0, "2P": 0, "AI": 0}

    with open(SCORES_FILE, "r") as file:
        lines = file.readlines()

    scores = {}

    for line in lines:
        player, score = line.strip().split(": ")
        score[player] = int(score)

    return scores


def save_scores(winner):
    scores = load_scores()

    if winner in scores:
        scores[winner] += 1

    with open(SCORES_FILE, "w") as file:
        for player, score in scores.items():
            file.write(f"{player}: {score}\n")


def get_leaderboard():
    scores = load_scores()
    return sorted(scores.items(), key=lambda x: x[1], reverse=True)
