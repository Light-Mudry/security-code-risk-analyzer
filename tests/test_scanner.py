from analyzer.scanner import scan_code


def test_strcpy_detection():
    code = """
    #include <string.h>

    int main() {
        char buffer[10];
        strcpy(buffer, "Hello");
        return 0;
    }
    """

    findings = scan_code(code)

    assert len(findings) == 1
    assert findings[0]["cwe"] == "CWE-120"
    assert findings[0]["severity"] == "HIGH"
    assert findings[0]["confidence"] == "HIGH"


def test_multiple_risks_detection():
    code = """
    void test(char *input) {
        gets(input);
        strcpy(input, "test");
        strcat(input, "data");
        sprintf(input, "%s", "test");
        system(input);
    }
    """

    findings = scan_code(code)

    assert len(findings) == 5


def test_safe_code():
    code = """
    #include <stdio.h>

    int main(void) {
        printf("Hello World");
        return 0;
    }
    """

    findings = scan_code(code)

    assert len(findings) == 0