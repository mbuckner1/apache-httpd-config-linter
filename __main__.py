#!/usr/bin/env python3

"""
Apache HTTPD Config Linter - Main Entrypoint

This script provides a command-line interface for scanning Apache httpd.conf files
for insecure or risky configuration directives. It helps users identify common
misconfigurations and provides recommendations to improve the security and robustness
of their Apache server setup.
"""

import sys
import argparse
from .linter import ApacheConfigLinter

def main():
    parser = argparse.ArgumentParser(
        description="Scan Apache httpd.conf files for insecure or risky configuration directives."
    )
    parser.add_argument(
        "config_path",
        metavar="CONFIG_PATH",
        type=str,
        help="Path to the Apache httpd.conf or site configuration file"
    )
    parser.add_argument(
        "--output", "-o",
        type=str,
        default=None,
        help="Optional output file for the report"
    )
    parser.add_argument(
        "--rules",
        type=str,
        default=None,
        help="Custom YAML/JSON rules file"
    )
    parser.add_argument(
        "--format",
        choices=["text", "json"],
        default="text",
        help="Output format for the report"
    )
    args = parser.parse_args()

    linter = ApacheConfigLinter(
        rules_path=args.rules
    )
    results = linter.lint_file(args.config_path)

    if args.format == "json":
        import json
        report = json.dumps(results, indent=2)
    else:
        report = linter.format_report(results)

    if args.output:
        with open(args.output, "w") as f:
            f.write(report)
        print(f"Report written to {args.output}")
    else:
        print(report)

if __name__ == "__main__":
    main()
