import re

from analyzer.sources import SOURCES
from analyzer.sinks import SINKS
from analyzer.dataflow import extract_assignments, resolve_variable

def _extract_call_arguments(line, pattern):
    """
    Extract arguments from a function call.

    Example:
        gets(buffer);

    returns:
        ["buffer"]
    """

    function_name = pattern[:-1]

    match = re.search(
        rf"\b{re.escape(function_name)}\s*\((.*?)\)",
        line
    )

    if not match:
        return []

    arguments = match.group(1)

    return [
        argument.strip()
        for argument in arguments.split(",")
        if argument.strip()
    ]


def _find_source_assignment(variable, assignments, sources):
    """
    Determine whether a variable ultimately comes from a known source.

    Example:

        input = getenv("CMD")
        cmd = input

    For "cmd", this resolves to:

        getenv("CMD")
    """

    resolved = resolve_variable(variable, assignments)

    for source in sources:
        function_name = source["pattern"][:-1]

        if re.search(
            rf"\b{re.escape(function_name)}\s*\(",
            resolved
        ):
            return source

    return None


def find_data_flows(code):
    """
    Find simple source-to-sink data flows.

    Supported direct flow:

        gets(buffer);
        system(buffer);

    """

    lines = code.splitlines()

    sources_found = []
    sinks_found = []

    # Detect sources
    for line_number, line in enumerate(lines, start=1):
        for source in SOURCES:
            if source["pattern"] in line:
                sources_found.append({
                    "source": source,
                    "line": line_number,
                    "evidence": line.strip(),
                    "arguments": _extract_call_arguments(
                        line,
                        source["pattern"]
                    )
                })

    # Detect sinks
    for line_number, line in enumerate(lines, start=1):
        for sink in SINKS:
            if sink["pattern"] in line:
                sinks_found.append({
                    "sink": sink,
                    "line": line_number,
                    "evidence": line.strip(),
                    "arguments": _extract_call_arguments(
                        line,
                        sink["pattern"]
                    )
                })

    assignments = extract_assignments(code)

    flows = []

    for source_match in sources_found:
        for sink_match in sinks_found:

            source_variables = source_match["arguments"]
            sink_variables = sink_match["arguments"]

            # Direct flow:
            # gets(buffer) -> system(buffer)
            common_variables = set(source_variables) & set(sink_variables)
                        # Propagated flow:
            #
            # input = getenv("CMD");
            # cmd = input;
            # system(cmd);

            for sink_variable in sink_variables:

                source = _find_source_assignment(
                    sink_variable,
                    assignments,
                    SOURCES
                )

                if source is None:
                    continue

                flows.append({
                    "source": source["name"],
                    "source_type": source["type"],
                    "source_line": sink_match["line"],
                    "variable": sink_variable,
                    "sink": sink_match["sink"]["name"],
                    "sink_type": sink_match["sink"]["type"],
                    "sink_cwe": sink_match["sink"]["cwe"],
                    "sink_severity": sink_match["sink"]["severity"],
                    "sink_line": sink_match["line"]
                })

            for variable in common_variables:
                flows.append({
                    "source": source_match["source"]["name"],
                    "source_type": source_match["source"]["type"],
                    "source_line": source_match["line"],
                    "variable": variable,
                    "sink": sink_match["sink"]["name"],
                    "sink_type": sink_match["sink"]["type"],
                    "sink_cwe": sink_match["sink"]["cwe"],
                    "sink_severity": sink_match["sink"]["severity"],
                    "sink_line": sink_match["line"]
                })

            # Future support for propagated variables
            for source_variable in source_variables:

                if source_variable not in assignments:
                    continue

                assigned_value = assignments[source_variable]

                if assigned_value in sink_variables:
                    flows.append({
                        "source": source_match["source"]["name"],
                        "source_type": source_match["source"]["type"],
                        "source_line": source_match["line"],
                        "variable": source_variable,
                        "sink": sink_match["sink"]["name"],
                        "sink_type": sink_match["sink"]["type"],
                        "sink_cwe": sink_match["sink"]["cwe"],
                        "sink_severity": sink_match["sink"]["severity"],
                        "sink_line": sink_match["line"]
                    })

    return flows