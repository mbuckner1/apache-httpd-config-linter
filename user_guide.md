# User Guide

## Apache HTTPD Config Linter: Detailed User Guide

### Overview

This guide provides detailed instructions for installing, configuring, and using the Apache HTTPD Config Linter. The linter is a command-line tool that scans Apache HTTP Server configuration files to identify security risks, deprecated directives, and common misconfigurations. Its goal is to help system administrators, DevOps engineers, and security professionals maintain secure and robust server configurations.

---

### Key Features

- Comprehensive Scanning: Detects insecure directives, missing security best practices, and deprecated or risky modules.
- Clear Reporting: Outputs human-readable findings with file/line context, severity ratings, and actionable recommendations.
- CI/CD Friendly: Supports JSON output for integration with automation and CI pipelines.
- Customizable: Allows adding or disabling rules via configuration files.
- Extensible: Easily add new rules or checks to suit your organization’s needs.

---

## Installation

### 1. Prerequisites

- **Python 3.7+** is required.
- Recommended to use a virtual environment.

### 2. Install via PyPI

```sh
pip install apache-httpd-config-linter
```

### 3. Install from Source

```sh
git clone https://github.com/yourorg/apache_httpd_config_linter.git
cd apache_httpd_config_linter
pip install .
```

---

## Usage

### 1. Basic Scan

To scan a single Apache config file:

```sh
apache-httpd-config-linter /path/to/httpd.conf
```

### 2. Recursively Scan a Directory

To scan all config files in a directory (and subdirectories):

```sh
apache-httpd-config-linter /etc/httpd/
```

### 3. View Help and Available Options

```sh
apache-httpd-config-linter --help
```

### 4. Output Formats

- **Default:** Rich, colored CLI output for easy human reading.
- **JSON:** For machine parsing or CI integration:

```sh
apache-httpd-config-linter --format json /path/to/httpd.conf
```

---

## Interpreting Results

Each finding contains:

- **Rule ID:** Identifier for the specific check.
- **Severity:** `HIGH`, `MEDIUM`, `LOW`, or `INFO`.
- **Description:** Explanation of the detected issue.
- **File and Line:** Where the issue is found.
- **Recommendation:** How to remediate the issue.

#### Example Output

```
[HIGH] [Rule: DIR_ALLOWOVERRIDE_ALL]
Description: AllowOverride All is enabled, which can allow .htaccess files to override security settings.
File: insecure_directory.conf:2
Recommendation: Set AllowOverride to 'None' and move configuration to the main file.
```

---

## Advanced Usage

### 1. Custom Rules and Exclusions

You may configure which rules are enforced or suppressed by creating a YAML-based configuration file:

```yaml
rules:
  suppress:
    - DIR_ALLOWOVERRIDE_ALL
    - MOD_STATUS_EXPOSED
```

Run with a custom config:

```sh
apache-httpd-config-linter --config my_linter_config.yaml /path/to/httpd.conf
```

### 2. CI/CD Integration

The linter can be used as part of automated pipelines. Use the JSON output and nonzero exit codes to fail builds on critical findings.

```sh
apache-httpd-config-linter --format json /etc/httpd/conf/httpd.conf
```

---

## Troubleshooting

- **Nothing is detected, but configs are insecure:** Make sure the configuration files are valid and readable.
- **False positives/negatives:** Check the [Rules Reference](rules_reference.md) for rule descriptions and how to customize them.
- **Command not found:** Ensure your `PATH` includes the Python scripts directory.

---

## Getting Help

- **Documentation:** See other files in the `docs/` directory for rule details and developer information.
- **Community:** File issues or ask questions on the project GitHub page.
- **Contributing:** See [developer_guide.md](developer_guide.md) for guidance on adding new rules or features.

---

## Example Workflow

1. Install the linter.
2. Run the linter on your Apache config files.
3. Review the output and apply the recommended changes.
4. Optionally, integrate the linter into your CI/CD process to ensure ongoing compliance.

---

## Frequently Asked Questions

See [faq.md](faq.md) for answers to common questions.

---
