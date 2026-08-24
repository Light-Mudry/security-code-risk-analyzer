import sys

from analyzer.scanner import scan_code
from analyzer.risk import calculate_risk


def analyze_file(file_path):
    with open(file_path, "r", encoding="utf-8") as file:
        code = file.read()

    findings = scan_code(code)
    risk = calculate_risk(findings)

    print("=" * 40)
    print("     SECURITY CODE RISK ANALYZER")
    print("=" * 40)

    print(f"\nFile: {file_path}")
    print(f"\nRisk level : {risk['level']}")
    print(f"Risk score : {risk['score']}/100")

    print("\nFindings")
    print("-" * 40)

    if not findings:
        print("No potential security risks detected.")
        return

    for finding in findings:
        print(f"[{finding['severity']}] {finding['cwe']}")
        print(f"Name       : {finding['name']}")
        print(f"Line       : {finding['line']}")
        print(f"Confidence : {finding['confidence']}")
        print(f"Evidence   : {finding['evidence']}")
        print(f"Description: {finding['description']}")
        print("-" * 40)


def main():
    if len(sys.argv) != 2:
        print("Usage: python -m analyzer <source_file>")
        sys.exit(1)

    file_path = sys.argv[1]

    try:
        analyze_file(file_path)
    except FileNotFoundError:
        print(f"Error: file not found: {file_path}")
        sys.exit(1)
    except Exception as error:
        print(f"Error while analyzing file: {error}")
        sys.exit(1)


if __name__ == "__main__":
    main()