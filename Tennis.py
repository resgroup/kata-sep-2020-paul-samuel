from enum import Enum


class TennisScore(Enum):
    Zero = 0
    Fifteen = 1
    Thirty = 2
    Forty = 3
    Fifty = 4
    Advantage = 5
    Win = 6


class TennisPlayer(Enum):
    Server = "Server"
    Receiver = "Receiver"


MAXIMUM_SCORE = TennisScore.Fifty


class TennisGame:

    def __init__(self, server_score, receiver_score):
        self._scores = {TennisPlayer.Server: server_score, TennisPlayer.Receiver: receiver_score}

    def score_point(self, player):
        if player == TennisPlayer.Server:
            self._scores[TennisPlayer.Server], self._scores[TennisPlayer.Receiver] = \
                self._add_to_existing_score(
                    self._scores[TennisPlayer.Server],
                    opponent_score=self._scores[TennisPlayer.Receiver]
                )
        else:
            self._scores[TennisPlayer.Receiver], self._scores[TennisPlayer.Server] = \
                self._add_to_existing_score(
                    self._scores[TennisPlayer.Receiver],
                    opponent_score=self._scores[TennisPlayer.Server]
                )

    @staticmethod
    def _add_to_existing_score(score, opponent_score):
        if score == MAXIMUM_SCORE:
            if opponent_score == MAXIMUM_SCORE:
                return TennisScore.Advantage, opponent_score
            elif opponent_score == TennisScore.Advantage:
                return MAXIMUM_SCORE, MAXIMUM_SCORE
            else:
                return TennisScore.Win, opponent_score
        elif score == TennisScore.Advantage:
            return TennisScore.Win, opponent_score
        else:
            return TennisScore(score.value + 1), opponent_score

    def get_score(self):
        if self._scores[TennisPlayer.Server] == TennisScore.Win:
            return "Server Wins"
        elif self._scores[TennisPlayer.Receiver] == TennisScore.Win:
            return "Receiver Wins"
        elif self._scores[TennisPlayer.Server] == TennisScore.Advantage:
            return "Advantage Server"
        elif self._scores[TennisPlayer.Receiver] == TennisScore.Advantage:
            return "Advantage Receiver"
        elif (self._scores[TennisPlayer.Server] == MAXIMUM_SCORE) and (self._scores[TennisPlayer.Receiver] == MAXIMUM_SCORE):
            return "Deuce"
        else:
            return self.format_score(self._scores[TennisPlayer.Server]) + ":" + self.format_score(self._scores[TennisPlayer.Receiver])

    @staticmethod
    def format_score(score_value):
        if score_value == TennisScore.Zero:
            return "0"
        elif score_value == TennisScore.Fifteen:
            return "15"
        elif score_value == TennisScore.Thirty:
            return "30"
        elif score_value == TennisScore.Forty:
            return "40"
        elif score_value == TennisScore.Fifty:
            return "50"

    def is_winner(self, player):
        return self._scores[player] == TennisScore.Win
