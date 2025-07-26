# Apache HTTPD Config Linter

[![License](https://img.shields.io/badge/license-Apache%202.0-blue.svg)](LICENSE)
[![Python](https://img.shields.io/badge/python-3.7%2B-blue.svg)](https://www.python.org/downloads/)

## Overview

**Apache HTTPD Config Linter** is a command-line utility designed to scan and analyze Apache `httpd.conf` configuration files for insecure, deprecated, or risky directives. Its primary goal is to help system administrators, DevOps engineers, and developers proactively identify misconfigurations and security weaknesses in their Apache HTTP Server deployments.

With an ever-evolving threat landscape and the complexity of maintaining secure web server configurations, this tool provides **actionable recommendations** for strengthening the security and robustness of your Apache server setup.

---

## Features

- **Comprehensive Scanning:** Examines Apache HTTPD configuration files for a wide range of security issues and best practice violations.
- **Security-Focused Analysis:** Detects insecure or deprecated directives, unsafe permissions, and risky modules.
- **Actionable Recommendations:** Offers clear explanations and step-by-step guidance for remediation.
- **Custom Rule Support:** Allows users to define and extend custom linting rules.
- **CI/CD Integration:** Easily fits into automation pipelines for continuous security validation.
- **Modular Design:** Well-structured, making it easy to adapt, extend, or integrate.
- **Informative Reporting:** Generates detailed reports highlighting issues, severity levels, and suggested fixes.

---

## Why Use a Config Linter for Apache HTTPD?

Maintaining a secure Apache HTTPD configuration is critical, as misconfigurations can:

- Expose sensitive information
- Enable unnecessary modules or features
- Permit risky file or directory access
- Weaken HTTP security headers
- Allow legacy or deprecated behaviors

Manual configuration reviews are error-prone and can miss subtle but dangerous issues. This linter automates the process, providing a **reproducible, systematic, and up-to-date** security check for your Apache environments.

---

## Security-Focused Checks

Some of the key security aspects the linter examines include:

- **Enabled Modules:** Detects potentially insecure modules (`mod_status`, `mod_info`, etc.) and recommends disabling them if unused.
- **Directory and File Permissions:** Checks for overly permissive `<Directory>` or `<Files>` settings (e.g., `AllowOverride All`, `Options Indexes`).
- **Access Controls:** Ensures proper use of `Require`, `Order`, and `Allow`/`Deny` directives.
- **HTTP Headers:** Verifies secure headers like `X-Frame-Options`, `X-Content-Type-Options`, `Strict-Transport-Security`, etc.
- **TLS/SSL Settings:** Flags weak encryption protocols or ciphers, insecure SSL settings, and missing HTTPS redirects.
- **Deprecated Directives:** Identifies use of deprecated or obsolete configuration options incompatible with recent Apache versions.
- **Server Information Disclosure:** Warns if `ServerTokens` or `ServerSignature` are configured to reveal unnecessary version details.
- **User and Group:** Checks that Apache is not running as root and that user/group permissions are correctly set.
- **Error & Log Handling:** Recommends secure logging practices and checks for safe error reporting.
- **Custom Checks:** Users can extend the linter with organization-specific security requirements.

---

## Installation

### Prerequisites

- Python 3.7 or higher
- pip (Python package manager)

### From PyPI (coming soon)

```bash
pip install apache-httpd-config-linter
```

### From Source

```bash
git clone https://github.com/mbuckner1/apache-httpd-config-linter.git
cd apache-httpd-config-linter
pip install -r requirements.txt
python setup.py install
```

---

## Usage

### Basic Scan

```bash
apache-httpd-config-linter /path/to/httpd.conf
```

### Scan a Custom Config

```bash
apache-httpd-config-linter --config /etc/apache2/sites-enabled/example.conf
```

### Output Report

```bash
apache-httpd-config-linter /path/to/httpd.conf --output report.txt
```

### Use Custom Rules

```bash
apache-httpd-config-linter /path/to/httpd.conf --rules custom_rules.yaml
```

### Integration Example (GitHub Actions)

```yaml
- name: Run Apache HTTPD Config Linter
  run: apache-httpd-config-linter /path/to/httpd.conf
```

---

## Example Output

```text
[HIGH] Found Directory directive with 'AllowOverride All'. Restrict to 'None' or only necessary options.
[MEDIUM] ServerTokens is set to 'Full'. Set to 'Prod' to limit server version disclosure.
[LOW] mod_status enabled without access restrictions. Restrict access to trusted IPs or disable if unused.
```

---

## Configuration & Customization

- **Custom Rules:** Extend or override built-in rules by providing a YAML or JSON file with your own checks.
- **Severity Levels:** Configure which levels (LOW, MEDIUM, HIGH) you want reported.
- **Output Formats:** Supports plain text and JSON output for easy integration with other tools.

---

## Security Best Practices

- **Run Regularly:** Integrate the linter into your CI/CD pipelines or regular server maintenance routines.
- **Follow Recommendations:** Address all HIGH and MEDIUM findings promptly. Use LOW findings as opportunities for further hardening.
- **Least Privilege:** Avoid running Apache with administrative privileges. The linter highlights dangerous user/group settings.
- **Minimize Exposure:** Disable unused modules and restrict access to sensitive URLs and directories.
- **Keep Updated:** Regularly update both Apache HTTPD and the linter tool for the latest features and security checks.

---

## Contributing

Contributions are welcome! Please see [CONTRIBUTING.md](CONTRIBUTING.md) for guidelines.

- Bug reports and feature requests: [GitHub Issues](https://github.com/mbuckner1/apache-httpd-config-linter/issues)
- Pull requests: Fork the repo and submit your improvements.

---

## Roadmap

- [ ] Add more built-in security checks
- [ ] Support for additional output formats (HTML, SARIF)
- [ ] Integration with popular DevSecOps tools
- [ ] Internationalization (i18n) support
- [ ] Web-based report viewer

---

## License

This project is licensed under the [Apache License 2.0](LICENSE).

---

## Disclaimer

This tool is provided as-is and is intended to assist in identifying potential configuration issues. It does not guarantee complete security. Always review findings and consult up-to-date security best practices and documentation for your environment.

---

## References

- [Apache HTTP Server Documentation](https://httpd.apache.org/docs/)
- [OWASP Secure Configuration Guidelines](https://owasp.org/www-project-secure-configuration-guidelines/)
- [Mozilla SSL Configuration Generator](https://ssl-config.mozilla.org/)

---

## Contact

For questions, suggestions, or support, open an issue or contact [mbuckner1](https://github.com/mbuckner1).
