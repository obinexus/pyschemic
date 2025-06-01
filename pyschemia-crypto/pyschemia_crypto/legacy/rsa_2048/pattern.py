"""
RSA-2048 Pattern Enforcement Implementation

Implements mandatory if/else control logic per OBINexus Section 2.1
for legacy RSA-2048 cryptographic primitives.
"""

from typing import Set
from ...common.automaton import PatternEnforcer as BaseEnforcer, ValidationResult
from .config import RSA2048Config, ALLOWED_CONTEXTS

class PatternEnforcer(BaseEnforcer):
    """RSA-2048 pattern enforcement implementation."""
    
    def __init__(self):
        self.config = RSA2048Config()
    
    def enforce_primitive_pattern(self, 
                                primitive_digest: str, 
                                context: str) -> ValidationResult:
        """
        Mandatory pattern enforcement for RSA-2048 primitives.
        Implements Section 2.1 of OBINexus Standard v1.0.
        """
        # Phase 1: Pattern Recognition
        if not self.config.pattern.match(primitive_digest):
            return ValidationResult.REJECT_UNKNOWN_PATTERN
        
        # Phase 2: Context Validation
        if context not in ALLOWED_CONTEXTS:
            return ValidationResult.REJECT_CONTEXT_VIOLATION
        
        # Phase 3: Legacy Security Check
        if context == "production" and self.config.security_level == "legacy":
            return ValidationResult.REJECT_DEPRECATED_SECURITY
        
        return ValidationResult.ACCEPT_VALIDATED
    
    def get_canonical_pattern(self):
        """Return canonical regex pattern for RSA-2048."""
        return self.config.pattern
    
    def get_security_level(self) -> str:
        """Return security level: legacy."""
        return self.config.security_level
