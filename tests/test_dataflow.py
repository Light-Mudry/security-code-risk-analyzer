from analyzer.dataflow import extract_assignments


def test_extract_simple_assignment():
    code = """
    char *cmd = input;
    """

    assignments = extract_assignments(code)

    assert assignments["cmd"] == "input"


def test_extract_multiple_assignments():
    code = """
    char *cmd = input;
    char *name = username;
    """

    assignments = extract_assignments(code)

    assert assignments["cmd"] == "input"
    assert assignments["name"] == "username"


def test_no_assignment():
    code = """
    system(input);
    """

    assignments = extract_assignments(code)

    assert assignments == {}