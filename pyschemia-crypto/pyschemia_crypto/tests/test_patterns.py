"""
Pattern Compliance Testing

Validates pattern enforcement across all cryptographic layers per 
OBINexus Standard v1.0 Section 2.
"""

import pytest
from pyschemia_crypto.legacy.rsa_2048.pattern import PatternEnforcer as LegacyRSA
from pyschemia_crypto.stable.rsa_3072.pattern import PatternEnforcer as StableRSA
from pyschemia_crypto.common.automaton import ValidationResult

class TestPatternCompliance:
    """Validate pattern enforcement across all cryptographic layers."""
    
    @pytest.mark.parametrize("enforcer_class,valid_digest", [
        (LegacyRSA, "RSA-2048:" + "a" * 512),
        (StableRSA, "RSA-3072:" + "b" * 768),
    ])
    def test_pattern_recognition(self, enforcer_class, valid_digest):
        """Test mandatory pattern recognition per OBINexus Section 2.1."""
        enforcer = enforcer_class()
        
        # Valid pattern should be accepted
        result = enforcer.enforce_primitive_pattern(valid_digest, "audit_verification")
        assert result == ValidationResult.ACCEPT_VALIDATED
        
        # Invalid pattern should be rejected
        invalid_digest = "INVALID-PATTERN:xyz123"
        result = enforcer.enforce_primitive_pattern(invalid_digest, "audit_verification")
        assert result == ValidationResult.REJECT_UNKNOWN_PATTERN
    
    def test_context_validation(self):
        """Test context validation enforcement."""
        enforcer = LegacyRSA()
        valid_digest = "RSA-2048:" + "a" * 512
        
        # Invalid context should be rejected
        result = enforcer.enforce_primitive_pattern(valid_digest, "invalid_context")
        assert result == ValidationResult.REJECT_CONTEXT_VIOLATION
    
    def test_legacy_security_enforcement(self):
        """Test legacy security level enforcement."""
        enforcer = LegacyRSA()
        valid_digest = "RSA-2048:" + "a" * 512
        
        # Production context should reject legacy primitives
        result = enforcer.enforce_primitive_pattern(valid_digest, "production")
        assert result == ValidationResult.REJECT_DEPRECATED_SECURITY
