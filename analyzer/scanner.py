from analyzer.rules import RULES
from analyzer.context import assess_confidence

def scan_code(code):
    findings = []

    lines = code.splitlines()

    for line_number, line in enumerate(lines, start=1):

        for rule in RULES:

            if rule["pattern"] in line:

                findings.append({
                    "name": rule["name"],
                    "cwe": rule["cwe"],
                    "severity": rule["severity"],
                    "confidence": assess_confidence(rule["pattern"], line),
                    "line": line_number,
                    "evidence": line.strip(),
                    "description": rule["description"]
                })

    return findings