from __future__ import annotations




def GetWinningProbability(rating1: float, rating2: float):
    return 1.0 / (1.0 + 10 ** ((rating1 - rating2) / 400))


def ComputeDeltaRating(ratingPlayer1: float, ratingPlayer2: float, isWinPlayer1: bool) -> float:
    P1 = (1.0 / (1.0 + pow(10, ((ratingPlayer1 - ratingPlayer2) / 400))))
    P2 = (1.0 / (1.0 + pow(10, ((ratingPlayer2 - ratingPlayer1) / 400))))
    #return (isWinPlayer1 - P2), (1 - isWinPlayer1 - P1)
    return (isWinPlayer1 - P2)

