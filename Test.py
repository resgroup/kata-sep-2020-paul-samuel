from Tennis import TennisGame, TennisScore, TennisPlayer


def test_first_point():
    tennis_game = TennisGame(TennisScore.Zero, TennisScore.Zero)

    tennis_game.score_point(TennisPlayer.Server)

    assert tennis_game.get_score() == "15:0"


def test_returner_point():
    tennis_game = TennisGame(TennisScore.Fifteen, TennisScore.Fifteen)

    tennis_game.score_point(TennisPlayer.Receiver)

    assert tennis_game.get_score() == "15:30"


def test_server_point():
    tennis_game = TennisGame(TennisScore.Thirty, TennisScore.Thirty)

    tennis_game.score_point(TennisPlayer.Server)

    assert tennis_game.get_score() == "40:30"


def test_server_wins():
    tennis_game = TennisGame(TennisScore.Forty, TennisScore.Thirty)

    tennis_game.score_point(TennisPlayer.Server)

    assert tennis_game.server_wins()

    assert tennis_game.get_score() == "Win:30"


def test_returner_wins():
    tennis_game = TennisGame(TennisScore.Thirty, TennisScore.Forty)

    tennis_game.score_point(TennisPlayer.Receiver)

    assert tennis_game.returner_wins()

    assert tennis_game.get_score() == "30:Win"


def test_server_advantage():
    tennis_game = TennisGame(TennisScore.Forty, TennisScore.Forty)

    tennis_game.score_point(TennisPlayer.Server)

    assert not tennis_game.server_wins()

    assert tennis_game.get_score() == "A:40"


def test_returner_advantage():
    tennis_game = TennisGame(TennisScore.Forty, TennisScore.Forty)

    tennis_game.score_point(TennisPlayer.Receiver)

    assert not tennis_game.returner_wins()

    assert tennis_game.get_score() == "40:A"


def test_server_deuce():
    tennis_game = TennisGame(TennisScore.Forty, TennisScore.Advantage)

    tennis_game.score_point(TennisPlayer.Server)

    assert not tennis_game.server_wins()

    assert tennis_game.get_score() == "40:40"


def test_returner_deuce():
    tennis_game = TennisGame(TennisScore.Advantage, TennisScore.Forty)

    tennis_game.score_point(TennisPlayer.Receiver)

    assert not tennis_game.returner_wins()

    assert tennis_game.get_score() == "40:40"


def test_server_win_from_advantage():
    tennis_game = TennisGame(TennisScore.Advantage, TennisScore.Forty)

    tennis_game.score_point(TennisPlayer.Server)

    assert tennis_game.server_wins()

    assert tennis_game.get_score() == "Win:40"


def test_returner_win_from_advantage():
    tennis_game = TennisGame(TennisScore.Forty, TennisScore.Advantage)

    tennis_game.score_point(TennisPlayer.Receiver)

    assert tennis_game.returner_wins()

    assert tennis_game.get_score() == "40:Win"
