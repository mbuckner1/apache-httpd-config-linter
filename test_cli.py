"""
Integration tests for the Apache HTTPD Config Linter command-line interface.
"""

import subprocess
import os
import sys

def get_test_config_path(filename):
    return os.path.join(os.path.dirname(__file__), "configs", filename)

def test_cli_basic_scan():
    config_path = get_test_config_path("insecure_directory.conf")
    result = subprocess.run(
        [sys.executable, "-m", "apache_httpd_config_linter", config_path],
        capture_output=True, text=True
    )
    assert "AllowOverride All" in result.stdout
    assert result.returncode == 0

def test_cli_json_output():
    config_path = get_test_config_path("missing_servertokens.conf")
    result = subprocess.run(
        [sys.executable, "-m", "apache_httpd_config_linter", config_path, "--format", "json"],
        capture_output=True, text=True
    )
    assert result.returncode == 0
    assert result.stdout.strip().startswith("[") or result.stdout.strip().startswith("{")

def test_cli_help():
    result = subprocess.run(
        [sys.executable, "-m", "apache_httpd_config_linter", "--help"],
        capture_output=True, text=True
    )
    assert "usage" in result.stdout.lower()
    assert result.returncode == 0
