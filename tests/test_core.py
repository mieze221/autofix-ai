# tests/test_core.py
import pytest
from autofix.core import check_internet, check_disk_space, check_cpu_usage, check_ram, check_program

def test_check_internet():
    result = check_internet()
    assert isinstance(result, str)  # Should return a string
    assert "Internet" in result or "No internet" in result

def test_check_disk_space():
    result = check_disk_space()
    assert isinstance(result, str)
    assert "Disk space" in result

def test_check_cpu_usage():
    result = check_cpu_usage()
    assert isinstance(result, str)
    assert "CPU usage" in result

def test_check_ram():
    result = check_ram()
    assert isinstance(result, str)
    assert "RAM usage" in result

def test_check_program():
    result = check_program("python")
    assert isinstance(result, str)
