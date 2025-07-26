setup.py - Packaging configuration for Apache HTTPD Config Linter

This file defines the setuptools-based configuration for packaging and distributing
the Apache HTTPD Config Linter Python project. It specifies metadata, dependencies,
package discovery, entry points for the CLI, and more.
"""

from setuptools import setup, find_packages

setup(
    name="apache-httpd-config-linter",
    version="0.1.0",
    description="A command-line utility to scan Apache httpd.conf files for insecure or risky configuration directives.",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    author="mbuckner1",
    author_email="mbuckner1@example.com",
    url="https://github.com/mbuckner1/apache-httpd-config-linter",
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        "PyYAML>=6.0",
        "rich>=13.0",
    ],
    python_requires=">=3.7",
    entry_points={
        "console_scripts": [
            "apache-httpd-config-linter=apache_httpd_config_linter.__main__:main"
        ]
    },
    license="Apache License 2.0",
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: System Administrators",
        "Topic :: Security",
        "License :: OSI Approved :: Apache Software License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
        "Operating System :: OS Independent",
    ],
    keywords="apache httpd config linter security",
    project_urls={
        "Source": "https://github.com/mbuckner1/apache-httpd-config-linter",
        "Documentation": "https://github.com/mbuckner1/apache-httpd-config-linter#readme",
        "Tracker": "https://github.com/mbuckner1/apache-httpd-config-linter/issues",
    },
)
