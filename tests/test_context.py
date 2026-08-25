from analyzer.context import assess_confidence


def test_system_with_variable_has_high_confidence():
    confidence = assess_confidence(
        "system(",
        "system(input);"
    )

    assert confidence == "HIGH"


def test_system_with_constant_has_medium_confidence():
    confidence = assess_confidence(
        "system(",
        'system("ls -la");'
    )

    assert confidence == "MEDIUM"


def test_strcpy_with_constant_remains_high_confidence():
    confidence = assess_confidence(
        "strcpy(",
        'strcpy(buffer, "Hello");'
    )

    assert confidence == "HIGH"


def test_unknown_pattern_has_high_confidence():
    confidence = assess_confidence(
        "unknown(",
        "unknown(input);"
    )

    assert confidence == "HIGH"