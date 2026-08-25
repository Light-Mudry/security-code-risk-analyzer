SOURCES = [
    {
        "pattern": "gets(",
        "name": "Unsafe user input",
        "type": "USER_INPUT",
        "confidence": "HIGH"
    },
    {
        "pattern": "getenv(",
        "name": "Environment variable",
        "type": "ENVIRONMENT_INPUT",
        "confidence": "MEDIUM"
    },
    {
        "pattern": "scanf(",
        "name": "User input",
        "type": "USER_INPUT",
        "confidence": "HIGH"
    },
    {
        "pattern": "fgets(",
        "name": "Input stream",
        "type": "USER_INPUT",
        "confidence": "MEDIUM"
    }
]