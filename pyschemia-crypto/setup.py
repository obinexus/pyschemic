"""
PySchemia-Crypto Package Setup

Implements OBINexus Cryptographic Interoperability Standard v1.0
with support for non-monolithic version deployment.
"""

from setuptools import setup, find_packages
import os

# Read version from environment or default
version = os.getenv('PACKAGE_VERSION', '1.0.0')
version_suffix = os.getenv('VERSION_SUFFIX', '')

# Read long description
with open('README.md', 'r', encoding='utf-8') as fh:
    long_description = fh.read()

setup(
    name="pyschemia-crypto",
    version=f"{version}{version_suffix}",
    packages=find_packages(),
    include_package_data=True,
    
    # Package metadata
    description="OBINexus Cryptographic Interoperability Layer",
    long_description=long_description,
    long_description_content_type="text/markdown",
    
    author="OBINexus Computing",
    author_email="nnamdi@obinexus.com",
    url="https://github.com/obinexus/pyschemia-crypto",
    
    # Dependencies
    install_requires=[
        "cryptography>=3.4.8",
        "typing-extensions>=4.0.0",
    ],
    
    extras_require={
        "dev": [
            "pytest>=6.0",
            "pytest-cov>=2.12",
            "black>=21.0",
            "mypy>=0.910",
            "flake8>=3.9",
        ],
        "docs": [
            "sphinx>=4.0",
            "sphinx-rtd-theme>=0.5",
        ],
    },
    
    # Classifiers
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Topic :: Security :: Cryptography",
        "Topic :: Software Development :: Libraries :: Python Modules",
    ],
    
    python_requires=">=3.8",
    
    # Entry points for CLI tools
    entry_points={
        "console_scripts": [
            "pyschemia-validate=pyschemia_crypto.cli:validate_command",
        ],
    },
)
