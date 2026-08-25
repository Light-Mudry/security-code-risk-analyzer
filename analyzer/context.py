def assess_confidence(pattern, line):
    """
    Estimate the confidence of a security finding
    based on the local code context.
    """

    line = line.strip()

    # A constant command passed to system() is less suspicious
    # than a command that may come from external input.
    if pattern == "system(":
        if '"' in line:
            return "MEDIUM"

    # For strcpy(), strcat() and sprintf(), a constant string
    # does not prove that the operation is safe.
    # Keep high confidence until we perform deeper analysis.
    return "HIGH"