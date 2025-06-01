"""
RSA-2048 Legacy Primitive Configuration

Implements legacy cryptographic primitive support per OBINexus 
Cryptographic Interoperability Standard v1.0 Section 3.
"""

from dataclasses import dataclass, field
from typing import Pattern, Dict
import re

@dataclass(frozen=True)
class RSA2048Config:
    """RSA-2048 primitive configuration following OBINexus v1.0 standard."""
    
    algorithm: str = "RSA-2048"
    key_size: int = 2048
    pattern: Pattern = field(default_factory=lambda: re.compile(r"^RSA-2048:[a-fA-F0-9]{512}$"))
    security_level: str = "legacy"
    digest_length: int = 512
    
    # Compatibility matrix per OBINexus Section 3.2
    compatibility_matrix: Dict[str, bool] = field(default_factory=lambda: {
        'legacy': True,
        'stable': True, 
        'modern': True,
        'experimental': False
    })

# Pattern validation constants
CANONICAL_PATTERN = "RSA-2048:[a-fA-F0-9]{512}"
SECURITY_POLICY = "LEGACY_COMPATIBILITY"
ALLOWED_CONTEXTS = {
    "legacy_migration",
    "compatibility_testing",
    "audit_verification"
}
