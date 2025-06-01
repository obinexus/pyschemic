"""
RSA-3072 Stable Primitive Configuration

Implements stable production cryptographic primitive per OBINexus 
Cryptographic Interoperability Standard v1.0.
"""

from dataclasses import dataclass, field
from typing import Pattern, Dict
import re

@dataclass(frozen=True)
class RSA3072Config:
    """RSA-3072 primitive configuration following OBINexus v1.0 standard."""
    
    algorithm: str = "RSA-3072"
    key_size: int = 3072
    pattern: Pattern = field(default_factory=lambda: re.compile(r"^RSA-3072:[a-fA-F0-9]{768}$"))
    security_level: str = "stable"
    digest_length: int = 768
    
    # Compatibility matrix per OBINexus Section 3.2
    compatibility_matrix: Dict[str, bool] = field(default_factory=lambda: {
        'legacy': True,
        'stable': True,
        'modern': True, 
        'experimental': True
    })

# Pattern validation constants
CANONICAL_PATTERN = "RSA-3072:[a-fA-F0-9]{768}"
SECURITY_POLICY = "FIPS_140_2_LEVEL_3"
ALLOWED_CONTEXTS = {
    "key_generation",
    "signature_verification",
    "production_deployment",
    "audit_verification",
    "legacy_migration"
}
