from __future__ import annotations

from typing import List

from EloRater import ComputeDeltaRating, GetWinningProbability

from random import random, randint, shuffle

from matplotlib import pyplot as plt

"""
Talk about how you can use multiplier K for fast initial convergence
big K can be used in game for new patch for adjustment too maybe, if ranking has been reset? (not sure if great example)

"""


### CONSTANTS

MIN_INITIAL_RATING = 1000
MAX_INITIAL_RATING = 2000



### CLASSES

class Player:
    def __init__(self):
        self.Rating = randint(MIN_INITIAL_RATING, MAX_INITIAL_RATING)
        self.Skill = random()
    



### FUNCTIONS

def CreatePlayerPool(sizePool: int = 100) -> List[Player]:
    return [Player() for _ in range(sizePool)]


def CreatePairsFromPool(playerPool: List[Player]) -> List[List[Player]]:
    shuffle(playerPool)
    pairs = []
    currPair = []
    for _ in range(len(playerPool)):
        currPair.append(playerPool.pop())
        if len(currPair) == 2:
            pairs.append(currPair)
            currPair = []
    return pairs


def CreatePoolFromPairs(pairs: List[List[Player]]) -> List[Player]:
    playerPool = []
    for p in pairs:
        playerPool += p
    return playerPool

def DrawWinner(skillPlayer1: float, skillPlayer2: float) -> bool:
    return random() < skillPlayer1 / (skillPlayer1 + skillPlayer2)


def RunSimulation(nbRounds: int = 100):
    recordedSkillsRatings = []
    playerPool = CreatePlayerPool(250)
    recordedSkillsRatings.append(
        [(p.Skill, p.Rating) for p in playerPool]
    )

    for idLoop in range(nbRounds):
        pairs = CreatePairsFromPool(playerPool)
        currSkillsRatings = []
        for p in pairs:
            # gotta draw winner
            delta = ComputeDeltaRating(p[0].Rating, p[1].Rating, DrawWinner(p[0].Skill, p[1].Skill))
            p[0].Rating += delta * 30
            p[1].Rating += -delta * 30
            for elem in p:
                currSkillsRatings.append((elem.Skill, elem.Rating))
        recordedSkillsRatings.append(currSkillsRatings)
        playerPool = CreatePoolFromPairs(pairs)

    return recordedSkillsRatings


### CALLED FROM CMD

if __name__ == "__main__":
    rec = RunSimulation()
    # get nb digits for saving records
    nbDigits = len(str(len(rec)))
    for idRecord, record in enumerate(rec):
        strId = str(idRecord)
        while len(strId) < nbDigits:
            strId = "0" + strId
        plt.scatter(*zip(*record))
        plt.axis(ymin = 750, ymax = 2250)
        plt.savefig("OutputImages/round-{}.jpg".format(strId), dpi=300)
        plt.clf()