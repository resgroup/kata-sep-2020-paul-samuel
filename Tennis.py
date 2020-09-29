from enum import Enum


class TennisScore(Enum):
    Zero = "0"
    Fifteen = "15"
    Thirty = "30"
    Forty = "40"
    Advantage = "A"
    Win = "Win"


class TennisGame:

    def __init__(self):
        self._server_score = TennisScore.Zero
        self._returner_score = TennisScore.Zero

    def score_point(self, is_server):
        if is_server:
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

    def set_score(self, is_server, score):
        if is_server:
            self._server_score = score
        else:
            self._returner_score = score

    def get_score(self):
        return self._server_score.value + ":" + self._returner_score.value

    def server_wins(self):
        return self._server_score == TennisScore.Win

    def returner_wins(self):
        return self._returner_score == TennisScore.Win
