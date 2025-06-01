"""
RSA-3072 Pattern Enforcement Implementation

Implements mandatory if/else control logic per OBINexus Section 2.1
for stable RSA-3072 cryptographic primitives.
"""

from ...common.automaton import PatternEnforcer as BaseEnforcer, ValidationResult
from .config import RSA3072Config, ALLOWED_CONTEXTS

class PatternEnforcer(BaseEnforcer):
    """RSA-3072 pattern enforcement implementation."""
    
    def __init__(self):
        self.config = RSA3072Config()
    
    def enforce_primitive_pattern(self, 
                                primitive_digest: str, 
                                context: str) -> ValidationResult:
        """
        Mandatory pattern enforcement for RSA-3072 primitives.
        Implements Section 2.1 of OBINexus Standard v1.0.
        """
        # Phase 1: Pattern Recognition
        if not self.config.pattern.match(primitive_digest):
            return ValidationResult.REJECT_UNKNOWN_PATTERN
        
        # Phase 2: Context Validation
        if context not in ALLOWED_CONTEXTS:
            return ValidationResult.REJECT_CONTEXT_VIOLATION
        
        # Phase 3: Compatibility Check
        if not self._validate_compatibility(context):
            return ValidationResult.REJECT_INCOMPATIBLE_VERSION
        
        return ValidationResult.ACCEPT_VALIDATED
    
    def get_canonical_pattern(self):
        """Return canonical regex pattern for RSA-3072."""
        return self.config.pattern
    
    def get_security_level(self) -> str:
        """Return security level: stable."""
        return self.config.security_level
    
    def _validate_compatibility(self, context: str) -> bool:
        """Validate against compatibility matrix."""
        context_map = {
            "production_deployment": "stable",
            "legacy_migration": "legacy",
            "key_generation": "modern"
        }
        
        required_level = context_map.get(context, "stable")
        return self.config.compatibility_matrix.get(required_level, False)
