import re


def extract_assignments(code):
    """
    Extract simple variable assignments from C code.

    Example:
        char *cmd = input;

    Returns:
        {
            "cmd": "input"
        }
    """

    assignments = {}

    pattern = re.compile(
        r"\b(?:char\s+\*?|int\s+|long\s+|float\s+|double\s+)"
        r"(\w+)\s*=\s*([^;]+);"
    )

    for match in pattern.finditer(code):
        variable = match.group(1)
        value = match.group(2).strip()

        assignments[variable] = value

    return assignments