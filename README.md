Security Code Risk Analyzer 🔐

An automated source-code security analysis tool designed to identify potentially risky coding patterns, trace unsafe data flows, and estimate security risk using static analysis.

Overview

Security Code Risk Analyzer is a Python-based security analysis project focused on identifying potentially vulnerable patterns in source code.

The analyzer combines:

- Static source-code analysis
- Security rule-based detection
- Source-to-sink dataflow analysis
- Context-aware confidence analysis
- CWE-oriented findings
- Risk scoring
- Automated testing

The project is designed as an experimental and extensible foundation for exploring automated security analysis and secure coding practices.

Key Features

🔎 Static Code Analysis

The analyzer scans source files and applies security-oriented rules to identify potentially dangerous coding patterns.

🔗 Source-to-Sink Dataflow Analysis

The project tracks data flows between defined sources and sinks to identify potentially unsafe paths.

This allows the analyzer to reason beyond isolated code patterns and detect when potentially untrusted data reaches security-sensitive operations.

🎯 Context-Aware Confidence Analysis

Detected findings include a confidence assessment based on the surrounding code context.

This helps provide more informative findings than simple pattern matching alone.

📊 Risk Scoring

The analyzer calculates an overall risk score from 0 to 100 and assigns a corresponding risk level.

Example levels include:

SAFE
MEDIUM
HIGH

🧩 CWE-Oriented Findings

Security findings include CWE identifiers together with additional information such as:

- Severity
- Finding name
- Source-code line
- Confidence
- Evidence
- Description

🧪 Automated Testing

The project includes a pytest test suite covering:

- Code scanning
- Security rules
- Risk analysis
- Source detection
- Sink detection
- Dataflow propagation
- Context analysis

Example source files are provided under "samples/" to demonstrate safer and vulnerable coding patterns.

---

Analysis Pipeline

The analyzer is organized around the following workflow:

Source Code
    │
    ▼
┌──────────────┐
│   Scanner    │
└──────┬───────┘
       │
       ▼
┌──────────────┐
│    Rules     │
└──────┬───────┘
       │
       ├───────────────┐
       ▼               ▼
   Sources           Sinks
       │               │
       └───────┬───────┘
               ▼
      ┌─────────────────┐
      │ Dataflow / Flow │
      └────────┬────────┘
               │
               ▼
      ┌─────────────────┐
      │ Context Analysis│
      └────────┬────────┘
               │
               ▼
      ┌─────────────────┐
      │   Risk Scoring  │
      └────────┬────────┘
               │
               ▼
         Security Findings

---

Project Structure

security-code-risk-analyzer/
├── analyzer/
│   ├── __init__.py
│   ├── __main__.py
│   ├── context.py
│   ├── dataflow.py
│   ├── flow.py
│   ├── risk.py
│   ├── rules.py
│   ├── scanner.py
│   ├── sinks.py
│   └── sources.py
│
├── samples/
│   ├── safe/
│   └── vulnerable/
│
├── tests/
│   ├── test_context.py
│   ├── test_dataflow.py
│   ├── test_flow.py
│   ├── test_risk.py
│   ├── test_scanner.py
│   ├── test_sinks.py
│   └── test_sources.py
│
├── pytest.ini
├── requirements.txt
├── .gitignore
└── README.md

Core Components

Component| Purpose
"scanner.py"| Scans source code and produces security findings
"rules.py"| Defines security-oriented detection rules
"sources.py"| Handles potential data sources
"sinks.py"| Handles security-sensitive sinks
"flow.py"| Supports source-to-sink flow analysis
"dataflow.py"| Performs dataflow propagation
"context.py"| Performs context-aware confidence analysis
"risk.py"| Calculates risk levels and scores
"__main__.py"| Provides the command-line interface
"tests/"| Automated tests for the analysis components
"samples/"| Safe and vulnerable example programs

---

Getting Started

Requirements

- Python 3.12+
- pip
- Git

Installation

Clone the repository and install the dependencies:

git clone https://github.com/Light-Mudry/security-code-risk-analyzer.git
cd security-code-risk-analyzer
pip install -r requirements.txt

Analyze a Source File

The analyzer can be executed directly as a Python module:

python -m analyzer <source_file>

For example:

python -m analyzer samples/vulnerable/buffer_overflow.c

The analyzer reports:

- The analyzed file
- Overall risk level
- Risk score out of 100
- Detected findings
- Severity
- CWE
- Source-code line
- Confidence
- Evidence
- Description

Example output structure:

========================================
     SECURITY CODE RISK ANALYZER
========================================

File: samples/vulnerable/example.c

Risk level : HIGH
Risk score : 70/100

Findings
----------------------------------------
[HIGH] CWE-XXX
Name       : Example security issue
Line       : 12
Confidence : ...
Evidence   : ...
Description: ...
----------------------------------------

«The exact findings and scores depend on the source file being analyzed.»

---

Running the Tests

Run the complete test suite with:

pytest

The repository contains dedicated tests for the major analysis components:

test_scanner.py
test_risk.py
test_sources.py
test_sinks.py
test_flow.py
test_dataflow.py
test_context.py

The test corpus includes both vulnerable and safer examples.

For example:

buffer_overflow.c  → HIGH
safe_copy.c        → SAFE

---

Example Analysis

The project includes two main categories of sample code:

samples/
├── safe/
└── vulnerable/

This makes it possible to experiment with the analyzer on contrasting implementations and evaluate how the security analysis behaves in different contexts.

---

Technologies

- Python 3.12+
- pytest
- Static analysis
- Dataflow analysis
- Source-to-sink analysis
- Rule-based security analysis
- CWE-oriented security findings
- Risk scoring
- Git / GitHub

---

Current Focus

This project currently explores:

- Automated source-code security analysis
- Vulnerability-oriented rule design
- Source-to-sink dataflow tracking
- Context-aware security findings
- Risk scoring
- Automated security testing

---

Future Work

Potential directions for future development include:

- Expanding the security rule set
- Supporting additional vulnerability classes
- Improving dataflow propagation
- Extending context-aware analysis
- Improving risk scoring
- Expanding CWE coverage
- Supporting additional programming languages
- Generating richer analysis reports
- Expanding the automated test corpus
- Exploring more advanced static and dynamic analysis techniques

---

Disclaimer

This project is intended for educational, research, and defensive security purposes.

Automated analysis can produce both false positives and false negatives. The results should therefore not be considered a replacement for comprehensive security auditing or professional security testing.

---

Author

Lumière Minka

Software Engineer interested in:

- Cybersecurity
- Linux systems
- Container security
- Cloud computing
- Vulnerability analysis
- Secure software engineering
- Systems research
