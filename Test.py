import Tennis


def test_first_point():
    Tennis.set_score(is_server=True, score=0)
    Tennis.set_score(is_server=False, score=0)

    Tennis.score_point(is_server=True)

    assert Tennis.get_score() == "15:0"


def test_returner_point():
    Tennis.set_score(is_server=True, score=15)
    Tennis.set_score(is_server=False, score=15)

    Tennis.score_point(is_server=False)

    assert Tennis.get_score() == "15:30"


def test_server_point():
    Tennis.set_score(is_server=True, score=30)
    Tennis.set_score(is_server=False, score=30)

    Tennis.score_point(is_server=True)

    assert Tennis.get_score() == "40:30"
