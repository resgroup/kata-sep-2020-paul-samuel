
class TennisGame:

    def __init__(self):
        self.server_score = 0
        self.returner_score = 0

    def score_point(self, is_server):
        if is_server:
            self.server_score = self.add_to_existing_score(self.server_score, opponent_score=self.returner_score)
        else:
            self.returner_score = self.add_to_existing_score(self.returner_score, opponent_score=self.server_score)

    @staticmethod
    def add_to_existing_score(score, opponent_score):
        if score == 0:
            return 15
        elif score == 15:
            return 30
        elif score == 30:
            return 40
        elif score == 40:
            if opponent_score == 40:
                return 'A'
            elif opponent_score == 'A':
                # ToDo: Set self.returner_score to 40 using self.set_score() perhaps
                pass
            else:
                return 50
        elif score == 'A':
            return 50
        else:
            raise ValueError('Score is already maximum 40')

    def set_score(self, is_server, score):
        if is_server:
            self.server_score = score
        else:
            self.returner_score = score

    def get_score(self):
        return str(self.server_score) + ":" + str(self.returner_score)

    def server_wins(self):
        return self.server_score == 50

    def returner_wins(self):
        return self.returner_score == 50
