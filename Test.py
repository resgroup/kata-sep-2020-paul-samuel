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

    assert tennis_game.is_winner(TennisPlayer.Server)

    assert tennis_game.get_score() == "Server Wins"


def test_returner_wins():
    tennis_game = TennisGame(TennisScore.Thirty, TennisScore.Forty)

    tennis_game.score_point(TennisPlayer.Receiver)

    assert tennis_game.is_winner(TennisPlayer.Receiver)

    assert tennis_game.get_score() == "Receiver Wins"


def test_server_advantage():
    tennis_game = TennisGame(TennisScore.Forty, TennisScore.Forty)

    tennis_game.score_point(TennisPlayer.Server)

    assert not tennis_game.is_winner(TennisPlayer.Server)

    assert tennis_game.get_score() == "Advantage Server"


def test_returner_advantage():
    tennis_game = TennisGame(TennisScore.Forty, TennisScore.Forty)

    tennis_game.score_point(TennisPlayer.Receiver)

    assert not tennis_game.is_winner(TennisPlayer.Receiver)

    assert tennis_game.get_score() == "Advantage Receiver"


def test_server_deuce():
    tennis_game = TennisGame(TennisScore.Forty, TennisScore.Advantage)

    tennis_game.score_point(TennisPlayer.Server)

    assert not tennis_game.is_winner(TennisPlayer.Server)

    assert tennis_game.get_score() == "Deuce"


def test_returner_deuce():
    tennis_game = TennisGame(TennisScore.Advantage, TennisScore.Forty)

    tennis_game.score_point(TennisPlayer.Receiver)

    assert not tennis_game.is_winner(TennisPlayer.Receiver)

    assert tennis_game.get_score() == "Deuce"


def test_server_win_from_advantage():
    tennis_game = TennisGame(TennisScore.Advantage, TennisScore.Forty)

    tennis_game.score_point(TennisPlayer.Server)

    assert tennis_game.is_winner(TennisPlayer.Server)

    assert tennis_game.get_score() == "Server Wins"


def test_returner_win_from_advantage():
    tennis_game = TennisGame(TennisScore.Forty, TennisScore.Advantage)

    tennis_game.score_point(TennisPlayer.Receiver)

    assert tennis_game.is_winner(TennisPlayer.Receiver)

    assert tennis_game.get_score() == "Receiver Wins"
