SINKS = [
    {
        "pattern": "system(",
        "name": "Command execution",
        "type": "COMMAND_EXECUTION",
        "cwe": "CWE-78",
        "severity": "HIGH"
    },
    {
        "pattern": "strcpy(",
        "name": "Unbounded string copy",
        "type": "BUFFER_COPY",
        "cwe": "CWE-120",
        "severity": "HIGH"
    },
    {
        "pattern": "strcat(",
        "name": "Unbounded string concatenation",
        "type": "BUFFER_CONCATENATION",
        "cwe": "CWE-120",
        "severity": "HIGH"
    },
    {
        "pattern": "sprintf(",
        "name": "Unbounded formatted output",
        "type": "FORMATTED_OUTPUT",
        "cwe": "CWE-134",
        "severity": "HIGH"
    }
]