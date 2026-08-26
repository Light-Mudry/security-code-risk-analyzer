import re


def extract_assignments(code):
    """
    Extract simple variable assignments from C code.

    Examples:

        char *input = getenv("CMD");
        char *cmd = input;

    Returns:

        {
            "input": 'getenv("CMD")',
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


def resolve_variable(variable, assignments):
    """
    Follow a simple chain of variable assignments.

    Example:

        input = getenv("CMD")
        cmd = input

    resolve_variable("cmd", assignments)

    returns:

        getenv("CMD")
    """

    visited = set()
    current = variable

    while current in assignments and current not in visited:
        visited.add(current)

        value = assignments[current]

        # If the value is another variable, continue following it.
        if re.fullmatch(r"[A-Za-z_]\w*", value):
            current = value
            continue

        return value

    return current