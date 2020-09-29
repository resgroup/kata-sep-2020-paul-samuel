import Tennis


def test_first_point():
    Tennis.set_score(True, 0)
    Tennis.set_score(False, 0)

    Tennis.score_point(True)

    assert Tennis.get_score() == "15:0"


def test_returner_point():
    Tennis.set_score(True, 15)
    Tennis.set_score(False, 15)

    Tennis.score_point(False)

    assert Tennis.get_score() == "15:30"


def test_server_point():
    Tennis.set_score(True, 30)
    Tennis.set_score(False, 30)

    Tennis.score_point(True)

    assert Tennis.get_score() == "40:30"
