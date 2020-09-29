from Tennis import TennisGame


def test_first_point():
    tennis_game = TennisGame()
    tennis_game.set_score(True, 0)
    tennis_game.set_score(False, 0)

    tennis_game.score_point(True)

    assert tennis_game.get_score() == "15:0"


def test_returner_point():
    tennis_game = TennisGame()
    tennis_game.set_score(True, 15)
    tennis_game.set_score(False, 15)

    tennis_game.score_point(False)

    assert tennis_game.get_score() == "15:30"


def test_server_point():
    tennis_game = TennisGame()
    tennis_game.set_score(True, 30)
    tennis_game.set_score(False, 30)

    tennis_game.score_point(True)

    assert tennis_game.get_score() == "40:30"


def test_server_wins():
    tennis_game = TennisGame()
    tennis_game.set_score(True, 40)
    tennis_game.set_score(False, 30)

    tennis_game.score_point(True)

    assert tennis_game.server_wins()

    assert tennis_game.get_score() == "Win:30"


def test_returner_wins():
    tennis_game = TennisGame()
    tennis_game.set_score(True, 30)
    tennis_game.set_score(False, 40)

    tennis_game.score_point(False)

    assert tennis_game.returner_wins()

    assert tennis_game.get_score() == "30:Win"


def test_server_advantage():
    tennis_game = TennisGame()
    tennis_game.set_score(True, 40)
    tennis_game.set_score(False, 40)

    tennis_game.score_point(True)

    assert not tennis_game.server_wins()

    assert tennis_game.get_score() == "A:40"


def test_returner_advantage():
    tennis_game = TennisGame()
    tennis_game.set_score(True, 40)
    tennis_game.set_score(False, 40)

    tennis_game.score_point(False)

    assert not tennis_game.returner_wins()

    assert tennis_game.get_score() == "40:A"


def test_server_deuce():
    tennis_game = TennisGame()
    tennis_game.set_score(True, 40)
    tennis_game.set_score(False, 'A')

    tennis_game.score_point(True)

    assert not tennis_game.server_wins()

    assert tennis_game.get_score() == "40:40"


def test_returner_deuce():
    tennis_game = TennisGame()
    tennis_game.set_score(True, 'A')
    tennis_game.set_score(False, 40)

    tennis_game.score_point(False)

    assert not tennis_game.returner_wins()

    assert tennis_game.get_score() == "40:40"


def test_server_win_from_advantage():
    tennis_game = TennisGame()
    tennis_game.set_score(True, 'A')
    tennis_game.set_score(False, 40)

    tennis_game.score_point(True)

    assert tennis_game.server_wins()

    assert tennis_game.get_score() == "Win:40"


def test_returner_win_from_advantage():
    tennis_game = TennisGame()
    tennis_game.set_score(True, 40)
    tennis_game.set_score(False, 'A')

    tennis_game.score_point(False)

    assert tennis_game.returner_wins()

    assert tennis_game.get_score() == "40:Win"
