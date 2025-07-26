"""
Basic unit tests for ApacheConfigLinter core functionality.
"""

import os
import pytest
from apache_httpd_config_linter.linter import ApacheConfigLinter

def get_test_config_path(filename):
    return os.path.join(os.path.dirname(__file__), "configs", filename)

def test_detect_insecure_directory_all(monkeypatch):
    linter = ApacheConfigLinter()
    config_path = get_test_config_path("insecure_directory.conf")
    results = linter.lint_file(config_path)
    assert any(
        "AllowOverride All" in finding["description"]
        for finding in results
    ), "Should detect insecure AllowOverride All"

def test_detect_missing_server_tokens(monkeypatch):
    linter = ApacheConfigLinter()
    config_path = get_test_config_path("missing_servertokens.conf")
    results = linter.lint_file(config_path)
    assert any(
        "ServerTokens" in finding["description"]
        for finding in results
    ), "Should flag missing ServerTokens directive"

def test_detect_mod_status_enabled(monkeypatch):
    linter = ApacheConfigLinter()
    config_path = get_test_config_path("mod_status_enabled.conf")
    results = linter.lint_file(config_path)
    assert any(
        "mod_status" in finding["description"] and finding["severity"] == "LOW"
        for finding in results
    ), "Should warn about mod_status being enabled"

def test_no_findings_on_hardened_config(monkeypatch):
    linter = ApacheConfigLinter()
    config_path = get_test_config_path("hardened.conf")
    results = linter.lint_file(config_path)
    assert len(results) == 0, "Hardened config should have no findings"
