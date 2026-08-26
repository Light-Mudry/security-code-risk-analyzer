from analyzer.flow import find_data_flows


def test_direct_source_to_sink_flow():
    code = """
    char buffer[100];

    gets(buffer);

    system(buffer);
    """

    flows = find_data_flows(code)

    assert len(flows) == 1

    flow = flows[0]

    assert flow["source"] == "Unsafe user input"
    assert flow["variable"] == "buffer"
    assert flow["sink"] == "Command execution"
    assert flow["sink_cwe"] == "CWE-78"


def test_no_flow_when_source_and_sink_use_different_variables():
    code = """
    gets(buffer);

    system(command);
    """

    flows = find_data_flows(code)

    assert flows == []


def test_simple_assignment_flow():
    code = """
    char *cmd = input;

    system(cmd);
    """

    flows = find_data_flows(code)

    assert len(flows) == 0


def test_source_to_sink_through_variable():
    code = """
    char *input = getenv("CMD");
    char *cmd = input;

    system(cmd);
    """

    flows = find_data_flows(code)

    assert len(flows) == 1

    flow = flows[0]

    assert flow["source"] == "Environment variable"
    assert flow["variable"] == "cmd"
    assert flow["sink"] == "Command execution"
    assert flow["sink_cwe"] == "CWE-78"