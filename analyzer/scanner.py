from analyzer.rules import RULES


def scan_code(code):
    findings = []

    for rule in RULES:
        if rule["pattern"] in code:
            findings.append({
                "name": rule["name"],
                "cwe": rule["cwe"],
                "severity": rule["severity"],
                "description": rule["description"]
            })

    return findings