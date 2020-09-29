server_score = 0
returner_score = 0


def score_point(is_server):
    return


def set_score(is_server, score):
    if is_server:
        server_score = score
    else:
        returner_score = score

    return


def get_score():
    return str(server_score) + ":" + str(returner_score)
