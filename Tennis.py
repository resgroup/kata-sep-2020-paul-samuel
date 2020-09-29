
class TennisGame:

    def __init__(self):
        self._server_score = 0
        self._returner_score = 0

    def score_point(self, is_server):
        if is_server:
            self._server_score, self._returner_score = self._add_to_existing_score(self._server_score, opponent_score=self._returner_score)
        else:
            self._returner_score, self._server_score = self._add_to_existing_score(self._returner_score, opponent_score=self._server_score)

    @staticmethod
    def _add_to_existing_score(score, opponent_score):
        if score == 0:
            return 15, opponent_score
        elif score == 15:
            return 30, opponent_score
        elif score == 30:
            return 40, opponent_score
        elif score == 40:
            if opponent_score == 40:
                return 'A', opponent_score
            elif opponent_score == 'A':
                return 40, 40
            else:
                return 'Win', opponent_score
        elif score == 'A':
            return 'Win', opponent_score
        else:
            raise ValueError('Score is already maximum 40')

    def set_score(self, is_server, score):
        if is_server:
            self._server_score = score
        else:
            self._returner_score = score

    def get_score(self):
        return str(self._server_score) + ":" + str(self._returner_score)

    def server_wins(self):
        return self._server_score == 'Win'

    def returner_wins(self):
        return self._returner_score == 'Win'
