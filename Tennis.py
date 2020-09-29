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
        self._scores = { TennisPlayer.Server: server_score, TennisPlayer.Receiver: receiver_score }

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
        if self._scores[TennisPlayer.Server] == TennisScore.Win:
            return "Server Wins"
        elif self._scores[TennisPlayer.Receiver] == TennisScore.Win:
            return "Receiver Wins"
        elif self._scores[TennisPlayer.Server] == TennisScore.Advantage:
            return "Advantage Server"
        elif self._scores[TennisPlayer.Receiver] == TennisScore.Advantage:
            return "Advantage Receiver"
        elif (self._scores[TennisPlayer.Server] == TennisScore.Forty) and (self._scores[TennisPlayer.Receiver] == TennisScore.Forty):
            return "Deuce"
        else:
            return self._scores[TennisPlayer.Server].value + ":" + self._scores[TennisPlayer.Receiver].value

    def is_winner(self, player):
        return self._scores[player] == TennisScore.Win
