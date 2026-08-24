from analyzer.risk import calculate_risk


def test_no_findings_is_safe():
    result = calculate_risk([])

    assert result["score"] == 0
    assert result["level"] == "SAFE"


def test_high_risk():
    findings = [
        {
            "severity": "HIGH"
        }
    ]

    result = calculate_risk(findings)

    assert result["score"] == 70
    assert result["level"] == "HIGH"


def test_multiple_high_risks_are_capped():
    findings = [
        {
            "severity": "HIGH"
        },
        {
            "severity": "HIGH"
        }
    ]

    result = calculate_risk(findings)

    assert result["score"] == 100
    assert result["level"] == "CRITICAL"


def test_medium_risk():
    findings = [
        {
            "severity": "MEDIUM"
        }
    ]

    result = calculate_risk(findings)

    assert result["score"] == 40
    assert result["level"] == "MEDIUM"