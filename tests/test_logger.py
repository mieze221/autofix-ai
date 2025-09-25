# tests/test_logger.py
import os
from autofix.logger import log


def test_log_creates_file():
    test_message = "Test log entry"
    log(test_message)

    assert os.path.exists("autofix.log")

    # Check that last line contains tests message
    with open("autofix.log", "r") as f:
        lines = f.readlines()
        assert test_message in lines[-1]

