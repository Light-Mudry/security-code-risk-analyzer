from analyzer.sinks import SINKS


def test_system_is_command_execution_sink():
    sink = next(
        sink for sink in SINKS
        if sink["pattern"] == "system("
    )

    assert sink["type"] == "COMMAND_EXECUTION"
    assert sink["cwe"] == "CWE-78"


def test_strcpy_is_buffer_copy_sink():
    sink = next(
        sink for sink in SINKS
        if sink["pattern"] == "strcpy("
    )

    assert sink["type"] == "BUFFER_COPY"
    assert sink["cwe"] == "CWE-120"


def test_sprintf_is_formatted_output_sink():
    sink = next(
        sink for sink in SINKS
        if sink["pattern"] == "sprintf("
    )

    assert sink["type"] == "FORMATTED_OUTPUT"
    assert sink["cwe"] == "CWE-134"