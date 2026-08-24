RULES = [
    {
        "pattern": "gets(",
        "name": "Unsafe input function",
        "cwe": "CWE-242",
        "severity": "HIGH",
        "description": "gets() does not perform bounds checking and may cause a buffer overflow."
    },
    {
        "pattern": "strcpy(",
        "name": "Unbounded string copy",
        "cwe": "CWE-120",
        "severity": "HIGH",
        "description": "strcpy() copies data without checking the destination buffer size."
    },
    {
        "pattern": "strcat(",
        "name": "Unbounded string concatenation",
        "cwe": "CWE-120",
        "severity": "HIGH",
        "description": "strcat() may overflow the destination buffer if insufficient space is available."
    },
    {
        "pattern": "sprintf(",
        "name": "Unbounded formatted output",
        "cwe": "CWE-134",
        "severity": "HIGH",
        "description": "sprintf() does not limit the amount of data written to the destination buffer."
    },
    {
        "pattern": "system(",
        "name": "Command execution",
        "cwe": "CWE-78",
        "severity": "HIGH",
        "description": "system() executes a command through the shell and may introduce command injection."
    }
]