from analyzer.sources import SOURCES


def test_gets_is_user_input():
    rule = next(
        rule for rule in SOURCES
        if rule["pattern"] == "gets("
    )

    assert rule["type"] == "USER_INPUT"
    assert rule["confidence"] == "HIGH"


def test_getenv_is_environment_input():
    rule = next(
        rule for rule in SOURCES
        if rule["pattern"] == "getenv("
    )

    assert rule["type"] == "ENVIRONMENT_INPUT"


def test_scanf_is_user_input():
    rule = next(
        rule for rule in SOURCES
        if rule["pattern"] == "scanf("
    )

    assert rule["type"] == "USER_INPUT"