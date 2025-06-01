# PySchemia-Crypto

> OBINexus Cryptographic Interoperability Layer

[![CI Status](https://github.com/obinexus/pyschemia-crypto/workflows/CI/badge.svg)](https://github.com/obinexus/pyschemia-crypto/actions)
[![PyPI version](https://badge.fury.io/py/pyschemia-crypto.svg)](https://badge.fury.io/py/pyschemia-crypto)
[![Coverage Status](https://codecov.io/gh/obinexus/pyschemia-crypto/branch/main/graph/badge.svg)](https://codecov.io/gh/obinexus/pyschemia-crypto)

## Overview

PySchemia-Crypto implements the **OBINexus Cryptographic Interoperability Standard v1.0**, providing regex-based primitive matching and isomorphic reduction for distributed cryptographic systems.

## Features

- **Regex-Based Pattern Matching**: Deterministic cryptographic primitive identification
- **Isomorphic Reduction**: Unicode normalization eliminating encoding-based exploits  
- **Non-Monolithic Architecture**: Separate legacy, stable, and experimental primitive support
- **Cross-Language Compatibility**: Consistent behavior across Python, Lua, and C
- **Secure Audit Trails**: Cryptographic-grade logging with pattern hash references

## Installation

```bash
# Stable release
pip install pyschemia-crypto

# Legacy compatibility
pip install pyschemia-crypto==1.0.0-legacy

# Experimental features
pip install pyschemia-crypto==1.0.0-experimental
```

## Quick Start

```python
from pyschemia_crypto import normalize_primitive_input
from pyschemia_crypto.stable.rsa_3072 import PatternEnforcer

# Normalize primitive input
canonical = normalize_primitive_input("rsa-3072:abc123")
# Result: "RSA-3072:ABC123"

# Validate cryptographic primitive
enforcer = PatternEnforcer()
result = enforcer.enforce_primitive_pattern(canonical, "production_deployment")
```

## Architecture

The package follows a non-monolithic structure separating cryptographic primitives by security level:

- `legacy/`: RSA-2048, AES-128 (compatibility only)
- `stable/`: RSA-3072, AES-256 (production ready)  
- `experimental/`: RSA-4096, ECDSA-P384 (future standards)

## Compliance

This package implements the formal specification defined in the OBINexus Cryptographic Interoperability Standard v1.0, ensuring:

- Deterministic pattern matching across deployments
- Security invariant preservation under encoding variations
- Comprehensive audit trail generation
- Cross-language regex compatibility

## Documentation

- [API Reference](docs/api_reference.md)
- [Implementation Guide](docs/implementation_guide.md)
- [Compliance Matrix](docs/compliance_matrix.md)

## License

MIT License - see [LICENSE](LICENSE) file for details.

## Contributing

Please read our contributing guidelines and ensure all changes maintain compliance with the OBINexus standard.
