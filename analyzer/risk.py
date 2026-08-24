SEVERITY_SCORES = {
    "LOW": 20,
    "MEDIUM": 40,
    "HIGH": 70,
    "CRITICAL": 90,
}


def calculate_risk(findings):
    if not findings:
        return {
            "score": 0,
            "level": "SAFE",
        }

    total_score = sum(
        SEVERITY_SCORES.get(finding["severity"], 0)
        for finding in findings
    )

    score = min(total_score, 100)

    if score >= 90:
        level = "CRITICAL"
    elif score >= 70:
        level = "HIGH"
    elif score >= 40:
        level = "MEDIUM"
    else:
        level = "LOW"

    return {
        "score": score,
        "level": level,
    }