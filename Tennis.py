from enum import Enum


class TennisScore(Enum):
    Zero = "0"
    Fifteen = "15"
    Thirty = "30"
    Forty = "40"
    Advantage = "A"
    Win = "Win"


class TennisPlayer(Enum):
    Server = "Server"
    Receiver = "Receiver"


class TennisGame:

    def __init__(self, server_score, receiver_score):
        self._server_score = server_score
        self._returner_score = receiver_score

    def score_point(self, player):
        if player == TennisPlayer.Server:
            self._server_score, self._returner_score = self._add_to_existing_score(self._server_score, opponent_score=self._returner_score)
        else:
            self._returner_score, self._server_score = self._add_to_existing_score(self._returner_score, opponent_score=self._server_score)

    @staticmethod
    def _add_to_existing_score(score, opponent_score):
        if score == TennisScore.Zero:
            return TennisScore.Fifteen, opponent_score
        elif score == TennisScore.Fifteen:
            return TennisScore.Thirty, opponent_score
        elif score == TennisScore.Thirty:
            return TennisScore.Forty, opponent_score
        elif score == TennisScore.Forty:
            if opponent_score == TennisScore.Forty:
                return TennisScore.Advantage, opponent_score
            elif opponent_score == TennisScore.Advantage:
                return TennisScore.Forty, TennisScore.Forty
            else:
                return TennisScore.Win, opponent_score
        elif score == TennisScore.Advantage:
            return TennisScore.Win, opponent_score
        else:
            raise ValueError('Invalid score: ' + str(score))

    def get_score(self):
        return self._server_score.value + ":" + self._returner_score.value

    def is_winner(self, player):
        if player == TennisPlayer.Server:
            return self._server_score == TennisScore.Win
        else:
            return self._returner_score == TennisScore.Win
